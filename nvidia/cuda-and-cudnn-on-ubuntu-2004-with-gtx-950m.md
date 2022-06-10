
## graphics driver

Get a list of your available drivers:

```
ubuntu-drivers devices
```
Remember <the-one> with the 'recommended' term in front of it. Then:

```
sudo apt install <the-one>
```

## cuda

For installation of cuda refer to the nvidia's main instruction:

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions

Download and install cuda:

Go to the nvidia site. Find the proper cuda version for your GPU and OS version. 
Download it.
Install it using:

Don't use the following commands. Nvidia site gives you the propers for your case which you have determined.

```
dpkg -i <cuda-file.deb>
<The proper command for GPG key>
sudo apt-get update
<installation command>
```

Here are the detaoled steps since the first:

### Prerequirements

The steps I took:

Make sure you got gcc:

```
gcc --version
```

Otherwise, install it using:

```
sudo apt install gcc
```

Make sure you got Linux headers:

```
sudo apt-get install linux-headers-$(uname -r)
```

Then, based on the main instruction (Check! Don't use this!):

```
sudo apt-key del 7fa2af80
```

### Installation

Download your proper cuda version from:

https://developer.nvidia.com/cuda-downloads

They proposed me this:

```
#1 - Didn't run
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin

#2 - Didn't run
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600

#3 - Did it manually
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda-repo-ubuntu2004-11-7-local_11.7.0-515.43.04-1_amd64.deb

#4 - Run:
sudo dpkg -i cuda-repo-ubuntu2004-11-7-local_11.7.0-515.43.04-1_amd64.deb

#5 - Run:
sudo cp /var/cuda-repo-ubuntu2004-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/

```

I don't remember using #1 and #2. I did #3 manually with pasting the address in the brower (The download speed in shell was like it won't finish until the apocalypse!). And a '.deb' file was downloaded. I moved the '.deb' file to a folder and there, I executed the #4 and #5. It is generally presented in the main instruction that:

```
#4 - General case - run the previous command
sudo dpkg -i cuda-repo-<distro>_<version>_<architecture>.deb

#5 - General case - run the previous command
sudo cp /var/cuda-repo-<distro>-X-Y-local/cuda-*-keyring.gpg /usr/share/keyrings/
```

### Probably my mistake:

I did this but I think it was a mistake:

```
# I set 'ubuntu2004/x86_64' for my system:
https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb

sudo dpkg -i cuda-keyring_1.0-1_all.deb
```

### Fixing the probable mistake:

Then I  fixed it this way:

```
sudo apt clean

sudo apt update

sudo apt purge nvidia-* 

sudo apt autoremove
```
Reboot.


### The rest of installation:

The main installation procedure is:

```
#6
sudo apt-get update

#7
sudo apt-get -y install cuda
```

### Checking the installation success and version

For an installed cuda, the cuda version is determined with:

```
/usr/local/cuda/bin/nvcc --version
```

You should download your cuDNN file according to the version determined in the output.


## cuDNN

Go to the nvidia site. Find the proper cudnn version for your GPU and OS version. 
Download it.
Install it using the proper commands as given in:

https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html


To download, go to:

https://developer.nvidia.com/rdp/cudnn-download

There, find your suitable cuDNN version (based on your cuda version). Download it. Install it in by running the following command in folder the file is in

In the following, after 'sudo dpkg -i', hit 'tab' so the your present version is unpacked.

```
sudo dpkg -i cudnn-local-repo-ubuntu2004-8.4.1.50_1.0-1_amd64.deb 

# Then it proposed me to do (again; DON'T copy! run your proper command):
sudo cp /var/cudnn-local-repo-ubuntu2004-8.4.1.50/cudnn-local-E3EC4A60-keyring.gpg /usr/share/keyrings/
```

Then, start the installation. Remember not to copy these commands. After the 'lincudnn ...', yours must be set with 'tab'.

```
sudo apt-get update

# Install the runtime library.

sudo apt-get install libcudnn8=8.x.x.x-1+cudaX.Y

# Install the developer library.

sudo apt-get install libcudnn8-dev=8.x.x.x-1+cudaX.Y

# Install the code samples and the cuDNN library documentation.

sudo apt-get install libcudnn8-samples=8.x.x.x-1+cudaX.Y
```



