## Remote

#### Getting a list of remotes

```
git remote -v
```

#### Adding a remote

```
git remote add <remoteName> <https://...remoteAddress.git>
```

#### Removing a remote

```
git remote rm <remote>
```


## Douplicate remotes

#### Create a mirror (non-fork copy) of a repo:
  Open Git Bash.
Create a bare clone of the repository.
  ```
git clone --bare https://github.com/exampleuser/old-repository.git
  ```
Mirror-push to the new repository.
  ```
cd old-repository.git
git push --mirror https://github.com/exampleuser/new-repository.git
  ```
Remove the temporary local repository you created earlier.
  ```
  cd ..
rm -rf old-repository.git
```
   
   
## Merge into a remote
  
#### Merge into a branch
```
cd path/to/project-b
git remote add project-a /path/to/project-a
git fetch project-a --tags
git merge --allow-unrelated-histories project-a/master
```
  




## Navigating


#### Go to a specific branch

```
git checkout <branch-name>
```

#### Go to a specific commit

```
git checkout <sha1-hash-of-commit>
```

