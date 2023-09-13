
For ubuntu 2022, run in order:

```
sudo apt update

sudo apt install -y curl apt-transport-https

curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/ms-vscode-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ms-vscode-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list

sudo apt update

sudo apt install -y code
```


For ubuntu 2020:

```
sudo apt update 

sudo apt install software-properties-common apt-transport-https wget

wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

sudo apt install code
```

### How i added keyboard shortcut to move editor right of the current window

1. `ctrl` + `shift` + `P`

2. Type: `Open Keyboard Shortcuts` and select the option

3. search `move editor to right`

4. select the `+` sign on the left of the found option

5. Set your desired shortcut. I set `ctrl`+`meta`+`->`

6. I also did for other 3 directons

### Setup for c++

Install these two

```
- c/c++ microsoft

- Code runner by jun han

- intellicode
```

- Do `code .` on the project folder. on the relative directory `.vscode/settings.json`, add the absolute directory contaninig the `CMakeLists.txt`

- On the opened project window, on the upper bar, choose the proper compiler (for me gcc - idk which version) and cmake configuration starts

There are two important files in `.vscode` folder in the root of the project. I put the a sample of their content for one of my successfuly configured projects, just in case:

```
# file: settings.json

{
    "cmake.sourceDirectory": "/media/hamid/Workspace/smart_POV/env/AIMS/build",
    "cmake.configureOnOpen": true
}

# file: c_cpp_properties.json

{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [
                "${workspaceFolder}/**",
                "/usr/local/include/opencv4/"
            ],
            "defines": [],
            "compilerPath": "/usr/bin/gcc",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "linux-gcc-x64"
        }
    ],
    "version": 4
}
```
