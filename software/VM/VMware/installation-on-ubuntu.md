
This is the installation guide to install VMware on ubuntu. I did the installation on ubuntu 20.04. 


1. First, download the '.bundle' file of VMware Pro. I did it from [this link](https://soft98.ir/os/virtual-machine/1232-vmware-workstation.html).

2. In the folder in which the file is downloaded, right click on the file. Click on 'Properties'. Go to the 'permissions' tab. Check the option: 'Allow executing file as a program'.

3. Open a terminal in the folder in which the file is downloaded. Do the followings:

```
sudo ./<name-of-the-downloaded-file>.bundle
# mine was: sudo ./VMware-Workstation-Full-16.2.3-19376536.x86_64.bundle
```

This will install the VMware setup. 

4. To open the VMware setup, you might face a problem about GCC compiler not being installed. Do the followings to avoid the problem:

```
sudo apt-get update

sudo apt-get install build-essential
```

5. Then, go to the start menu. Search for the VMware Pro. Click on it. An installation setup window opens. Click on 'install'. At this step, you might face an error installing 'vmmon' and 'vmnet'. If you faced such problem, do the followings:

* *NOTE:* The followings are based on your version of VMware. Notice the version in command-line. Mine was 16.2.3. 

```
wget https://github.com/mkubecek/vmware-host-modules/archive/workstation-16.2.3.tar.gz

tar -xzf workstation-16.2.3.tar.gz

cd vmware-host-modules-workstation-16.2.3/

tar -cf vmmon.tar vmmon-only

tar -cf vmnet.tar vmnet-only

sudo cp -v vmmon.tar vmnet.tar /usr/lib/vmware/modules/source/

sudo vmware-modconfig --console --install-all
```

This probably solves your problem. By the way, I found it [here](https://ubuntu-mate.community/t/20-04-vmware-workstation-player-fails-to-build-kernel-modules-vmmon-vmnet/21176)

6. Then, you'll be able to open the VMware Pro installation setup from the start menu. Follow a next-next scheme and you'll get to a step in which you must enter a licence key or choose to you the product for just 30 days. Thanks to living in Iran, I managed to get some installation keys. Here they are:

ZF3R0-FHED2-M80TY-8QYGC-NPKYF
YF390-0HF8P-M81RQ-2DXQE-M2UT6
ZF71R-DMX85-08DQY-8YMNC-PPHV8
UV3TU-4AGD0-080WP-PPPNC-WARUA
YA7RA-F6Y46-H889Z-LZMXZ-WF8UA
ZV7HR-4YX17-M80EP-JDMQG-PF0RF
UZ70R-FTG0M-08DJQ-EWZZ9-XF2RF
UC3XK-8DD1J-089NP-MYPXT-QGU80
GY3RH-42X10-M8E0Q-FXNZT-XARC2

Enter the keys and you'll be fine finishing your installation. Enjoy you VMware. 

