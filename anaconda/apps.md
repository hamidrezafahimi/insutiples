

## opencv (cv2)

First, I suggest:

```
conda install -c conda-forge ffmpeg 
```

Do:

```
conda install -c conda-forge/label/cf202003 opencv 
```

Or generally:

```
conda install -c conda-forge opencv 
```

If no success, the best way is to try with pip:

```
pip install opencv-python
```


If no success, once I made it by:

```
conda install -c anaconda opencv 
```

*Note:* It installed opencv 3.4.2 for me.



# Python

## numpy

```
conda install -c anaconda numpy 
```

## yaml

#### To import in python3:

```
conda install -c conda-forge yaml
```

Or using pip:

```
pip install pyyaml
```

#### To import in python2:

```
conda install pyyaml
```

## pandas

For me worked:

```
conda install -c "conda-forge/label/pandas_rc" pandas
```

Or using pip:

```
pip install pandas
```

# ROS

*NOTE:* For both following packages (`rospy` and `rosbag`), if you have problems installing through conda channels, this work:

```
pip install --extra-index-url https://rospypi.github.io/simple/ rospy rosbag
```

## rospy

It didn't work for me, their site says though:

```
conda install -c conda-forge ros-rospy
```

## rosbag

```
conda install -c conda-forge ros-rosbag
```

## sensor_msgs

```
conda install -c "conda-forge/label/cf202003" ros-sensor-msgs
```


## cv_bridge

This is the recommended command in the website:

```
conda install -c conda-forge ros-cv-bridge 
```

It didn't work for me, though. So I used this:

```
pip install --extra-index-url https://rospypi.github.io/simple/ cv_bridge
```