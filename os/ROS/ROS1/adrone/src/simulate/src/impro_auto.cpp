#include <ros/ros.h>
#include <image_transport/image_transport.h>   //includes everything we need to publish and subscribe to images.
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include "opencv2/videoio.hpp"
#include "opencv2/opencv.hpp"
#include <cv_bridge/cv_bridge.h>
#include "simulate/imtodyn.h"
#include "simulate/dyntoim.h"
#include <algorithm>
using namespace cv;
using namespace std;

const int max_canny1 = 800;
const int max_canny2 = 800;
const int max_GuKernelSize = 50;
const float shapeAR = 1.5;
const String window_capture_name = "Video Capture";
const int max_value_H = 360/2;
const int max_value = 255;
int low_H = 15, low_S = 174, low_V = 0;
int high_H = 23, high_S = 255, high_V = 255;
int canny1 = 131, canny2 = 0, GuKernelSize = 7;
int ity=0, itz=0;
float GuSigma = 1.2, euc = 0;
int vecy, vecz, tempvecy, tempvecz, tempArea, iter=0, eucFilterIt=0, eucFIt=0, areaIt=0;
bool lost = false;
bool flag = false, msgFlag = false, long_distance = false, enterance = false;
Point oldP, newP;

Mat camera_matrix = (Mat_<double>(3,3) << 376.744103, 0.000000, 319.513089, 0.000000, 376.572581, 178.056011, 0.000000, 0.000000, 1.000000);
Mat distortion_matrix = (Mat_<double>(5,1) << -0.000545, 0.000835, -0.000038, -0.000143, 0.000000);
vector<Point3d> real_rect_info{Point3d(0,0,0), Point3d(1.5,0,0), Point3d(1.5,1,0), Point3d(0,1,0)};
vector<Point2d> found_rect_info;
Mat rotation_vec, translation_vec;

static void on_canny1_trackbar(int, void *)
{
    // low_H = min(high_H-1, low_H);
    setTrackbarPos("canny1", window_capture_name, canny1);
}
static void on_canny2_trackbar(int, void *)
{
    // low_H = min(high_H-1, low_H);
    setTrackbarPos("canny1", window_capture_name, canny1);
}
static void on_GuKernelSize_trackbar(int, void *)
{
    if(GuKernelSize%2 == 0) GuKernelSize += 1;
    setTrackbarPos("GuKernelSize", window_capture_name, GuKernelSize);
}
static void on_low_H_thresh_trackbar(int, void *)
{
    low_H = min(high_H-1, low_H);
    setTrackbarPos("Low H", window_capture_name, low_H);
}
static void on_high_H_thresh_trackbar(int, void *)
{
    high_H = max(high_H, low_H+1);
    setTrackbarPos("High H", window_capture_name, high_H);
}
static void on_low_S_thresh_trackbar(int, void *)
{
    low_S = min(high_S-1, low_S);
    setTrackbarPos("Low S", window_capture_name, low_S);
}
static void on_high_S_thresh_trackbar(int, void *)
{
    high_S = max(high_S, low_S+1);
    setTrackbarPos("High S", window_capture_name, high_S);
}
static void on_low_V_thresh_trackbar(int, void *)
{
    low_V = min(high_V-1, low_V);
    setTrackbarPos("Low V", window_capture_name, low_V);
}
static void on_high_V_thresh_trackbar(int, void *)
{
    high_V = max(high_V, low_V+1);
    setTrackbarPos("High V", window_capture_name, high_V);
}

float arCalculate(vector<Point>, Mat);
float euclideanDist(Point, Point);
Mat imageProcessing(Mat);
void rectangleGeometric(vector<Point>,  Mat, int&, int&);
Mat preProcessing(Mat);
vector<vector<Point>> contourExtraction(Mat, Mat&);
Mat contourManagement(  vector<vector<Point>>, Mat, vector<Point>&);
bool detectionSafetyCheck(vector<int>& ,const int, const int, const bool, const bool, int&);
void shiftVector(vector<int>&, int);
float vectorAverage(vector<int>);
float vectorSD(vector<int>);
bool sortcol( const vector<float>&, const vector<float>&);
bool fourPSort (vector<Point>, vector<Point2d>&);
vector<Point> reconstructRect(vector<Point>&);
Mat perception3D(Mat, vector<Point>);

void imageCallback(const sensor_msgs::ImageConstPtr& msg)    //will get called when a new image has arrived on the
{      //"camera/image" topic. Although the image may have been sent in some arbitrary transport-specific message type,
  cout<<"Iteration Begin\n\n\n";
  msgFlag = true;
  try  // notice that the callback need only handle the normal sensor_msgs/Image type. All image encoding/decoding is
  {    //handled automagically
    // cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);  //We convert the ROS image message to an OpenCV image
                                                                      //with BGR pixel encoding, then show it in a display window.
    Mat frame, frm, img = cv_bridge::toCvShare(msg, "bgr8")->image;
    // imshow("token pic", img);
    frm = img.clone();
    frame = imageProcessing(frm);
    cout<<"flag:\t"<<flag<<endl;
    // imshow("processed pic", frame);
    cv::waitKey(30);
  }
  catch (cv_bridge::Exception& e)
  {
    ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
  }
}

void dynCallback(const simulate::dyntoim msg)
{
  lost = msg.lost;
  cout<<"dyncon published data\tlost:"<<lost<<endl;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "impro");
  ros::NodeHandle nh;
  // cv::namedWindow("view");
  cv::startWindowThread();
  image_transport::ImageTransport it(nh);
  ros::Subscriber dynSub = nh.subscribe("dynamic_feedback", 1, dynCallback);
  image_transport::Subscriber sub = it.subscribe("/quadrotor_1/front/image_raw", 1, imageCallback);
  ros::Publisher pubinfo = nh.advertise<simulate::imtodyn>("visual_info", 10);
  ros::Rate loop_rate(10); // Loop at 10Hz
  simulate::imtodyn msg;

  bool safety_check_z = true, safety_check_y = true, has_detected = false;
  int count=0, pubCount=0;
  vector<int> yBuffer, zBuffer;
  while (ros::ok())
  {
    if(count == 0) cout<<"Node Started\n";

    if(flag) {pubCount++;
      has_detected = true;
    }
    else has_detected = false;

    cout<<"flag:   "<<flag<<endl;
    cout<<"has_detected:   "<<has_detected<<endl;

    cout<<"\npubCount:\t\t"<<pubCount<<endl;

    if(flag /*&& safety_check_y && safety_check_z*/){
      msg.y = vecy;
      msg.z = vecz;
      msg.enterance = enterance;
      cout<<"\n\nimpro published data:::\nmsg.y:"<<msg.y<<"\tmsg.z:\t"<<msg.z<<endl;
      cout<<"translation_vec: "<<translation_vec.at<double>(0) << " " << translation_vec.at<double>(1) << " " << translation_vec.at<double>(2) <<endl;
      cout<<"rotation_vec: "<<rotation_vec.at<double>(0) << " " << rotation_vec.at<double>(1) << " " << rotation_vec.at<double>(2) <<endl;
      pubinfo.publish(msg);
      flag = false;
    }
    else {
      // if(!(safety_check_y && safety_check_z)) cout<<"Not so safe!\n"<<"data might be wrong\tmsg.y:\t"<<vecy<<"\tmsg.z:\t"<<vecz<<endl;
      cout<<"nothing published\n";
      // safety_check_y = true;
      // safety_check_z = true;
    }
    cout<<"\n\n\nIteration End\n-----------------------------------------------------------------------\n";
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
    msgFlag = false;
  }
  return 0;
}


Mat imageProcessing(Mat imin){

  cout<<"\n~~~~~\nIP is called\n";

   Mat imin_, imout, drawing, result;
   vector<vector<Point> > contours, poly;
   vector<Point> window;

   imin_ = imin.clone();

   imout = preProcessing(imin);

   contours = contourExtraction(imout, imin_);

   drawing = contourManagement(contours, imin, window);

   result = perception3D(drawing, window);

   imshow("processed pic", imin_);
   imshow("window", result);
   cout<<"\nIP is out\n~~~~~\n";
   return result;
}

Mat preProcessing(Mat imin){
  // namedWindow(window_capture_name);
  // createTrackbar("canny1", window_capture_name, &canny1, max_canny1, on_canny1_trackbar);
  // createTrackbar("canny2", window_capture_name, &canny2, max_canny2, on_canny2_trackbar);
  // createTrackbar("GuKernelSize", window_capture_name, &GuKernelSize, max_GuKernelSize, on_GuKernelSize_trackbar);
  // createTrackbar("Low H", window_capture_name, &low_H, max_value_H, on_low_H_thresh_trackbar);
  // createTrackbar("High H", window_capture_name, &high_H, max_value_H, on_high_H_thresh_trackbar);
  // createTrackbar("Low S", window_capture_name, &low_S, max_value, on_low_S_thresh_trackbar);
  // createTrackbar("High S", window_capture_name, &high_S, max_value, on_high_S_thresh_trackbar);
  // createTrackbar("Low V", window_capture_name, &low_V, max_value, on_low_V_thresh_trackbar);
  // createTrackbar("High V", window_capture_name, &high_V, max_value, on_high_V_thresh_trackbar);

  Mat out, imin_hsv;
  // int erosion_size = 3;
  // Mat element = getStructuringElement( MORPH_RECT,
  //                                     Size( 2*erosion_size + 1, 2*erosion_size+1 ),
  //                                     Point( erosion_size, erosion_size ) );

  // GaussianBlur(imin, imin, Size(GuKernelSize,GuKernelSize), 1.2);
  cvtColor(imin, imin_hsv, COLOR_BGR2HSV);
  inRange(imin_hsv, Scalar(low_H, low_S, low_V), Scalar(high_H, high_S, high_V), out);
  // Canny(imin, out, canny1, canny2, 3);
  // dilate( out, out, element );
  // GaussianBlur(out, out, Size(7,7), 1.2);
  bitwise_not(out, out);
  // imshow(window_capture_name, out);
  // erode(out, out, element );
  return out;
}

vector<vector<Point>> contourExtraction(Mat img, Mat &img0){
  vector<vector<Point> > contours, polies, windows;
  vector<Vec4i> hierarchy;
  vector<Point> conto;

  findContours( img, contours, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_TC89_KCOS, Point(0, 0) );
  for( float i = 0; i< contours.size(); i++ ){
    approxPolyDP(Mat(contours[i]), conto, 13, true);
    polies.push_back(conto);
    windows.push_back(reconstructRect(conto));
    drawContours( img0, windows, i, Scalar(0,0,255), 2, 8);
  }
  cout<<"num of contours: \t"<<contours.size()<<endl;

  return polies;
}

Mat contourManagement(  vector<vector<Point>> poly, Mat img, vector<Point> &res){
  Mat drawing;
  vector<Point> conto;
  vector<vector<float> > polyInfo;
  float ar, maxAreaDiff, changeFactor, areaDiff, area,  picChord, polyScore, centerDist, arDiff, caseEuc;
  int goodIndex=-1, ind=0, case_z, case_y; // = (img.total()/450);
  bool four_found = false, is_it_4p, is_the_ar_ok, is_the_area_const, is_it_the_first,
       is_it_close_enough, is_it_almost_here, is_the_ca_const, is_it_the_full_frame,
       the_close_angle_case, in_fours=true, gab=true;
  int enteranceArea = 2*img.total()/5;

  cout<<"iter:\t"<<iter<<endl;

  picChord = sqrt((img.cols*img.cols) + (img.rows*img.rows));

  // if(lost) iter = 0;
  is_it_the_first = (iter==0);
  drawing = img.clone();

  // cout<<"max area diff:\t\t"<<maxAreaDiff<<endl;
  cout<<"\noldP: \t"<<oldP<<endl;;

  for( float i = 0; i< poly.size(); i++ ){
    conto = poly[i];
    ar = arCalculate(conto, img);
    if(conto.size()==2) area = abs(conto[0].x-conto[1].x)*abs(conto[0].y-conto[1].y);
    else if(conto.size()==3) area = 2*contourArea(conto);
    else area = contourArea(conto);
    rectangleGeometric(conto, drawing, case_y, case_z);
    if(is_it_the_first) oldP = Point(case_y,case_z);
    centerDist = euclideanDist(oldP, Point(case_y,case_z));
    arDiff = abs(ar-shapeAR);

    if(iter==0) polyScore = arDiff;
    else{
      polyScore = abs(area-tempArea)/tempArea + (2*centerDist/picChord) + (arDiff/shapeAR);
    }

    // if(iter==0)
    if(conto.size()==1) polyInfo.push_back({i, 1000, 1000, 1, 0, 1000, 0,0,0,1000,1000});
    else polyInfo.push_back({i, polyScore, arDiff, float(conto.size()), area, ar,
                            abs(area-tempArea)/tempArea, (2*centerDist/picChord),
                            float(0.5*arDiff/shapeAR), centerDist, float(case_y), float(case_z)});
  }
  int m = polyInfo.size();
  int n = polyInfo[0].size();
  // cout<<"unsorted polies:\n";
  // for (int i=0; i<m; i++)
  // {
  //     for (int j=0; j<n ;j++)
  //         cout << polyInfo[i][j] << " ";
  //     cout << endl;
  // }
  sort(polyInfo.begin(), polyInfo.end(),sortcol);
  cout<<"sorted polies:\n";

  for (int i=0; (i<m)&&(polyInfo[i][2]<100); i++)
  {

      for (int j=0; j<n ;j++)
          cout << polyInfo[i][j] << ",";
      cout /*<<polyInfo[i][4]*/<< endl;
  }

  the_close_angle_case = (polyInfo[0][2]>0.8);

  cout<<"area data:   before:\t"<< tempArea<<endl;

  for(int i=0; i<poly.size(); ++i){

    if(iter==0) {tempArea = polyInfo[i][4];
      // goodIndex = 0;
    }

    is_it_4p = (polyInfo[i][3]==4)/*||is_it_close_enough*/;
    if(!is_it_4p && in_fours) {
      if((i==polyInfo.size()-1)) {
        in_fours = false;
        i = -1;
        continue;
        }
      else continue;
    }

    if(tempArea >= enteranceArea/3) maxAreaDiff = (35*tempArea)/10;
    else if(tempArea >= enteranceArea/9) maxAreaDiff = (2.3*tempArea)/10;
    else if(long_distance) maxAreaDiff = (3.5*tempArea)/10;
    else maxAreaDiff = (1.8*tempArea)/10;

    areaDiff = abs(polyInfo[i][4]-tempArea);
    cout<<"areaDiff:\t"<<areaDiff<<endl;

    is_the_ca_const = (polyInfo[i][9]<(picChord/3)) || (iter<10);
    is_the_area_const = areaDiff<maxAreaDiff;/*||(areaIt>100);*/
    is_it_close_enough = (tempArea>=1e4)&&(tempArea<enteranceArea);
    is_it_the_full_frame = polyInfo[i][4]>(img.total()-1e4);
    if(the_close_angle_case) is_the_ar_ok = polyInfo[i][2]<1.5;
    else is_the_ar_ok = (polyInfo[i][2]<0.8);

    if(in_fours) cout<<"filters report 4p\t:\t";
    else cout<<"filters report n4p\t:\t";
    cout<<is_it_the_first <<"  " << is_the_ca_const<<"  "<<is_it_4p <<"  "<< is_the_ar_ok
        <<"  "<< is_the_area_const<<"  "<<is_it_close_enough <<"  "<< is_it_the_full_frame<<"  "<<endl;

    if((is_the_area_const|| is_it_the_first || is_it_close_enough)&& !is_it_the_full_frame
       && (is_it_4p == in_fours) && is_the_ca_const && is_the_ar_ok) {
         goodIndex = polyInfo[i][0];
         ind = i;
         if(in_fours) cout<<"---good 4p poly info:\t";
         else cout<<"---good none 4p poly info:\t";
         for(int k=0; k<polyInfo[ind].size(); ++k) cout<<polyInfo[ind][k]<<'\t';
         cout<<endl;
         cout<<"area data:   before:\t"<< tempArea<<"\tnew:\t"<<polyInfo[i][4] <<endl;
         four_found = true;
         break;
    }

    if(is_it_4p && i==polyInfo.size()-1 && in_fours){
      in_fours = false;
      i = -1;
      continue;
    }

  }

 if(!is_the_ca_const){
    eucFIt++;
    if(goodIndex<poly.size()-1) goodIndex++;
 }
 else eucFIt = 0;

 if(goodIndex==-1 || polyInfo[ind][2]>=100) return drawing;

 cout<<"the goodIndex:\t"<<goodIndex<<endl;

 // ostringstream name;
 // name << "im_" << iter << ".jpg";

  if((poly[goodIndex].size()==4 && polyInfo[ind][2]<100)||
     (poly[goodIndex].size()==2 && polyInfo[ind][4]<400)||
     (is_the_area_const || is_it_the_first || is_it_close_enough)){

       cout<<"entered\n";

    if((poly[goodIndex].size()<4 && polyInfo[ind][4]<(img.total()/500)) ||
      (poly[goodIndex].size()==4 && polyInfo[ind][4]<(img.total()/400)))
      long_distance = true;
    else long_distance = false;

    cout<<"long_distance:\t\t"<<long_distance<<endl;

    rectangleGeometric(poly[goodIndex] ,drawing, vecy, vecz);

    if(iter==0){
    tempvecy = vecy;
    tempvecz = vecz;
    }

    oldP = Point(tempvecy,tempvecz);
    newP = Point(vecy,vecz);
    euc = euclideanDist(oldP,newP);
    cout<<"iter:\t"<<iter<<"\tdata before:\t"<<tempvecy<<'\t'<<tempvecz<<'\t'<<"new data:\t"<<vecy<<'\t'<<vecz<<'\t'<<"euc:  "<<euc<<endl;

    // if(euc>img.cols/5) return drawing;
    // if(euc>img.cols/10) {
    if((euc>img.cols/5)){
      if((euc<(0.5*tempvecy)) || (eucFilterIt>50)) goto lab;
      eucFilterIt++;
      cout<<"eucFilterIt\t:\t"<<eucFilterIt<<endl;
      return drawing;
    }
    else {
      lab:
      tempvecy = vecy;
      tempvecz = vecz;
      eucFilterIt = 0;
    }

    flag = true;
    if(polyInfo[ind][4]>(2*enteranceArea/3)) {
      cout<<"enter!!\n";
      enterance = true;
    }

    if(polyInfo[ind][3]==2) tempArea = abs(poly[goodIndex][0].x-poly[goodIndex][1].x)*abs(poly[goodIndex][0].y-poly[goodIndex][1].y);
    else if(polyInfo[ind][3]==3) {tempArea = polyInfo[ind][4];/* imwrite(name.str(),img);*/}
    else tempArea = polyInfo[ind][4];

    drawContours( drawing, poly, goodIndex, Scalar(0,255,0), 2, 8);
    for (int k=0; k<poly[goodIndex].size(); ++k){
      circle(drawing, poly[goodIndex][k], 10, Scalar(0,0,0), 3);
    }
    res = poly[goodIndex];

    ++iter;
  }

  return drawing;
}

Mat perception3D(Mat img, vector<Point> win){
  vector<Point> rect;
  vector<Point2d> axis_2d;
  vector<Point3d> axis_3d{Point3d(0,0,0), Point3d(0.5,0,0), Point3d(0,0.5,0), Point3d(0,0,0.5)};
  Mat pic = img.clone();
  rect = reconstructRect(win);
  if(!fourPSort(rect, found_rect_info)) return img;

  solvePnP(real_rect_info, found_rect_info, camera_matrix, distortion_matrix, rotation_vec, translation_vec);
  projectPoints(axis_3d, rotation_vec, translation_vec, camera_matrix, distortion_matrix, axis_2d);

  for(int i=0; i<axis_2d.size(); ++i){
    line(pic, axis_2d[0], axis_2d[1], Scalar(0,255,255), 1, CV_AA);
    line(pic, axis_2d[0], axis_2d[2], Scalar(255,0,255), 1, CV_AA);
    line(pic, axis_2d[0], axis_2d[3], Scalar(255,255,0), 1, CV_AA);
  }
  return pic;
}

vector<Point> reconstructRect(vector<Point> &contour){
  if(contour.size()==2){
    return {contour[0], Point(contour[0].x, contour[1].y), contour[1], Point(contour[1].x, contour[0].y)};
  }
  else if(contour.size()==3){
    Point diam1_1, diam1_2, diam2_1, diam2_2;
    int diff = -1;;
    for(int i=0; i<3; ++i){
      cout<<"  "<<contour[i];
      for(int j=0; j<3; ++j){
        if(i==j) continue;
        // diff = abs(contour[i].x-contour[j].x)+abs(contour[i].y-contour[j].y);
        if(diff<abs(contour[i].x-contour[j].x)+abs(contour[i].y-contour[j].y)){
          diff = abs(contour[i].x-contour[j].x)+abs(contour[i].y-contour[j].y);
          // rect.clear();
          diam1_1 = contour[i];
          diam1_2 = contour[j];
        }
      }
    }
    for(int i=0; i<3; ++i){
    if(contour[i]!=diam1_1 && contour[i]!=diam1_2) diam2_1 = contour[i];
    }
    diam2_2 = diam1_2 + diam1_1 - diam2_1;
    cout<<'\n'<<diam1_1<<'\t'<<diam1_2<<'\t'<<diam2_1<<'\t'<<diam2_2<<endl;
    return {diam1_1,diam1_2,diam2_1,diam2_2};
  }
  else if(contour.size()==4){
    return contour;
  }
  else {
    Point p1, p2,p3,p4;
    int xpy, xmy, min_xpy=1e6, max_xpy=-1, min_xmy=1e6, max_xmy=-1;
    for(int i=0; i<contour.size(); ++i){
      xpy = contour[i].x+contour[i].y;
      xmy = contour[i].x-contour[i].y;
      if(min_xpy>=xpy) {min_xpy = xpy;
        p1 = contour[i];
      }
      if(min_xmy>=xmy) {
        min_xmy = xmy;
        p2 = contour[i];
      }
      if(max_xpy<=xpy) {
        max_xpy = xpy;
        p3 = contour[i];
      }
      if(max_xmy<=xmy) {
        max_xmy = xmy;
        p4 = contour[i];
      }
    }
    return {p1,p2,p3,p4};
    }
}

void rectangleGeometric(vector<Point> points, Mat pic, int& dx, int& dy){
  int xc=0, yc=0, xpc = (pic.cols/2)-1, ypc = (pic.rows/2)-1;
  unsigned int max=0, may=0, mix=10e6, miy=10e6;
  for(int i=0; i<points.size(); ++i){
    if(max<points[i].x) max = points[i].x;
    if(may<points[i].y) may = points[i].y;
    if(mix>points[i].x) mix = points[i].x;
    if(miy>points[i].y) miy = points[i].y;
  }
  xc = (max+mix)/2 + 1;
  yc = (may+miy)/2 + 1;
  dx = xc - xpc;
  dy = yc - ypc;
}

float arCalculate(vector<Point> points,  Mat pic){
  if(points.size() == 1) return 10e6;
  int borderPoints=0;
  vector<Point2d> sorted;
  // cout<<"num of pts:\t\t\t"<<points.size()<<endl;
  unsigned int max=0, may=0, mix=10e6, miy=10e6;
  Point pmax(0,0), pmay(0,0), pmix(10e6,0), pmiy(0,10e6);
  float aspRec, maxDist = -1;
  // const f;
  bool isHorizontal = false, is_sorted;

  for(int i=0; i<points.size(); ++i){
    if(max<points[i].x) max = points[i].x;
    if(may<points[i].y) may = points[i].y;
    if(mix>points[i].x) mix = points[i].x;
    if(miy>points[i].y) miy = points[i].y;
    if(abs(points[i].x-pic.cols)<5 || points[i].x<5 &&
       abs(points[i].y-pic.rows)<5 || points[i].y<5) borderPoints++ ;
  }
  if(borderPoints>=3) return 10e6;
  for(int i=0; i<points.size(); ++i){
    if(max == points[i].x && pmax==Point(0,0)) pmax = points[i];
    if(may == points[i].y && pmay==Point(0,0)) pmay = points[i];
    if(mix == points[i].x && pmix==Point(10e6,0)) pmix = points[i];
    if(miy == points[i].y && pmiy==Point(0,10e6)) pmiy = points[i];
    for(int j=0; j<points.size(); ++j){
      if(i==j) continue;
      if(maxDist<(points[i].x - points[j].x)) maxDist = points[i].x - points[j].x;
    }
  }
  // is_sorted =
  if(maxDist>(pic.cols-10)) return 10e6;

  // if(points.size()!=4){

    if(points.size()==4 && fourPSort(points, sorted)) {
      aspRec = euclideanDist(sorted[0],sorted[1])/euclideanDist(sorted[0],sorted[3]);
      }
  else{
    aspRec = float(max-mix)/float(may-miy);
    // cout<<"aspRec\t"<<aspRec<<endl;
  }
  return aspRec;
}

float euclideanDist(Point p, Point q) {
    Point diff = p - q;
    return sqrt(diff.x*diff.x + diff.y*diff.y);
}

void shiftVector(vector<int>& in, int x){
  for(int i=0; i<in.size()-1; ++i){
      // temp[i] = in[i];
      in[i] = in[i+1];
    }
  in.at(in.size()-1) = x;
  return;
}

bool sortcol( const vector<float>& v1, const vector<float>& v2 ) {
   return v1[1] < v2[1];
  }

bool fourPSort (vector<Point> cont, vector<Point2d> &res) {
    if(cont.size()==0)
    {
      cout << "empty" << endl;
      return false;
    }
    int xm=0, ym=0;
    for(int i=0; i<cont.size(); ++i){
      xm += cont[i].x;
      ym += cont[i].y;
    }
    xm /= cont.size();
    ym /= cont.size();
    vector<Point2d>  c1, c2, c3, c4;
    vector<Point2d>  t1, t2, t3, t4;

    for(int i=0; i<cont.size(); ++i){
        if((cont[i].x<=xm)&&(cont[i].y>=ym)){
          c1.push_back(cont[i]);
        }
        if((cont[i].x>xm)&&(cont[i].y>ym)){
          c2.push_back(cont[i]);
        }
        if((cont[i].x>=xm)&&(cont[i].y<=ym)){
          c3.push_back(cont[i]);
        }
        if((cont[i].x<xm)&&(cont[i].y<ym)){
          c4.push_back(cont[i]);
        }
    }

    cout << c1.size() << " " << c2.size() << " " << c3.size() << " " << c4.size() << endl;

    if(c1.size()>1){
      return false;
    }
    if(c2.size()>1){
      return false;
    }
    if(c3.size()>1){
      return false;
    }
    if(c4.size()>1){
      return false;
    }

    c1.insert(c1.end(), c2.begin(), c2.end());
    c3.insert(c3.end(), c4.begin(), c4.end());
    c1.insert(c1.end(), c3.begin(), c3.end());

    res.clear();
    res = c1;
    return true;
  }
