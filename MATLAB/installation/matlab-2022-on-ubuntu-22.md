

0. Mount iso-file  Matlab912R2022a_Lin64.iso

In the mounted file:
```
chmod +x install
./install 
```

1. Run  "install"  from mounted iso-file and if you see login/password/signin form (installer has access to internet)
     then in upper right corner in  "Advanced Options"  select setup mode  "I have a File Installation Key"
     If internet access is absent then required setup mode will be auto-selected and you do not need to select in manually


2. When you will be asked to  "Enter File Installation Key"  enter
50874-33247-14209-37962-45495-25133-28159-33348-18070-60881-29843-35694-31780-18077-36759-35464-51270-19436-54668-35284-27811-01134-26918-26782-54088


3. When you will be asked to  "Select License File"  select file  "license.lic"  from folder with  Matlab912R2022a_Lin64.iso  file


4. Then select folder where you want Matlab to be installed (<matlabfolder>)
     To avoid problems you need <matlabfolder> which have all access rights for you
     If it hard for you to select anything then use  "/home/<YourUserName>/Matlab/R2022a"  for example
     
*Note:* The best way is to select opt for this:

```
cd ~
cd /opt
sudo mkdir MATLAB
cd MATLAB
sudo mkdir R2022a
cd ~
sudo chown -R $LOGNAME: /opt/MATLAB/R2022a
```

Then set the installation directory as "/opt/MATLAB/R2022a"


5. When you will be asked to  "Select products"  select components you need
     If you all components are selected Matlab will need about 30Gb of disk space and somewhat longer startup time
     If you select only  "MATLAB"  then Matlab will need about  3Gb of disk space
     You better install Matlab on SSD disk for better startup time, so most likely you do not want to waste SSD-disk space for nothing


6. After installation is done copy file  "libmwlmgrimpl.so"  from folder with  Matlab912R2022a_Lin64.iso  file
     to ALREADY EXISTING FOLDER  "<matlabfolder>\bin\glnxa64\matlab_startup_plugins\lmgrimpl"
     WITH OVERWRITING OF EXISTING FILE (<matlabfolder> - is where you have selected to install Matlab on step 4)
     If you was NOT asked about overwriting then you are doing something wrong (or Matlab was not installed successfully)!!!


7. Work with Matlab :)


P.S.
During update/change of already working Matlab there is no need to execute step 3
Step 6 might be necessary to repeat (if during update/change of Matlab file  "libmwlmgrimpl.so"  was overwritten)
If after update/change you get error during startup of Matlab then first try to redo the step 6
