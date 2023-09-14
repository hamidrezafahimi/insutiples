
# Compile and Run Using GCC and Command-Line

## Compile and Run a Single Script

To run a single cpp script, 

Compile it using:

```
g++ <script-to-run> -o <exec-file-name>
```

Then, run the output executable file using:

```
./<exec-file-name>
```

## Compile and Run Multiple Scripts with GCC in Command-Line

If you have multiple `.cpp` files (probably within each, included a `.h` file), compile and create a single executable file:

```
g++ -Wall -o <exec-file-name> <script-1> <script-2> ...
#  -Wall  - this flag is used to turn on most compiler warnings
```

Then, run the output executable file using:

```
./<exec-file-name>
```

# Compile and Run CPP Scripts Using Makefile

Check [here]() to learn how to create a simple makefile.

1. Create a Makefile

2. In the folder containing the Makefile, Compile:

```
make
```

3. Run the main executable:

```
./<exec-file-name>
```

# Compile and Run CPP Scripts Using CMake

Check [here]() to learn how to create a simple `CMakeLists.txt` file.

1. Create a `CMakeLists.txt` file. 

2. In the same folder, run the following to create a Makefile:

```
cmake .
```

3. Right there, a `Makefile` is now created. Run the following to compile your programs:

```
make
```

4. An executable is created in the same directory with the same name as you specified for the project. To run the code, do:

```
./<exec-file-name>
```

