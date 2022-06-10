

#### List of commits

To get just a brief list of commits in the current branch:
  
```
git log --oneline
```

To get the list along with a working hostory tree:

```
git log --oneline --graph
```

#### Go to a specific commit

```
git checkout <sha1-hash-of-commit>
```

#### Get the current commit's hash:

Complete hash:

```
git rev-parse HEAD
```

Short version:

```
git rev-parse --short HEAD
```

#### Delete the last changes

To delete the last uncommited changes: 

```
git reset --hard
```


To delete the last commits: 

```
git reset --hard HEAD~<num-of-last-commits-to-be-deleted>
```
