
This is the installation guide for installation of cuda on ubuntu. It is performed on a fresh ubuntu 20.04 LTS. My graphics driver was nvidia GTX 950M.


1. Go to [the nvidia site](https://developer.nvidia.com/cuda-downloads). Find the proper cuda version for your GPU and OS version. Download it manually. It's a '.deb' file. I call it < cuda-file>.

2. Typically, for installation prerequisites, you must refer to the nvidia's [main instruction](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html). Although I took none of the pre-installation actions and it worked for me. In other words, the following instructions are enough to install cuda on a fresh ubuntu 20.04 - as the experiment states. However you can take a look to the link above to make sure everything is fine.

3. Put the cuda-file in the home directory. Then:

```
### Actually, do: sudo dpkg -i <cuda-file>.deb
sudo dpkg -i cuda-repo-<distro>_<version>_<architecture>.deb

### The following is often proposed in the terminal log of the previous command
sudo cp /var/cuda-repo-<distro>-X-Y-local/cuda-*-keyring.gpg /usr/share/keyrings/
```

4. Now, install cuda:

```
sudo apt-get update

sudo apt-get -y install cuda
```

5. Check the installation success:

```
/usr/local/cuda/bin/nvcc --version
```

You should get the version of your installed cuda.

