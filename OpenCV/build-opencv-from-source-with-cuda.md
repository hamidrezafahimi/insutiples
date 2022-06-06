
0. For installation guide, refer to the video:

https://www.youtube.com/watch?v=whAFl-izD-4

1. Download and apply your proper graphics driver

2. Download and install cuda:

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

3. Download and install cuDNN

Go to the nvidia site. Find the proper cudnn version for your GPU and OS version. 
Download it.
Install it using the proper commands as given in:

https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html


4. Create an <OpenCV-root> folder. Inside it, clone the both source codes for 'opencv' and 'opencv_contrib' from the main 'opencv' account in github. In the <OpenCV-root>, create a <build> folder named 'build'.

5. In a generall case, install the cmake GUI:

```
sudo apt-get install cmake cmake-gui
```

6. In the cmake gui, first, set the path to opencv local repository (until '.../opencv') in the 'source' field. Then set the path to '.../build' in the 'build' field.

Hit 'Configure'

The flags that must be set are then shown in red.

7. Set some flags:

Set the following arguments:

OPENCV_EXTRA_MODULES_PATH   --->   the/path/to/opencv_contrib/modules
OPENCV_DNN_CUDA    --->     ON
WITH_CUDA    --->     ON

For the rest, I did:

PYTHON3_EXECUTABLE --->    /usr/bin/python3
PYTHON3_INCLUDE_DIR --->    /usr/include/python3.8
PYTHON3_LIBRARY --->    /usr/lib/x86_64-linux-gnu/libpython3.8.so
PYTHON3_NUMPY_INCLUDE_DIRS --->    /usr/lib/python3/dist-packages/numpy/core/include
PYTHON3_PACKAGES_PATH --->    /usr/lib/python3/dist-packages

Check the above addresses to be valid in wour case. The video has more details about these stuff.

For the next flag, check the 'cuda' wikipedia page. In the large table, find the version for your graphics card. Also, set the 2nd following flag with the proper generation:
 
CUDA_ARCH_BIN    --->    (for-my-geforce-950m-it-was-5.0)
CUDA_GENERATION   --->    (for-me-it-was-Maxwell)

Hit 'Configure'

8. After configuration is done and you have no red flags, hit 'Generate'

9. Go to the <build> folder. Start the building:

In the following, I set -j7 to use 7 CPU cores in building procedure

```
make -j7
```

10. In the <build> directory:

```
sudo make install
```

