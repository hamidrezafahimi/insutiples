
*IMPORTANT TIP: PLEASE DO NOT try this installation prodecure with 'anaconda' installed. I did it once and it screwed my python paths. The best experience is to do the installation with a fresh ubuntu (mine was 20.04 LTS)*


0. For installation guide, refer to the video:

https://www.youtube.com/watch?v=whAFl-izD-4

*Note: What is explained in the video is not so fresh and changes have been made in the methods. So preferably refer to the instructions given in the nvidia website*

1. Download and apply your proper graphics driver


2. Download and install cuda


3. Download and install cuDNN


4. Create an <OpenCV-root> folder. Inside it, clone the both source codes for 'opencv' and 'opencv_contrib' from the main 'opencv' account in github. In the <OpenCV-root>, create a <build> folder named 'build'.


5. In a generall case, install the cmake GUI:

```
sudo apt-get install cmake cmake-gui
```


6. In the cmake gui, first, set the path to opencv local repository (until '.../opencv') in the 'source' field. Then set the path to '.../build' in the 'build' field.

Hit 'Configure'

The flags that must be set are then shown in red.


7. Set some flags:

Set the following arguments IN ORDER!!:


- **extra modules flag:**

OPENCV_EXTRA_MODULES_PATH   --->   the/path/to/opencv_contrib/modules

Hit 'configure'.


- **cuda flags:**

OPENCV_DNN_CUDA    --->     ON
WITH_CUDA    --->     ON

Hit 'configure'.


- **for the 'PYTHON3_EXECUTABLE' flag**, run in a terminal:

```
which python3
```

So I did:

PYTHON3_EXECUTABLE --->    /usr/bin/python3

Hit 'configure'.


- **for the 'PYTHON3_INCLUDE_DIR' flag**, run in a terminal:

```
python3
```

Then run the following script:

```
from sysconfig import get_paths
from pprint import pprint
pprint(get_paths())
```
You'll be shown something like this:

```
{'data': '/usr',
 'include': '/usr/include/python3.8',
 'platinclude': '/usr/include/python3.8',
 'platlib': '/usr/lib/python3.8/site-packages',
 'platstdlib': '/usr/lib/python3.8',
 'purelib': '/usr/lib/python3.8/site-packages',
 'scripts': '/usr/bin',
 'stdlib': '/usr/lib/python3.8'}
```

Set the address in front of 'include' for the flag. 

So I did:

PYTHON3_INCLUDE_DIR --->    /usr/include/python3.8


- **For the 'PYTHON3_LIBRARY'** flag, run:

```
sudo find / -name "libpython*.so"
```

You'll be shown the python library files. Choose the one under the '/usr/lib' and with your python version (the one that is given in the terminal when you run the '$python3' command). Copy its path and set it for the flag.

So I did:

PYTHON3_LIBRARY --->  	/usr/lib/python3.8/config-3.8-x86_64-linux-gnu/libpython3.8.so


- **for the 'PYTHON3_NUMPY_INCLUDE_DIRS' flag**, 

First, in a terminal, install pip and numpy itself:

```
sudo apt install pip

sudo pip install numpy
```

Then find numpy like you did before:

```
sudo find / -name "numpy"
```

From the output, get copy the address with the '/usr/local/.../include/numpy' format and paste it until before '/numpy' for the flag. 

So I did:

PYTHON3_NUMPY_INCLUDE_DIRS --->    /usr/local/lib/python3.8/dist-packages/numpy/core/include


- **for the 'PYTHON3_PACKAGES_PATH' flag**, the previous address (for numpy) gives you the write address for python packages. Copy it until the end of '/dist-packages' for the flag.

So I did:

PYTHON3_PACKAGES_PATH --->    /usr/local/lib/python3.8/dist-packages

Check the above addresses to be valid in wour case. The video has more details about these stuff.


Hit 'Configure'


- **The rest of cuda flags**

For the next flag, check the 'cuda' wikipedia page. In the large table, find the version for your graphics card. Also, set the 2nd following flag with the proper generation:

CUDA_GENERATION   --->    (for-me-it-was-Maxwell)

*NOTE: The above flag is enough. If you hit configure now, the following will be set properly.*
 
CUDA_ARCH_BIN    --->    (for-my-geforce-950m-it-was-5.0)

Hit 'Configure'

- **GUI-related flags**

I once faced an error trying to show an image in my first opencv script after installation. I first did the following in an alternative terminal:

```
sudo apt install libgtk2.0-dev

# NOTE: The exact package name must be read from the terminal output which is shown after you face the aforementioned error. It suggests you what to install if you're using ubuntu.
```

Then, I fixed the issue by recompiling the opencv with some additional flags on. Those are:

CMAKE_BUILD_TYPE=RELEASE
CMAKE_INSTALL_PREFIX=/usr/local
WITH_TBB=ON
BUILD_NEW_PYTHON_SUPPORT=ON
WITH_V4L=ON
INSTALL_C_EXAMPLES=ON
INSTALL_PYTHON_EXAMPLES=ON
BUILD_EXAMPLES=ON
WITH_QT=ON
WITH_GTK=ON
WITH_OPENGL=ON

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

11. Check if the installation was successful. Open a python script in the terminal:

```
python3
```

Inside it:

```
import cv2
cv2.cuda.getCudaEnabledDeviceCount()
```

You should get a '1' if you have successfully built opencv with cuda support for your GPU.



