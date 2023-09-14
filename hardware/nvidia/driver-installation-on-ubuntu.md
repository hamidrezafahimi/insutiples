




### GUI Approach

After installing your ubuntu OS, go to the 'Software & Updates'. Go to the 'Additional Drivers' tab. There, set the latest stable version for your graphic driver (Hit on the one in the list with the upper version and the characteristics: proprietary, tested). If it's not currently set, then it'll start 'Applying changes ...' which takes a while.



### Terminal Approach

Get a list of your available drivers:

```
ubuntu-drivers devices
```
Remember < the-one > with the 'recommended' term in front of it. Then:

```
sudo apt install <the-one>

sudo reboot
```

