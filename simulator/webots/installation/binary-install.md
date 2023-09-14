
This is the instruction to install a stand-alone webots 

Requirements:

```
sudo apt install mesa-utils

glxinfo | grep OpenGL
```

Installation: 

```
wget -qO- https://cyberbotics.com/Cyberbotics.asc | sudo apt-key add - 

sudo apt-add-repository 'deb https://cyberbotics.com/debian/ binary-amd64/'

sudo apt-get update

sudo apt-get install webots
```
