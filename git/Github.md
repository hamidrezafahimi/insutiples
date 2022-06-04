

#### Pushing nested repo in repo

These nested repos are seen with a white arrow on them in repo and include nothing.
To fix, navigate to the top directory of the nested repo. Run:

```
git rm --cached <folder-name>
git add --all
```

In the root, commit the changes. 
Push the results.

The nested git repos and the files within, will be pushed as normal directories. 
