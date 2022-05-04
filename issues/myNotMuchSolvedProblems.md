



### Problem:

git pull accepting theirs



### Solution:

If you want to simply ignore any local modifications to files from the repo, for example on a client that should always be a mirror of an origin, run this (replace master with the branch you want):

git fetch && git reset --hard origin/master

How does it work? git fetch does git pull but without merge. Then git reset --hard makes your working tree match the last commit. All of your local changes to files in the repo will be discarded, but new local files will be left alone.

* Above did not work properly





