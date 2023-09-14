

1. Do:

```
sudo apt-get update -y

sudo apt-get install libeigen3-dev
```

2. To add to a `CMakeLists.txt` file, typically the include directory is `/usr/include/eigen3`. So add something like the following to the `CMakeLists.txt`:

```
set(EIGEN_DIR  /usr/include/eigen3)
include_directories(${EIGEN_DIR})
```