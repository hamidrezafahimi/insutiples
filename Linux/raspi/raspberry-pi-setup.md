
## Setup your raspberry pi

The followings are general descriptions needed to start-up a raspberry pi:

1. Connect power supply adapter, monitor, keyboard, and mouse to your 

#### 2. **Initial Confiruration of OS: 

In the first opened GUI do the following

Next -> (set countr and time zoney) Next -> (create user account) next -> (setup screen - don't turn the option on!) Next -> (connecting to wi-fi) choose network -> Next -> (updating softwares) skip -> ... Restart

When you see your desktop, in a new terminal:

```
sudo apt-get update

sudo apt-get upgrade
```

#### 3. Expanding filesystem:

In a terminal:

```
sudo raspi-config
# raspi is the OS distro
```
advanced options -> expand filesystem -> yes -> (go to the first page) finish -> (asks to restart) ok

#### 4. Enabling the system to be connected through wi-fi:

In a terminal:

```
sudo raspi-config
# raspi is the OS distro
```

From the first page:

- Interface Options -> SSH -> (do you want to enable?) yes

From the first page:

- Interface Options -> VNC -> (do you want to enable?) yes


To shutdown the system:

```
sudo shutdown -h now
```
