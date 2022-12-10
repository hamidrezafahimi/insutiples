


### 1. Install the Ground Station App: QGround

This is for ubuntu. For other platforms, refer to the main [reference](https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html).


1. Before installing QGroundControl for the first time. On the command prompt enter:

```
    sudo usermod -a -G dialout $USER
    sudo apt-get remove modemmanager -y
    sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y
    sudo apt install libqt5gui5 -y
    sudo apt install libfuse2 -y
```

2. Logout and login again to enable the change to user permissions.

3. To install QGroundControl, first, Download QGroundControl.AppImage.

4. Then:

```
chmod +x ./QGroundControl.AppImage

./QGroundControl.AppImage  (or double click)
```

### Connect Pixhawk to QGround

Connect the board to the USB port

```
sudo chmod 666 /dev/tty<hit-tab>
```

Doing this, oprning the QGround:

```
./QGroundControl.AppImage
```

The app identifies tghe board. 


