

## Intalllation

Install:

```
pip install <pkg-name>
```

Uninstall:

```
pip uninstall <pkg-name>
```

## Config

List of installed python packages:

```
pip list
```

## Issues

### Dealing with the connection issue during pip installation

Performing the `pip install` command, I have had problems in the step in which pip downloads the installation wheel (the `.whl` file). The solution for this, is:

- Find the proper version of the wheel (the proper configuration is declared in the name of the file) in the internet and download it in a safe way (using download managers or whatever). The proper wheel can be found [here](https://pypi.tuna.tsinghua.edu.cn/simple/). Add the name for your desired package in the address of the link. If your desired package installation command is `pip install opencv-python`, then the the link must be `https://pypi.tuna.tsinghua.edu.cn/simple/opencv-python` Maybe you can find what you want!

- In the directory in which the lownloaded wheel lies, do:

```
pip install <downloaded-wheel>.whl
```

