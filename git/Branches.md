
#### Get the current branch

```
git rev-parse --abbrev-ref HEAD
```

If the output is head, then you'r on no branch.


#### Create a new branch
  
To have a new branch starting from the current commit:

```
git branch <branch-name>
```


#### Go to a specific branch

```
git checkout <branch-name>
```


#### Edit (remove, rename, mix, ...) commits of a branch

```
git rebase -i HEAD~5
```

5 means: I'm going to do the edit on until fifth commit before.


#### Remove local branch

```
git branch -D <branch> 
```

#### Remove remote branch

```
git push <remote> --delete <branch>
```


## Visualizer

To monitor just the current branch:

```
gitk
```

To monitor just all the branches:

```
gitk --all
```
