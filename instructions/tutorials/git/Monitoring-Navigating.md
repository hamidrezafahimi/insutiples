

## List of commits

To get just a brief list of commits in the current branch:
  
```
git log --oneline
```

To get the list along with a working hostory tree:

```
git log --oneline --graph
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


## Navigating

#### Go to a specific commit

```
git checkout <sha1-hash-of-commit>
```


#### Go to a specific branch

```
git checkout <branch-name>
```