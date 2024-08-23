# Setting-up Git
- Show the version of your Git installation
```bash
git -v
```
\
- Show the configurations
```bash
git config -l
```

- Configure your username and email
```bash
git config --global user.name "JISHNU-2002"
```

```bash
git config --global user.email "jsjishnu2002@gmail.com"
```

- The username and email is used by Git for every commit that you will create
- Without this configuration, you are not able to commit to a repository

- To show the origin of the configurations,  `--show-origin` parameter shows you in which file a configuration is located
```bash
git config -l --show-origin
```
- This command above allows you to find the _.gitconfig_ file that is in your user directory. That _.gitconfig_ file contains now the username and the email that you configured.

# Working with local Repositories
- Initialize an empty Git repository
```bash
git init
```

- To clone an existing repository
```bash
git clone https://github.com/username/repository.git
```

- Show the status of your repository
```bash
git status
```

- Stage a specific file
```bash
git add readme.txt
```

- Stage all changed files
```bash
git add .
```

- If you created a repository at Github and wants to add files to that repository
```bash
git add remote "git@github.com/JISHNU-2002/repo_name.git"
```

- Set the origin branch
```bash
git add branch -M main/master
```

- Commit the staged files
```bash
git commit -m "Create readme file"
```

- Show the changes of a specific file
```bash
git diff readme.txt
```

- Show the changes in your working directory
```bash
git diff
```

- Show the changes in your staging area
```bash
git diff --staged
```

- Show the history/log
```bash
git log
```

- Show the history/log with one commit per line
```bash
git log --pretty=oneline
```

- Checkout a specific commit by its snapshot hash
```bash
git checkout b346471
```

- Push the committed changes to your remote repository 
```bash
git push origin main
```

- To fetch and merge the latest changes from the remote repository
```bash
git pull origin main
```

- Navigate back to your main branch
```bash
git checkout main
```


