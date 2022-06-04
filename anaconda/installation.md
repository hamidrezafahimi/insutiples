

In home:

```
sudo apt update

sudo apt install curl -y

cd /tmp

```

Before the next comman in 'tmp', make sure you download the latest version by firstly visiting their official site:
https://repo.anaconda.com/archive/

```
curl --output anaconda.sh https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh

bash anaconda.sh
```

You should read the terms of service and confirm the location for anaconda files. 

After installetion, add the followings to your '.bashrc' in home:

```
# Add to .bashrc
export PATH=~/anaconda3/bin:$PATH
source ~/anaconda3/etc/profile.d/conda.sh
```

