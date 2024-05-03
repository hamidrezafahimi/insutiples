## cuda

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin

sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600

# Download the repo
wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda-repo-ubuntu2204-12-4-local_12.4.0-550.54.14-1_amd64.deb
# if having problems with wget, just go to the above link so that it is downloaded as a typical deb file

sudo dpkg -i cuda-repo-ubuntu2204-12-4-local_12.4.0-550.54.14-1_amd64.deb

sudo cp /var/cuda-repo-ubuntu2204-12-4-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update

sudo apt-get -y install cuda-toolkit-12-4
```

## cudnn

```
wget https://developer.download.nvidia.com/compute/cudnn/9.0.0/local_installers/cudnn-local-repo-ubuntu2204-9.0.0_1.0-1_amd64.deb
# if having problems with wget, just go to the above link so that it is downloaded as a typical deb file

sudo dpkg -i cudnn-local-repo-ubuntu2204-9.0.0_1.0-1_amd64.deb

sudo cp /var/cudnn-local-repo-ubuntu2204-9.0.0/cudnn-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update

sudo apt-get -y install cudnn


#To install for CUDA 11, perform the above configuration but install the CUDA 11 specific package:

sudo apt-get -y install cudnn-cuda-11

#To install for CUDA 12, perform the above configuration but install the CUDA 12 specific package:

sudo apt-get -y install cudnn-cuda-12
```
