
### Linked or Nested Repositories

#### Pushing nested repo in repo

There are multiple approaches when you're going to add a repo inside another one.

##### 1. The interior repo is yours and you just want to keep your codes

In this case, just follow the most simple approach:

1. Make sure that at first, the interior folder does not exist in the exterior. (By 'at first', I mean in the last commit)

2. Create a folder with same name of the interior repo

3. Copy all non-hidden files and folders (excluding all git-related things. Like '.gitignore', '.git/', etc.)

4. Add and commit! You just added what you needed. You said you didn't need the 'being-git-repo' aspect of your interior folder.

##### 2. You're not on the mood, or for other reasons, you JUST want to upload and no extra copying and pasting

If you put a git repo inside another one and push, you'll face a nested repo.
These nested repos are seen with a white arrow on them in repo and include nothing.
To fix, navigate to the top directory of the nested repo. Run:

```
git rm --cached <folder-name>
git add --all
```

In the root, commit the changes. 
Push the results.

The nested git repos and the files within, will be pushed as normal directories. 

*NOTE: It is seen that in this case, after the second command, some times you face an error like below:*

```
# I had a 'tello_driver' cloned, and I just wanted to push it in a simple approach. But I faces this:

warning: adding embedded git repository: tello_ws/src/tello_driver
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint: 
hint: 	git submodule add <url> tello_ws/src/tello_driver
hint: 
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint: 
hint: 	git rm --cached tello_ws/src/tello_driver
hint: 
hint: See "git help submodule" for more information.
```

Well, in such a case, idk what to do. Follow the method 1 or 3!


#### Linking a Folder inside a Repo to another Repo

The third method is creating the interior folder as a submodule. To do so, refer to the the instruction file: `Submodules.md`.

