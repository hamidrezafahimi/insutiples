


## 1. Install the Ground Station App: QGround

This is for ubuntu. For other platforms, refer to the main [reference](https://docs.qgroundcontrol.com/main/en/getting_started/download_and_install.html).


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

## 2. Connect Pixhawk to QGround

This is how it looks like when the app is not connected to the board:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/main_UI/1.png?raw=true", width="600"/>
</p>

You can connect the board to the QGC in two way:

1. Connect the board directly via USB: This is recommended for the initial configuration steps. To do so, you only need a USB cable!

2. Connect the board via a telemtry link: This is required for in-flight configuration procecdures such as PID tunning. To do so, you need a telemetry receiver-transmitter module, to be connected to both board, on the drone and the Ground Station platform.

You may need to set permissions for your connected USB/Telemetry. To do so:

- Connect the board to the USB port.

- Check the ID for the connected board:

```
lsusb
```

- Give the permission to the tty ID related to the connected USB.

```
# I once did:
# sudo chmod 666 /dev/ttyACM0

# The way I did this, wassimply hitting tab like above, when the board was connected and when not. So I could figure out what is the tty ID to give the proper permission to the connected port.
```

After successful connection, open the QGround:

```
./QGroundControl.AppImage
```

When you're connected to the QGroundControl app, via USB or telemetry, the app identifies the board and it will look like the following:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/main_UI/2.png?raw=true", width="600"/>
</p>



## 3. Setup the Board

Hit on the top-left logo. On the opened menu, hit on the icon 'Vehicle Setup' and you'll enter to the 'setup' space.


### Firmware

*Note:* Before this step, go to the *Params* menu. Set the 'SYS_BL_UPDATE' to 1. This will force the system to get the proper version and boot loader for the current STM32 processor.

The 'Firmware' menu gives the utility to update the firmware on the board. 

- Enter the menu and you'll see this:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/firmware/3.png?raw=true", width="600"/>
</p>

- Disconnect board and:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/firmware/4.png?raw=true", width="600"/>
</p>

- Connect the board again. You'll see such a menu:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/firmware/2.png?raw=true", width="600"/>
</p>

- Hit 'OK' and let complete.

<!-- If the board is connected to the QGround app, the firmware will be automatically updated. -->


### Airframe

Set your airframe from the existing options. 

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/airframe/1.png?raw=true", width="600"/>
</p>


### Sensors

This is where you'll calibrate compass, gyro, accelerometer. Hit on the proper icon and follow the steps as clarified in the followings:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/sensors/1.png?raw=true", width="600"/>
</p>

Note that the compass must be calibrated in the outdoor environment.


### Radio

*NOTE:* My radio was an 'FRSky Taranis Plus' when doing this:

1. Go to the 'Radio' menu.

2. Connect the 'SBUS' or 'RCIN' port on the board to the 'SBUS' port of the radio receiver (which is mounted on the vehicle) with a typical servo connector wire. You should see the changes you make on the radio sticks on the screen.

3. To calibrate the radio, hit on the 'calibrate' icon. It warns you to zero all the trims (= inputs : including roll, pitch, yaw, throttle, and keys). There are pysical keys beside 4 main channels to zero them (= tune a parameter so that some - * --------- bar to a ----- * ----- situation and get notices by the radio that the channel () is set to zero).

4. Then, follow the steps specified in the QGround window, setting the max/mins of each of channels, and finish the calibration.


### Flight Modes

In this part, check which channels are linked to which switch on your radio. You'll be able to set flight modes (like *Stabilized*, *Manual*, etc.) for different switch positions.

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/flight_modes/1.png?raw=true", width="600"/>
</p>

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/flight_modes/2.png?raw=true", width="600"/>
</p>


### Power

Make sure that the board does not receive any external voltage except from the power module (battery). For example once I had connected the radio receiver to the board and stucked on this step.

In the following,
- Disconnect the battery
- Just hit on the 'calibrate' botton
- Connect the battery. It will calibrate and the regular sound of the motors will shot down with a small continuous sound.

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/power/1.png?raw=true", width="600"/>
</p>


### Motors

*NOTE:* This step works only if the motors are calibrated. To calibrate them, go to 'Power' tab.

This part is only for testing the motors. Set your desired throttle for all and you'll see the motors working.

*HINT:* This is the traditional order for the motors:

3 ------- 1
  \
   \
    \
     \
      \
       \
        \
2 ------- 4

Make such an order when connecting the motors to related ports on the board (named prop1, ...).
You can check if the labels for the motors are correct, setting thrust in the following bars:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/motors/1.png?raw=true", width="600"/>
</p>


### PID Tunning




### Params

Search, find and set the following parameter(s):

- Set:  COM_ARM_SWISBTN    ---->    1   based on the following:

<p align="center">
  <img src="https://github.com/hamidrezafahimi/instuctor_archive/blob/main/PIX4/QGC/pics/params/1.png?raw=true", width="600"/>
</p>

- Set: 