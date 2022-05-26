

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

(For Linux) Create a file named: **pre-commit**. In the same folder, run:

```
chmod +x pre-commit
```

Then put the followings inside *pre-commit*:

```
#!/bin/sh

git grep --heading -n TODO > TODO.txt
git add TODO.txt
```


