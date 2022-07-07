


create the softlink:

```
ln -s /target/path/ ~/link/path 

# example: ln -s /media/hamid/Workspace/ ~/ws 
```

Create mountpoint on softlink:

```ln 
# 1:
sudo blkid
# 2: Copy the UIID related to your partition to be mounted
# 3:
sudo nano /etc/fstab 
# 4: Do the proper edit within the opened text file (Refer to the next block)
# 5:
sudo mkdir /target/path
# example: sudo mkdir /media/hamid/Workspace
# 6:
sudo mount -a
```

What you should do in the 'fstab' can be found in the following:

```
# What it was:

#/etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sdb1 during installation
UUID=bc722432-6702-4272-b8cd-8e0fbcc94cca /               ext4    errors=remoun>
# /boot/efi was on /dev/sdb5 during installation
UUID=B73A-1111  /boot/efi       vfat    umask=0077      0       1
# swap was on /dev/sdb2 during installation
UUID=ec9a80e5-f645-479d-ae72-25a3197b92a0 none            swap    sw           >


# --------------------------------------------------------------------------------


# How I changed it:

#/etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sdb1 during installation
UUID=bc722432-6702-4272-b8cd-8e0fbcc94cca /               ext4    errors=remoun>
#
UUID=477D2BB02F80432D   /media/hamid/Workspace/ ntfs    defaults        0      >
# /boot/efi was on /dev/sdb5 during installation
UUID=B73A-1111  /boot/efi       vfat    umask=0077      0       1
# swap was on /dev/sdb2 during installation
UUID=ec9a80e5-f645-479d-ae72-25a3197b92a0 none            swap    sw           >
```

Remember that you should hit 'tab' (not 'space') after adding each of <mount point>,
<type>, <options>, <dump>, and <pass> in front of the UUID=477D2BB02F80432D 
(or whatever UIID it is). 
Don't put '>' at the end of the line!
After editing, hit 'ctrl+X', then 'Y', and then 'Enter' to save and exit.

After creating such softlink, you'll need to do the following in each subdirectory which is a git repository.

```
git config --global --add safe.directory /target/path/path/to/repo
# example: git config --global --add safe.directory /media/hamid/Workspace/coder_archive
```
