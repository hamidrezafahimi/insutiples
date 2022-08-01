
This is the installation guide for installation of cudnn on ubuntu. It is performed on a fresh ubuntu 20.04 LTS. My graphics driver was nvidia GTX 950M.

1. Go to the [nvidia site](https://developer.nvidia.com/cudnn). Find your suitable cuDNN version (based on your cuda version and OS version). Download it.

2. Installation is based on the commands given in the [nvidia installation guide](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html). But if you're on a hurry, the following step are a simpified go-to version.

3. Place the cudnn '.deb' file in the home directory. In the following, after 'sudo dpkg -i cudnn', hit 'tab' so the your present version is unpacked.

```
sudo dpkg -i <cudnn-file>.deb
### Mine was: sudo dpkg -i cudnn-local-repo-ubuntu2004-8.4.1.50_1.0-1_amd64.deb 

### Then it proposed me to do:
sudo cp /var/cudnn-local-repo-ubuntu2004-8.4.1.50/cudnn-local-*-keyring.gpg /usr/share/keyrings/
```

4. After unpacking, start the installation. First of all refer to the [nvidia installation guide](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) for a more reliable set of commands depending on your current time. Remember not to copy these commands. After the 'lincudnn8=', 'lincudnn8-dev=', and 'lincudnn8-samples=', yours must be set with 'tab'.

```
sudo apt-get update

# Install the runtime library.
sudo apt-get install libcudnn8=8.x.x.x-1+cudaX.Y

# Install the developer library.
sudo apt-get install libcudnn8-dev=8.x.x.x-1+cudaX.Y

# Install the code samples and the cuDNN library documentation.
sudo apt-get install libcudnn8-samples=8.x.x.x-1+cudaX.Y
```

