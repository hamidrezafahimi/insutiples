Kitware now provides an APT Repository that supports Ubuntu 16.04, 18.04, and 20.04. So we can install it easily following these steps:

A-1. Uninstall the default version provided by Ubuntu's package manager and configuration by using:

```
sudo apt remove --purge --auto-remove cmake
```

A-2. Prepare for installation

```
sudo apt update && \
sudo apt install -y software-properties-common lsb-release && \
sudo apt clean all
```

A-3. Obtain a copy of kitware's signing key.

```
wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | sudo tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null
```

A-4. Add kitware's repository to your sources list for Ubuntu Focal Fossa (20.04), Ubuntu Bionic Beaver (18.04) and Ubuntu Xenial Xerus (16.04).

```
sudo apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main"
```

A-5. As an optional step, is recommended that we also install the kitware-archive-keyring package to ensure that Kitware's keyring stays up to date as they rotate their keys.

```
sudo apt update
sudo apt install kitware-archive-keyring
sudo rm /etc/apt/trusted.gpg.d/kitware.gpg
```

A-5.Note If running sudo apt update gets the following error:

```
Err:7 https://apt.kitware.com/ubuntu bionic InRelease
The following signatures couldn't be verified because the public key is not available: NO_PUBKEY <key-num>
Fetched 11.0 kB in 1s (7552 B/s)
```
Copy the public key `<key-num>` and run this command:
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <key-num>
```
A-6. Finally we can update and install the cmake package.
```
sudo apt update
sudo apt install cmake
```
