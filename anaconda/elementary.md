
### General initial task

Do the following each time you're going to use anaconda in a terminal:

```
export PATH=~/anaconda3/bin:$PATH

source ~/anaconda3/etc/profile.d/conda.sh
```

*TIP:* I strongly recommend not to add the above to your `.bashrc`!


#### Create a conda environment

```
conda create --name <env-name> python=<desired-python-version>
```
For a triple-number python version like 3.6.11 it didn't work for me. But for 3.6 it worked.

#### Activating a conda environment

```
conda activate <env-name>
```

#### Deactivating a conda environment

```
conda deactivate 
```

#### Get a list of environments

```
conda info --env
```


#### Get a list of environment packages and their versiond

```
conda list
```

#### Get the anaconda version

```
conda --version
```



