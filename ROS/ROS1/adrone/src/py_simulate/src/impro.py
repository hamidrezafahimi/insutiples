#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('py_simulate')
import sys
import rospy
import cv2 as cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import math

cv_image = np.zeros((1, 1, 3), np.uint8)
max_canny1, max_canny2 = 800, 800
max_GuKernelSize = 50
window_capture_name = "Video Capture"
max_value_H, max_value = 360/2, 255
low_H, low_S, low_V = 15, 174, 0
high_H, high_S, high_V = 23, 255, 255
canny1, canny2, GuKernelSize, GuSigma = 131, 0, 7, 1.2
ity, itz = 0, 0
shapeAR=1000
euc, eucFilterIt, eucFIt, areaIt, iter = 0, 0, 0, 0, 0
vecy, vecz, tempvecy, tempvecz, tempArea = 0,0,0,0,0
flag, long_distance, enterance = False, False, False
oldP = [[0,0]]
newP = [[0,0]]

seed = []
is_set = False
camera_matrix = np.float64([[376.744103, 0, 319.513089],
                [0,  376.572581,178.056011],
                [0.0,0.0,      1.000000]])
distortion_matrix = [-0.000545, 0.000835, -0.000038, -0.000143, 0.000000]
distortion_matrix = np.array(distortion_matrix)
distortion_matrix = distortion_matrix.reshape((5,1))
x1, y1 = 1.5, 1
real_rect_info = np.float32([[0, 0, 0], [x1, 0, 0], [x1, y1, 0], [0, y1, 0]])

def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos("Low H", window_capture_name, low_H)
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos("High H", window_capture_name, high_H)
def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos("Low S", window_capture_name, low_S)
def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos("High S", window_capture_name, high_S)
def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos("Low V", window_capture_name, low_V)
def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos("High V", window_capture_name, high_V)

def onMouse(event, x, y, flags, param):
    global seed, is_set, shapeAR, tempArea, oldP, tempvecy, tempvecz
    if event == cv.EVENT_LBUTTONDOWN:
        seed = (x,y)
        print(seed)

        im = cv_image.copy()
        pic = preProcessing(im)
        cntrs, wins = contourExtraction(pic, im)
        minDist=1e7
        dist=-1
        choiceIndex=-1
        i = 0
        for win in wins:
            if cv.pointPolygonTest(win, seed, False)!=-1:
                print(1)
                dist = cv.pointPolygonTest(win, seed, True)
                if minDist>dist:
                    print(2)
                    minDist = dist
                    choiceIndex = i
            i = i+1
        shapeAR = arCalculate(cntrs[choiceIndex], im)
        if shapeAR>100:
            print(shapeAR)
            return
        tempArea = cv.contourArea(wins[choiceIndex])
        tempvecy, tempvecz = rectangleGeometric(cntrs[choiceIndex], im)
        oldP = [[tempvecy, tempvecz]]
        print("oldP", oldP)
        cv.drawContours( im, wins, choiceIndex, (255,0,0), 2);
        print("set info:\t" ,oldP,'\t', shapeAR ,'\t', tempArea ,'\t', tempvecy ,'\t',tempvecz, '\n')
        cv.imshow("operator desicion", im)
        is_set = True

def setWindow(img):
    cv.namedWindow("operator desicion")
    cv.setMouseCallback("operator desicion", onMouse)
    pic = preProcessing(img)
    cntrs, _ = contourExtraction(pic, img)

    cv.imshow("operator desicion", img)
    cv.waitKey()
    cv.destroyAllWindows()

def preProcessing(img):
    # cv.namedWindow(window_capture_name)
    # cv.createTrackbar("Low H", window_capture_name , low_H, max_value_H, on_low_H_thresh_trackbar)
    # cv.createTrackbar("High H", window_capture_name , high_H, max_value_H, on_high_H_thresh_trackbar)
    # cv.createTrackbar("Low S", window_capture_name , low_S, max_value, on_low_S_thresh_trackbar)
    # cv.createTrackbar("High S", window_capture_name , high_S, max_value, on_high_S_thresh_trackbar)
    # cv.createTrackbar("Low V", window_capture_name , low_V, max_value, on_low_V_thresh_trackbar)
    # cv.createTrackbar("High V", window_capture_name , high_V, max_value, on_high_V_thresh_trackbar)
    frame_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    frame_inverse = cv.bitwise_not(frame_threshold)
    # cv.imshow(window_capture_name,frame_inverse)
    # cv.waitKey(30)
    return frame_inverse

def contourExtraction(img, img0):
    _, contours, _ = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_TC89_KCOS)
    polies = []
    windows = []
    print("num of contours:  ", len(contours))
    i=0
    for cnt in contours:
        polies.append(cv.approxPolyDP(cnt,13, True))
        windows.append(reconstructRect(cnt))
    cv.drawContours(img0, windows, -1, (0,255,0), 2)
    return polies, windows;

def fourPSort(cont):
    success = False
    res = []
    if len(cont)==0: return res, success;
    print("cont in fps", cont)
    xm = ym = 0
    for point in cont:
        xm = xm + point[0][0]
        ym = ym + point[0][1]
    xm = xm / len(cont)
    ym = ym / len(cont)
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    for point in cont:
        if (point[0][0]<=xm)and(point[0][1]>=ym):
            c1.append(point)
        elif (point[0][0]>xm)and(point[0][1]>ym):
            c2.append(point)
        elif (point[0][0]>=xm)and(point[0][1]<=ym):
            c3.append(point)
        elif (point[0][0]<xm)and(point[0][1]<ym):
            c4.append(point)
    if (len(c1)==0) or (len(c2)==0) or (len(c3)==0) or (len(c4)==0): return res, success;
    c = c1 + c2 + c3 + c4
    success = True
    return success, c;

def euclideanDist(p, q):
    p1 = np.array(p)
    p2 = np.array(q)
    p1 = p1.ravel()
    p2 = p2.ravel()
    diff = [p1[0]-p2[0], p1[1]-p2[1]]
    return math.sqrt((diff[0]*diff[0])+(diff[1]*diff[1]))

def arCalculate(points, pic):
    if len(points)==1: return 10e6
    cornerPoints = 0
    sorted = []
    max = may = maxDist = 0
    mix = miy = aspRec = 1e6
    pmax = pmay = [[0,0]]
    pmiy = [[0,10e6]]
    pmix = [[10e6,0]]
    pax_ch = pix_ch = pay_ch = piy_ch = False
    rows,cols,_ = pic.shape
    for pnt in points:
        if max<pnt[0][0]: max = pnt[0][0]
        if may<pnt[0][1]: may = pnt[0][1]
        if mix>pnt[0][0]: mix = pnt[0][0]
        if miy>pnt[0][1]: miy = pnt[0][1]
        if (abs(pnt[0][0]-cols)<5 or pnt[0][0]<5) and (abs(pnt[0][1]-rows)<5 or pnt[0][1]<5):
            cornerPoints = cornerPoints + 1
    if cornerPoints>=3 : return 1e6
    for pnt in points:
        # print("it")
        if max == pnt[0][0] and (not pax_ch) :
            pmax = pnt
            pax_ch = True
        if may == pnt[0][1] and (not pay_ch) :
            pmay = pnt
            pay_ch = True
        if mix == pnt[0][0] and (not pix_ch) :
            pmix = pnt
            pix_ch = True
        if miy == pnt[0][1] and (not piy_ch):
            pmiy = pnt
            piy_ch = True
        for pont in points:
            if(maxDist<(pnt[0][0] - pont[0][0])): maxDist = pnt[0][0] - pont[0][0]
    if maxDist>abs(cols-10):
        return 10e6
    is_sorted, sorted = fourPSort(reconstructRect(points))
    if len(points)==4 and is_sorted:
        aspRec = euclideanDist(sorted[0],sorted[1])/euclideanDist(sorted[0],sorted[3]);
    else:
        aspRec = abs(max-mix)/abs(may-miy)
    return aspRec


def reconstructRect(contour):
    if len(contour)==2:
        win = [[[contour[0][0][0], contour[0][0][1]]],
              [[contour[0][0][0], contour[1][0][1]]],
              [[contour[1][0][0], contour[1][0][1]]],
              [[contour[1][0][0], contour[0][0][1]]]]
        win = np.array(win)
        return win
    elif len(contour)==3:
        diff = -1
        for i in range(3):
            for j in range(3):
                if i==j: continue
                if diff<(abs(contour[i][0][0]-contour[j][0][0])+abs(contour[i][0][1]-contour[j][0][1])):
                    diff = abs(contour[i][0][0]-contour[j][0][0])+abs(contour[i][0][1]-contour[j][0][1])
                    diam1_1 = [[contour[i][0][0], contour[i][0][1]]]
                    diam1_2 = [[contour[j][0][0], contour[j][0][1]]]
        for k in range(3):
            di = [[contour[k][0][0], contour[k][0][1]]]
            if di!=diam1_1 and di!=diam1_2:
                diam2_1 = di
        print(diam1_1)
        print(diam1_2)
        print(diam2_1)
        diam2_2 = [[diam1_2[0][i] + diam1_1[0][i] - diam2_1[0][i] for i in range(2)]]
        win = [diam1_1,diam1_2,diam2_1,diam2_2]
        win = np.array(win)
        return win
    elif len(contour)==4:
        return contour
    else:
        p1, p2, p3, p4 = [], [],[],[]
        min_xpy=1e6
        max_xpy=-1
        min_xmy=1e6
        max_xmy=-1e6
        for cnt in contour:
            xpy = cnt[0][0] + cnt[0][1]
            xmy = cnt[0][0] - cnt[0][1]
            if min_xpy>=xpy:
                min_xpy = xpy
                p1 = cnt
            if min_xmy>=xmy:
                min_xmy = xmy
                p2 = cnt
            if max_xpy<=xpy:
                max_xpy = xpy
                p3 = cnt
            if max_xmy<=xmy:
                max_xmy = xmy
                p4 = cnt
        win = [p1,p2,p3,p4]
        win = np.array(win)
        return win

def contourManagement(polies, img):
    global iter, shapeAR, tempArea, tempvecy, tempvecz, oldP, long_distance, eucFilterIt, enteranceArea, enterance, flag, vecy, vecz
    rows, cols, _ = img.shape
    polyInfo = []
    in_fours = True
    goodIndex = ind = -1
    eucFIt = 0
    win = []
    enteranceArea = 2*img.size/5

    picChord = math.sqrt((cols*cols)+(rows*rows))
    drawing = img.copy()
    is_it_the_first = (iter==0)

    print("iter:\t", iter)
    print("oldP", oldP)

    for i, poly in enumerate(polies):
        ar = arCalculate(poly, img)
        if len(poly)==2: area = abs(poly[0][0][0]-poly[1][0][0])*abs(poly[0][0][1]-poly[1][0][1])
        elif len(poly)==3: area = 2*cv.contourArea(poly);
        else: area = cv.contourArea(poly)
        case_y, case_z = rectangleGeometric(poly, img)
        centerDist = euclideanDist(oldP, [[case_y,case_z]])
        arDiff = abs(ar-shapeAR)
        polyScore = abs(area-tempArea)/tempArea + (2*centerDist/picChord) + (arDiff/shapeAR)
        polyInfo_case = [i, polyScore, arDiff, len(poly), area, ar, abs(area-tempArea)/tempArea, (2*centerDist/picChord), arDiff/shapeAR, centerDist, case_y, case_z]
        polyInfo_op = [i, 1000, 1000, 1, 0, 1000, 0,0,0,1000,1000, 1000]
        if(len(poly)==1): polyInfo.append(polyInfo_op)
        else: polyInfo.append(polyInfo_case)

    m = len(polyInfo)
    polyInfo.sort(key=lambda x: x[1])
    print("polyInfo size:  ", len(polyInfo))
    print("sorted polies:")

    for p in polyInfo:
        if p[2]>100: continue
        print(p)

    the_close_angle_case = (polyInfo[0][2]>0.8)

    print("area data:   before:", tempArea)

    i = 0
    while i<m :
        is_it_4p = (polyInfo[i][3]==4)
        if (not is_it_4p) and in_fours:
            if i==m-1:
                in_fours = False
                i = 0
                continue
            else:
                i = i+1
                continue

        if tempArea >= enteranceArea/3: maxAreaDiff = (3.5*tempArea)/10
        elif tempArea >= enteranceArea/9: maxAreaDiff = (2.3*tempArea)/10
        elif long_distance: maxAreaDiff = (4*tempArea)/10
        else: maxAreaDiff = (1.8*tempArea)/10

        areaDiff = abs(polyInfo[i][4]-tempArea)
        print("areaDiff", areaDiff)

        is_the_ca_const = (polyInfo[i][9]<(picChord/3))
        is_the_area_const = areaDiff<maxAreaDiff
        is_it_close_enough = (tempArea>=1e4)and(tempArea<enteranceArea)
        is_it_the_full_frame = polyInfo[i][4]>(img.size-1e4)
        if the_close_angle_case: is_the_ar_ok = polyInfo[i][2]<1.5
        else: is_the_ar_ok = polyInfo[i][2]<0.8

        if in_fours: print("filters report 4p:   ", is_it_the_first, is_the_ca_const, is_it_4p, is_the_ar_ok, is_the_area_const, is_it_close_enough, is_it_the_full_frame)
        else:  print("filters report none 4p:   ", is_it_the_first, is_the_ca_const, is_it_4p, is_the_ar_ok, is_the_area_const, is_it_close_enough, is_it_the_full_frame)

        if (is_the_area_const or is_it_close_enough) and (not is_it_the_full_frame) and (is_it_4p==in_fours) and is_the_ca_const and is_the_ar_ok:
            goodIndex = polyInfo[i][0]
            ind = i
            if in_fours: print("---good 4p poly info:   ", polyInfo[ind])
            else: print("---good none 4p poly info:   ", polyInfo[ind])
            print("area data:    before:", tempArea, "   new:   ", polyInfo[ind][4])
            win = polies[goodIndex]
            break

        if is_it_4p and i==m-1 and in_fours:
            in_fours = False
            i = 0
            continue
        i = i+1

    if not is_the_ca_const:
        eucFIt = eucFIt + 1
        if goodIndex<m-1 : goodIndex = goodIndex + 1
    else: eucFIt = 0
    if (goodIndex==-1) or (polyInfo[ind][2]>100): return drawing, [];
    print("the goodIndex:   ", goodIndex)

    if (polyInfo[ind][3]==4 and polyInfo[ind][2]<100) or (polyInfo[ind][3]==2 and polyInfo[ind][4]<400) or (is_the_area_const or is_it_the_first or is_it_close_enough):
        print("entered")

        if (polyInfo[ind][3]<4 and polyInfo[ind][4]<(img.size/500)) or (polyInfo[ind][3]==4 and polyInfo[ind][4]<(img.size/400)):
            long_distance = True;
        else: long_distance = False;
        print("long_distance", long_distance)

        vecy, vecz = rectangleGeometric(polies[goodIndex], img)
        newP =[[vecy,vecz]]
        euc = euclideanDist(oldP, newP)
        print("iter:\t", iter, "\tdata before:\t", tempvecy, tempvecz, "\tnew data:\t", vecy, vecz, "\teuc:\t", euc)
        if euc>(cols/5):
            if not (euc<(0.5*tempvecy)) or (eucFilterIt>50):
                eucFilterIt = eucFilterIt + 1
                print("eucFilterIt\t:\t",eucFilterIt)
                return drawing, [];
        else:
            tempvecy = vecy
            tempvecz = vecz
            eucFilterIt = 0
        flag = True
        if polyInfo[ind][4]>(2*enteranceArea/3):
            print("enter!!")
            enterance = True
        tempArea = polyInfo[ind][4]
        shapeAR = polyInfo[ind][5]

        cv.drawContours(drawing, polies, goodIndex, (0,255,0), 2)
        for point in win:
            # point = [[x,y]]
            xp, yp = point[0][0], point[0][1]
            center = (xp,yp)
            cv.circle(drawing, center, 10, (0,0,0), 3)
        iter = iter + 1
    return drawing, win;

def perception3D(img, win):
    global real_rect_info, translation_vec, rotation_vec
    axis_3d = np.float32([[0, 0, 0], [0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]])
    is_sorted, rect = fourPSort(reconstructRect(win))
    if not is_sorted: return img
    found_rect_info = np.float32([rect[0][0], rect[1][0], rect[2][0], rect[3][0]])
    pic = img.copy()
    _, rotation_vec, translation_vec = cv.solvePnP(real_rect_info, found_rect_info, camera_matrix, distortion_matrix)
    axis_2d, j = cv.projectPoints(axis_3d, rotation_vec, translation_vec, camera_matrix, distortion_matrix)
    # print("a2d", axis_2d)
    start = (axis_2d[0][0][0], axis_2d[0][0][1])
    # print("start:  ", start)
    cv.line(pic, start, (axis_2d[1][0][0],axis_2d[1][0][1]), (0,255,255), 1)
    cv.line(pic, start, (axis_2d[2][0][0],axis_2d[2][0][1]), (255,0,255), 1)
    cv.line(pic, start, (axis_2d[3][0][0],axis_2d[3][0][1]), (255,255,0), 1)
    return pic


def windowDetection(imin):
    print("\n~~~~~\nWD is called\n")
    imin_ = imin.copy()
    imout = preProcessing(imin)
    contours, poly = contourExtraction(imout, imin_)
    drawing, window = contourManagement(contours, imin)
    result = perception3D(drawing, window)
    cv.imshow("window detection result",result)
    cv.waitKey(30)
    print("\n~~~~~\nWD is out\n")
    return imout

def rectangleGeometric(points, pic):
    max = may = dx = xc = dy = yc = 0
    rows,cols,_ = pic.shape
    xpc = cols/2 - 1
    ypc = rows/2 - 1
    mix = miy = 1e6
    for point in points:
        if max<point[0][0]: max = point[0][0]
        if may<point[0][1]: may = point[0][1]
        if mix>point[0][0]: mix = point[0][0]
        if miy>point[0][1]: miy = point[0][1]
    xc = (max+mix)/2 + 1;
    yc = (may+miy)/2 + 1;
    dx = xc - xpc;
    dy = yc - ypc;
    return dx, dy;

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/quadrotor_1/front/image_raw",Image,self.imageCallback)
    # self.image_sub = rospy.Subscriber("/image_raw",Image,self.imageCallback)

  def imageCallback(self,data):
    global cv_image, is_set
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    print("Iteration Begin\n\n\n")
    frame = cv_image.copy()

    if is_set == False:
        print("is_set",is_set)
        setWindow(frame)

    else:
        print("is_set",is_set)
        frame = windowDetection(cv_image)
    print("flag", flag)
    if flag:
        print("\n\nimpro published data:::\nmsg.y:",vecy,"\tmsg.z:\t",vecz)
        print("translation_vec: ",translation_vec)
        print("rotation_vec: ",rotation_vec)
    else:
        print("nothing published\n")
    print("Iteration end\n---------------------------------------------------------------------------------\n")



def main(args):

  print("Node Started\n")
  ic = image_converter()
  # ic = window_detection()
  pub = rospy.Publisher('chatter', String, queue_size=10)
  rospy.init_node('visual_info', anonymous=True)

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
