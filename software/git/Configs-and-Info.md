
#### Get the git version
```
git --version
```

#### Get the address to the root of current repo

```
git rev-parse --show-toplevel
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

#### Set the default editor for git

Used in tools such as rebase.

```
git config --global core.editor "<editor-name>"
```


#### Counting the size and number of repo objects

```
git count-objects -v
```


