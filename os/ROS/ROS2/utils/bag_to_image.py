from pathlib import Path

from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_typestore
from rosbags.image import message_to_cvimage
import cv2 as cv

bagpath = Path('/home/hamid/w/record02112023_13')

# Create a type store to use if the bag has no message definitions.
typestore = get_typestore(Stores.ROS2_FOXY)

k = 0
# Create reader instance and open for reading.
with AnyReader([bagpath], default_typestore=typestore) as reader:
    connections = [x for x in reader.connections if x.topic == '/camera_image_gray']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)
         img = message_to_cvimage(msg)
         # In order to visualize, uncomment this part:
         cv.imshow("df", img)
         cv.waitKey(30)
         # In order to write, uncomment this part:
         cv.imwrite("/home/hamid/w/DATA/bagimgs/img%04d.jpg"%(k), img)
         print(k)
         k += 1
