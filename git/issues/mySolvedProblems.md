





### Problem:

Log in to GitHub from the command line with multiple accounts



### Solution:

**Link:**
https://stackoverflow.com/questions/34731832/log-in-to-github-from-the-command-line-with-multiple-accounts


Use this command to relogin with a different account on GitHub:

```
git remote set-url origin "remote repository URL"
```

From the docs:

    If you omit --global or use --local, the configuration is applied only to the current repository.

In your shell, add your user name:

git config user.name "your_username"

And your email address:

git config user.email "your_email_address@example.com"

To check the configuration, run:

git config --list

And to compare to your global configuration, run:

git config --global --list



