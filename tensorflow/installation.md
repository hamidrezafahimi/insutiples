

## Installation

1. First:

```
sudo apt update

sudo apt install python3-dev python3-pip
```


2. Install the `python3-venv` ([installation guide](https://github.com/hamidrezafahimi/instructor_archive/blob/main/python/venv/installation.md)


3. Do:

```
mkdir ~/tensorflow-dev

cd ~/tensorflow-dev
```

4. Create and activate a virtual environment [like this](https://github.com/hamidrezafahimi/instructor_archive/blob/main/python/venv/bash.md)


5. Do:

```
pip install --upgrade pip
```


6. Now install the tensorflow within your environment:

```
pip install --upgrade tensorflow
```

It is about 600MB.


7. Check the installation:

- It must appear in the pip package list:

```
pip list | grep tensorflow
```

- Check the installed version:

```
python -c 'import os; os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"; import tensorflow as tf; print(tf.__version__)'
```


## Usage

To use the tensorflow wherever you want, just do:

```
source ~/tensorflow-dev/venv/bin/activate
```

And then run your code.