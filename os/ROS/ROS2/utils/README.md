Code to extract images from ros2 bagfiles. No need to ros. Better create a virtual env first (tested with python 3.8)
Setup:

```
# 
pip install rosbags
pip install rosbags-image
pip install opencv-python
```

Run:
```
python bag_to_image.py
```
You should set the parent directory containing the `.db3` file as well as topic name inside code.
