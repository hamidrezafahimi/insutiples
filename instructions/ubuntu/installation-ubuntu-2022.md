

1. Make a bootable flash. 

(in ubuntu) Use the app "startup disk creator". Set the flash memory and the .iso file separately in the two fields.

(in window) ... You can use rufus.

2. Make sure that the bootable flash is connected to the usb port. Restart.

3. When the system starts. Hit 'delete', so the bios UI opens.

3. Go to the 'boot' tab.

4. Here, the boot options (priorities) are listed. Hit 'enter' on the first priority and in the pop-up menu, set the flash memory boot for it. 

5. Save & exit. (The proper key must be determined in an instruction menu beside the pages. Usually: 'F10')

6. On reboot , the image file opens. You can try ubuntu or choose to install it. A typical way is to try it (in the flash memory) so you can first format you hard and determine your storage partitions.

7. Inside ubuntu, you can manage your hard disk partitions using the app 'Disks'. Select the hardware from the left menu. 

8. To format the disk, you shold firs unmount the "swap" partition. To do so, in the graphical interface, click on the partition with the "swap" name. Hit the 'square' botton on the down-left to unmount it. 

9. Hit the triple-dot botton. Select the "Format Disk". 

10. In the "Erase" field, choose the 'Quick' type (No need to feel with zeros). In the "Partitioning" field, select the 'GPT' mode or 'MBR'. (Only MBR worked in myy system).

11. When the formating is finished, you can add partitions hitting the 'cross' botton in the down-left. Determine name and choose a proper format. Choose a 'Ext4' format for a partition in which you're going to install Linux. Choose 'NTFS' to acces data from both Linux and windows. 

12. Determine the size for your partition.

13. In a disk in which you're going to intall OS, create a partition with 'swap' format. If the format is not found in the pop-up menu, hit 'more options' (or something like that!). You'll probably find it.

14. When you created your desired partitions, start intalling ubuntu using the item in the left-menu

15. Continue the intalaltion steps like the next-next paradigm ... . Note that:

- A 'normal' and 'offline' installation is often prefered.

- When arrived to the step in which the disk partitions are listed, the main partitions must be allocated in the 'root' (Determined with '/'). 

- In some platforms, an 'EFI' partition is necessary with like 100 MB size and '/efi' allocation. A partition for '/boot' is necessary too. Starting the installation, it is possible that you face an error related with non-allocating such partitions. In such cases, simply add the mentioned partitions, in the list. 

- Remember the 'swap' format for swap partition, the 'Ext4' for Linux, and 'NTFD' for the shared spaces.

16. After the memory allocation step, installation begins. After it's done, a reboot is performed. When system statrts again (on the basis of boot priorities determined in the bios), it asks you to unplug the flash memory so the OS starts on your device.

17. After celebrating your new OS, go to 'Software and Updates' app. In ther 'additional drivers' tab, you may find your GPU driver (If you got one!). An installed-driver case is gained such that when you choose the first GPU driver item (like nvidia - the stable version) and choose to download it. Restart. If you got out of boot and saw your GPU, your driver is installed and ... here you go.

- In a case that you are stucked in the boot, if your kernel is still on (check with alt+ctl+f2 or f3 ...; if the command-prompt works you're ok), reboot. Enter the bios. Go to advanced options for ubuntu. Go to an older version. Inside that version, upgrade your ubuntu to a newr version. reboot. Go to 'Safotware and updates'. Try on the driver I said. Install or set the driver. Reboot. I fixed the issue this way :/.
