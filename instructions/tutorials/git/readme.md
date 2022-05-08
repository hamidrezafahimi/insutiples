


#### Get the git version
```
git --version
```

#### Make a local repository from a remote repository
```
git clone https
```

#### Get the current authentication data

```
git config --list
```


#### Set the user info in command-line

In order to correctly introduce the account which is commiting to the git.

```
git config user.name "<username>"
git config user.email "<email>"
```

#### Reomve the current user info in command-line

In order to correctly introduce the account which is commiting to the git.

```
git config --unset user.name "<username>"
git config --unset user.email "<email>"
```

#### Get the last changes

Including added or un-added files.

```
git status
```

#### Adding (after changes)

```
git add .
```

. stands for <the-current-dir>

#### Commiting (after adding)

```
git commit -m "<commit msg>"
```


#### Pushing

```
git push <remote> <branch>
```


#### Getting the list of remotes

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


#### Fetching a remote (before pulling it)

```
git fetch <remote>
```


#### Pulling a remote repo

```
git pull <remote> <branch>
```


#### Get the brief list of commits in the current branch

```
git log --oneline
```

#### Go to a specific commit

```
git checkout <sha1-hash-of-commit>
```

#### Get the current branch

```
git rev-parse --abbrev-ref HEAD
```

If the output is head, then you'r on no branch.

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

#### Set the default editor for git

Used in tools such as rebase.

```
git config --global core.editor "<editor-name>"
```


#### Get back the last commit and ignore all changes

```
git reset --hard
```

#### Git visualizer

```
gitk
```

#### Create an automaticly updating todo list (before each commit):
In the root of repo:
```
cd .git/hooks/
```
(For windows) Create a file named: **pre-commit**. Then put the followings inside it:
```
#!/bin/bash

git grep --heading -n TODO > TODO.txt
```

(For Linux - probably!) Create a file named: **pre-commit**. Then put the followings inside it:
```
#!/bin/sh

git grep --heading -n TODO > TODO.txt
```
  
  
