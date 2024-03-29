
Git submodules allow you to keep a git repository as a subdirectory of another git repository. Git submodules are simply a reference to another repository at a particular snapshot in time. Git submodules enable a Git repository  to incorporate and track version history of external code.


### Declare a directory as a sobmodule (before commiting)

If you've cloned a repo inside your repo, declare it as a submodule before adding it into the stage space.

```
#if needed
#git config --global --add safe.directory path/to/the/interior/folder

git submodule add <url-for-the-root-repo>.git path/to/the/interior/folder
```

If you need to link a specific branch (version):

```
git submodule add -b <desired-branch-or-version> <url-for-the-root-repo.git> path/to/the/interior/folder
```


### Syncing and Updating sobmodules

This will update the submodule to the latest remote commit:

```
git submodule update --remote --merge
```

To synchronize addresses for submodules:

```
# In the root of repo
git submodule sync --recursive
```

When cloning empty submodules inside your repo, do the following in order to update your submodules:

```
git submodule update --init --recursive --force
```

To force-update a specific submodule:

```
git submodule update --init --recursive --force <respective-module-folder-path>
```

### Ignore the changes made into local submodule

Inside the `.gitmodules` file, for a specific sobmodule, you got something like:

```
[submodule "PX4-Autopilot"]
	path = PX4-Autopilot
	url = https://github.com/PX4/PX4-Autopilot.git
```

Change it this way so that the changes made into the local folder (e.g. build and compile) will be ignored by git.

```
[submodule "PX4-Autopilot"]
	path = PX4-Autopilot
	url = https://github.com/PX4/PX4-Autopilot.git
	ignore = dirty
```

### Remove a submodule

```
#1. git submodule deinit -f -- a/submodule
3. git rm -f -r a/submodule
2. rm -rf .git/modules/a/submodule
#4. git rm -r --cached a/submodule
```
