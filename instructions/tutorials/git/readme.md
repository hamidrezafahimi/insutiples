


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

### Remotes

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

### Pulling
  
#### Fetching a remote (before pulling it)

```
git fetch <remote>
```


#### Pulling a remote repo

```
git pull <remote> <branch>
```

### Commits and monitoring

#### Get a commit list

To get just a brief list of commits in the current branch:
  
```
git log --oneline
```

To get the list along with a working hostory tree:

```
git log --oneline --graph
```
#### Git visualizer

To monitor just the current branch:

```
gitk
```

To monitor just all the branches:

```
gitk --all
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


### Branch
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

### Config
  
#### Set the default editor for git

Used in tools such as rebase.

```
git config --global core.editor "<editor-name>"
```


#### Get back the last commit and ignore all changes

```
git reset --hard
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
git add TODO.txt
```

(For Linux - probably!) Create a file named: **pre-commit**. Then put the followings inside it:
```
#!/bin/sh

git grep --heading -n TODO > TODO.txt
git add TODO.txt
```
  
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
   
  
#### Merge into a branch:
```
cd path/to/project-b
git remote add project-a /path/to/project-a
git fetch project-a --tags
git merge --allow-unrelated-histories project-a/master
```
  
