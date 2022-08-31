# Project 0 - Git Guide

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Is used to create a copy of a specific repository or branch within a repository
    - By cloning with Git, you get the entire repository - all files, all branches, and all commits
    - Once a repository already exists on a remote, like on GitHub, then you would clone that repository so you could interact with it locally
  - `git clone [url]`
- add
  - Adds new or changed files in your working directory to the Git staging area
    - This step allows you to choose what you are going to commit
    - Allows you to systematically shape your commits and your history anyway
  - `git add [filename]`
- rm
  - Removes specific files or a group of files from a Git repository
    - Used for removing files from both the staging index and the working directory
  - `git rm <filename>`
- commit
  - Captures a snapshot of the project's currently staged changes
    - Commits are the building blocks of "save points" within Git's version control
	- By using commits, you're able to craft history intentionally and safely
  - `git commit -a -m "commit message"`
- push
  - Uploads all local branch commits to the corresponding remote branch
    - Updates the remote branch with local commits
	- Comparable to *publish* or *update*
  - `git push`
- fetch
- merge
- pull
- branch
- checkout
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
- .gitignore file
- ~~.git/hooks~~

## GitHub

- Pull requests
- SSH authentication to repositories
- ~~Actions~~