


* [Here](http://www.cs.umd.edu/~mount/ANN) is the documentation.

* Download [this](http://www.cs.umd.edu/~mount/ANN/Files/1.1.2/ann_1.1.2.zip) as the source code and extract it in - for example - `$HOME` directory.

* Do:

```
 cd ~

 make
```
* This will provide a list of platforms and options under which to compile ANN. See your particular configuration on this list and try the comman. For me it was:

```
make linux-g++
```

* Now in the `CMakeLists.txt` of the project in which you are going to use *ANN*, you can simply add:

```
set(ANN_DIR  /home/hamid/ann_1.1.2)
include_directories(${ANN_DIR}/include)
link_directories(${ANN_DIR}/lib)
```
