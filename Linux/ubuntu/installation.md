
# Installation of ubuntu 20.04 and 22.04

The following instruction is tested and is almost the same for ubuntu 20.04 and ubuntu 22.04.

1. Make a bootable flash. 

- (in ubuntu) Use the app "startup disk creator". Set the flash memory and the .iso file separately in the two fields.

- (in windows) It's so simple. You can use a portable rufus.

* *Note:*  the partitioning format (MBR or GPT) for making the bootable flash must be set properly wrt what you're going to choose for your hard drive partitioning (e.g. select GPT if you're going to set the partitioning format on GPT)

2. Make sure that the bootable flash is connected to the usb port. Restart.

3. When the system starts. Hit 'delete' (or whatever key needed to enter BIOS menu, depending on your device), so the bios UI (boot) opens.

3. Go to the 'boot' tab.

4. Here, the boot options (priorities) are listed. Hit 'enter' on the first priority and in the pop-up menu, set the flash memory boot for it. 

* *NOTE:* If your partitioning format is GPT, then an option like 'launch CSM' must be disabled.

5. Save & exit. (The proper key must be determined in an instruction menu beside the pages. Usually: 'F10')

* *Note:* In a case that the image file is not opened after setting the priority in boot options, you can go to the last tab (save and exit), where some advanced options exist. There, you can enter the image file manually.

6. On reboot , the image file opens. You can try ubuntu or choose to install it. A typical way is to try it (in the flash memory) so you can first format your hard disk and determine your storage partitions.

7. Inside ubuntu, you can manage your hard disk partitions using the app 'Disks'. Select the hardware from the left menu. 

8. To format the disk, you should first unmount the "swap" partition (If exists - and also all of the other partitions must be unmounted). To do so, in the graphical interface, click on the partition with the "swap" name. Hit the 'square' botton on the down-left to unmount it. 

9. (In a case that you want to format your hard disk,) Hit the triple-dot botton. Select the "Format Disk". 

10. In the "Erase" field, choose the 'Quick' type (No need to feel with zeros). In the "Partitioning" field, select the 'GPT' mode or 'MBR'.

11. When the formating is finished, you can add partitions hitting the '+' botton in the down-left. Note that if a partition is already allocated, you'll need to delete that partition hitting the '-' botton so that you can create some partition(s) in that area. 

* The followings are the instructions to add partitions. The best partitioning scheme I choose for my hard drive is (left to right means from the beginning of disk space to the end):

efi (efi) - Linux (ext4) - swap (swap area) - Workspace (NTFS) - VirtualOS (NTFS)

12. Determine the size for your partition. The left space will be shown in the bottom. Hit 'Next'.

* 100 MB is enough for EFI partition

13. Determine a name for the partition and choose a proper format. Choose an 'Ext4' format for a partition in which you're going to install Linux. Choose 'NTFS' to acces data from both Linux and windows. 

* For EFI partition, you won't find an EFI format. Select 'No Filesystem'. Then, in the step 17, select the 'EFI' format for EFI partition.

14. In a disk in which you're going to intall a Linux OS, you need to create a partition with 'swap' format. If the format is not found in the pop-up menu, hit 'other' (or something like that!). You'll probably find it.

15. When you created your desired partitions, start installing ubuntu using the item in the left-menu

16. Continue the intalaltion steps like the next-next paradigm ... . Note that:

- A 'normal' and 'offline' installation is often prefered (Once, installing ubuntu 20, I figured out that an 'online' installation worked and installing offline, caused unsuccessful installation).

- In the 'installation type' step, choose 'something else'. Don't choose to erase or to install anlogside other OS's.

- Don't check the 'third party' installation option. You'll be able to install your desired graphics driver in the future.

17. When arrived to the step in which the disk partitions are listed:

- click on the partition in which you are to install ubuntu. Hit the 'change...' option. This `mount point` must be 'root' (Determined with `/`). Also, the 'Ext4' format is needed for the partition in which you're going to install ubuntu (Set in the `Use As` field). Check the 'format partition' option.

- Also, an 'EFI' partition is necessary with like 100 MB size and 'efi' format. Starting the installation, it is possible that you face an error related with non-allocating such partition. In such cases, simply add the mentioned partition in the list. To do so, select an unallocated partition and hit on the cross botton. Set 'efi' for the `Use As` field. If your partitioning type is MBR, you can wether check the options 'logical' or 'primary' and 'At the beginning of the space'. If your partitioning type is GPT, set 'primary' for sure!

- Remember the 'swap' format for swap partition, the 'Ext4' for Linux, and 'NTFS' for the shared spaces. (We're talking about the `Use As` field in the 'change ...' menu)

- In the bottom, there is also a pop-up menu in which the device to onstall the boot is to be determined. Choose your main hard drive in which you're installing the OS.

18. After the memory allocation step, choosing the region, and setting username and password, installation begins. After it's done, a reboot is performed. When system starts again (on the basis of boot priorities determined in the bios), it asks you to unplug the flash memory so the OS starts on your device.

* A probable problem in installation step is facing an 'Executing grub-install/dev/sdb failed' fatal error. In this case, a boot-repair inside the image file you are in, to do so:

Power off your system. Then turn it on and enter to the bootable flash image. When you enter

```
sudo apt-add-repository ppa:yannubuntu/boot-repair
# Then press enter to install it

sudo apt-get update

sudo apt-get install boot-repair
# Then type Y to install it
```

Then go to the start menu. Search for the 'boot-repair app. Click on it. 
The boot-repair process starts.
If asked, select the recommended boot-repair.
If asked, select to upload report to pastebin


19. After celebrating your new OS, go to 'Software and Updates' app. In ther 'additional drivers' tab, you may find your GPU driver (If you got one!). An installed-driver case is gained such that when you choose the first GPU driver item (like nvidia - the stable version - usually determined with the term 'tested') and choose to download it. Restart. If you got out of boot and saw your GPU, your driver is installed and ... here you go.

- In a case that you are stucked in the boot, if your kernel is still on (check with alt+ctl+f2 or f3 ...; if the command-prompt works you're ok), reboot. Enter the bios. Go to advanced options for ubuntu. Go to an older version. Inside that version, upgrade your ubuntu to a newr version. reboot. Go to 'Safotware and updates'. Try on the driver I said. Install or set the driver. Reboot. I fixed the issue this way :/.


*IMPORTANT TIP:* DO NOT CHANGE THE PARTITIONING OF YOUR HARD DISK AFTER INSTALLING OS! I DID IT ONCE AND IT TOOK LIKE A YEAR TO FIX IT AND I HAD TO FORMAT ALL MY DISK AND INSTALL THE OS AGAIN!!!
