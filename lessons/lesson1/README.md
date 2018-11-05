# Lesson 1: Version control with Git

## Version control

Has one of these happened to you?

- "I accidentally deleted my code and now I'm sad"
- "I broke something in my code and I can't remember how it was"
- "I don't know if I meant to send my collaborator `code_v3_oct31_2018_A1.py` or `code_v3_oct31_2018_B7.py`"
- "My collaborator changed half of my code, but I've updated it a bunch since I sent it to them 6 months ago and now I don't know how to combine the two"


Version control systems were developed to solve these challenges of collaborating on code that changes over time. Different version control systems differ in the nitty gritty of their inner workings, but they all allow multiple collaborators to work on the same code, and to revert code to old snapshots if something breaks.

If you are working with collaborators on code, having a version control system in place will make your lives much easier.

### I fly solo, why bother?
If you mostly work on your science and your code by yourself (how??), you might wonder why you would ever need version control. Non-collaboration bonuses:

1) You always have time-stamped snapshots of your code that you can revert to if something breaks.

2) Version control makes it really easy to host a backup of your code on a local or remote server.

3) You can easily check out code on multiple machines, say, if you're working via ssh on a remote computer or in the cloud. :wink:

4) Git hosting sites (like GitHub) provide a well-established way to share your beautiful science analysis and/or code that won't fit in the footnotes of a paper.


## WTG?! (What the Git)
You should have an idea of what Git *does* from the pre-class homework, but what *is* Git? 

**Git: the software** is a super efficient and popular choice of version control system.

**Git: the philosophy** or **gitflow** is a workflow and set of practices about how to develop and share code. We will steal some inspiration from the software industry to make our academic coding lives a little more techincal, but a lot more reproducible.

### The basics: repos
A Git **repository** or **repo** is a directory that is set up to be tracked by Git. Any old directory can be turned into a repository with the `git init` command. This command dumps some files in a hidden `.git` folder, and from then on Git will track all changes to the new repo and its contents.

### The basics: commits
You can think of Git **commits** as snapshots or checkpoints in the history of your repo. You get to decide how much work you do between commits, and you also get to leave a message to descibe those changes.

Take a walk with me to the year 2020 (or <current_year>+2 if you're joining us from the future). You've been tracking your research in a git repo and somebody asks for a function, `awesome_func()` that you remember writing about 2 years ago. The problem is you deleted that function because you didn't need it. Thanks to the magic of git, you have a checkpoint with it somewhere... 

When you look at your git commit history to find it, which would you rather see?

> s87f6s9 - I added stuff (Thu Nov 1, 2018)  
> klh54as - deleting stuff (Fri Nov 30, 2018)  
> f984jst - whoops (Sat Dec 1, 2018)  
> un23hc8 - adds a whoooole lotta stuff from December (Fri Dec 28, 2018)  

Or:

> s87f6s9 - Add awesome_func() to improve performance of slow_func() (Thu Nov 1, 2018)  
> klh54as - Fix a bug in awesome_func() that made it crash (Fri Nov 2, 2018)  
> f984jst - Remove awesome_func() in favor of even_better_func() (Fri Nov 9, 2018)  
> un23hc8 - Added figures to even_better_func() (Tue Nov 13, 2018)  

An important part of **Git: the philosophy** is making commits that are retrievable later. Some guiding principles will have you committing like a pro in no time:

1) Commit often
2) Leave descriptive commit messages 
3) Make commits atomic (single units of work)

1: How often depends on your work. If in doubt, commit more often.

2: Descriptive mesages can save a lot of headache later. Easy habit to make, while leaving bad messages is a hard habit to break. Note: convention is to start the message with a singular 1st person verb so that if I ask a commit, "What do you do?", it will respond "Fix a bug...", not "Fixed a bug..." or "Christian broke everything so I'm fixing it".

3: Commits are the building blocks of your repo. If you realize later that you broke something in the month that you added a "whoooole lotta stuff", it will be hard to extract the breaking changes from all the other stuff. This is the hardest of the 3 rules and takes a bit of practice. When in doubt, ask yourself: "Does this commit add/change/fix one thing?" if not, consider splitting it up into 2 (or more) commits.

### The basics: branches
Again with the tree metaphors... Git repos start out with one main **branch** called **master**. Branches are used to split off from the master history for awhile, usually with the eventual goal of **merging** back into master.

Why branch? Say you have a program `code.py` that reads a bunch of numbers from a text file and does some math on them. This code works and you're happy with it, but you want to also be able to read from Excel spreadsheets. You might be worried about breaking your code while you add this new feature. Without Git, you could make a copy of your code called `code_excel.py` and add the functionality. You get it working but you had to change `code.py` a bunch and now you have two different programs to do almost the same thing.

This is where `git branch` comes in. If, instead you did a `git branch import-excel` and switched to the `import-excel` branch, you now have a copy of your whole repository that you can edit to your heart's content without ever breaking the **master** branch functionality. You can even continue to use your perfectly good `code.py` on **master** while you finish up your new feature. When the new feature is ready, you can perform a `git merge` to get your `import-excel` feature into **master**.

The **gitflow** philosophy of branching:
- When working with others, all new features, bug fixes, or other changes should be made on their own **branch**. This allows your collaboratots to review your changes on the branch before they are merged into master to make sure nothing gets broken. It also helps ensure that the **master** branch is always in good working order and usable by you and your collaborators.

## Git on with it
We have some ideas to guide us, so let's practice. 

### Checking if Git is installed
Let's check if Git is installed.
```bash
git --version
#git version 2.17.1
```
If there is a version number, great! Skip to [Configuring your Git](#configuring-your-git).

If there is no version number, you will need to install Git (this requires administrator access). 

In Ubuntu, you can run: 
```bash
apt-get install git
```

For other Linux distributions, find guidance at https://git-scm.com/download/linux.

For Mac, the `git --version` command should have prompted you to install it.

For Windows see [lesson 0](./lessons/lesson0) about using a UNIX based OS. If you are adamant about coding on windows and do not have the Windows Subsytem for Linux, you can use https://gitforwindows.org/. Gti for Windows provides a bash-like shell called *Git BASH* that emulates the standard bash shell and should work the same as we will see in this lesson.

### Configuring your Git
The first thing to do when using git on a new machine is to configure your credentials so that you get credit for your commits. To do this, use the `git config --global` command.
```bash
git config --global user.name "<Your Full Name>"
git config --global user.email "<your.email@somewhere.com>"
```

If you use the email that you used to sign up for GitHub, any commits you make to GitHub repos will automatically be associated with your account.

### Making a local repository from scratch
Create a new directory called `lesson1` and `cd` into it.
```bash
mkdir lesson1
cd lesson1
```

Let's initialize `lesson1/` as a Git repo.
```bash
git init
# Initialized empty Git repository in ~/projects/lesson1/.git/
```

You can check that the `.git` folder was created using `ls -a`.
```bash
ls -a
# .  ..  .git
```

Great! That's all tere is to it. Git will now track all changes in `lesson1/`.

### Making our first commit
Let's make a new file with our bash redirection trick.
```bash
echo 'Hello World' > file1.txt
```

Since Git is tracking this repo, it should have "sensed" the change. You can always check changes with `git status`.
```bash
git status
# On branch master

# No commits yet

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)

#         file1.txt

# nothing added to commit but untracked files present (use "git add" to track)
```

Git status tells us that we have an untracked file, and even tells us that we need to `git add` it in order for it to be committed. Let's add `file1.txt` to the staging area.
```bash
git add file1.txt
git status
# On branch master

# No commits yet

# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)

#         new file:   file1.txt
```

Now `git status` shows a *new file* in the staging area. Everything in the staging area will be committed in the next commit. Let's make our first commit.
```bash
git commit -m "Add hello world to file1.txt"
# [master (root-commit) 8a7625f] Add hello world to file1.txt
#  1 file changed, 1 insertion(+)
#  create mode 100644 file1.txt
```

Great! Let's double check that everything got cleared from the staging area with one more `git status`.
```bash
git status
# On branch master
# nothing to commit, working tree clean
```

To git, your files can be in 3 possible places. The **working directory**, the **staging area**, or in **history** as a commit. You just moved `file1.txt` from your **working directory** to the **staging area** with `git add`, then into **history** with `git commit`. The following figure summarizes how to move between the 3 areas.

![git areas](./data/git_at_a_glance.png)


Notice that we can move back to an old state too. Let's add a toy commit to illustracte this. Like before, make a file, add it to the staging area and then commit it. This time let's use `touch` which is a simple way to make a new empty file.
```bash
touch f2.txt
git add f2.txt
git commit f2.txt -m "Make empty file f2.txt"
```

Let's check that our new commit is in history with the `git log` command.
```bash
git log
# commit 00eb672faf8aa02903de965e5cf91b0feee032c7 (HEAD -> master)
# Author: Christian Tai Udovicic <cj.taiudovicic@gmail.com>
# Date:   Sun Nov 4 22:36:37 2018 -0700

#     Make empty file f2.txt

# commit 8a7625fd943aacc1f9bb722ddffb210990b23d9b
# Author: Christian Tai Udovicic <cj.taiudovicic@gmail.com>
# Date:   Sun Nov 4 21:29:03 2018 -0700

#     Add hello world to file1.txt
```

Git log gives detailed info including the long commit address, the author, the full date and the commit message. This can be overwhelming why dispaying a large number of commits. Let's make `git log` cleaner with the `--oneline` flag.
```bash
git log --oneline
# 00eb672 (HEAD -> master) Make empty file f2.txt
# 8a7625f Add hello world to file1.txt
```

Great! Now that we have our test commit, let's try reverting to our previous commit. Git reset needs a commit number to reset to, in my case it would be **8a7625f** (you can check your git log for your commit number). Alternatively, we can use the shorthand `HEAD~1` or simply `HEAD~` to mean the previous commit (Likewise, `HEAD~2` would be the second last commit, etc.).
```bash
git reset --soft HEAD~
git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)

#         new file:   f2.txt
```

Great, now our last commit (`f2.txt.`) is back in the staging area. Finally we can remove files from the staging area with `git reset`.
```bash
git reset
git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)

#         f2.txt

# nothing added to commit but untracked files present (use "git add" to track)
```

Beware, `git reset --hard` will delete all the changes forever! Use with caution.

To remove untracked files from your working directory, you can simply use `rm`.
```bash
rm f2.txt
git status
# On branch master
# nothing to commit, working tree clean
```

Getting the hang of moving files from the working directory to the staging area and finally into history is the first step to becoming fluent in Git. Don't worry if it's still a little unnatural, we will get lots of practice in the coming weeks!

## Remotes and GitHub
Many git beginners (myself included) confuse **Git** and **GitHub**. Git is the software that has been keeping track of our files so far, while **GitHub** is a website where Git repos are hosted. There are othe. websites that also specialize in hosting git repos (e.g. **GitLab**, **BitBucket**, etc). GitHub is by far the most used and most widely recognized open source platform in world. It is where many useful scientific packages are developed and made available to the community (e.g. astropy, emcee, scikit-learn). Using GitHub for this course will give you some insight into how these packages are developed and will reveal a great researouce for open-source code to use in your research.

### Finding the remote

So far, our `lesson1/` repo only exists locally. This will work fine for keeping track of our changes over time, but what if our hard drive dies or we want to share our code?

This is where the **remote** comes in. The remote tells git where another version of your repository on another computer is located. In our case, our remote will reside on GitHub's servers out in the internet somewhere. You could also use, e.g. an internal lab server as your remote repo, but then you would only have access to it when you were connected to the same network (or through a **vpn**).

To make our first GitHub Repository, first log in to https://github.com. If you are just signing up for GitHub, make sure to update your `git config` with the same email address you use to sign up.

Next make a new repository (either with the button on your profile, or with the little `+` in the upper right).

![new repo](./data/new_repo.png)

Here, you are given some options. You can name the repository `lesson1` and give it a description if you would like. Choose `Private` to keep your practice private. Finally, you can leave the last 3 options blank: no README, no .gitignore, no license (more on these soon).

![create new repo](./data/create_new_repo.png)

You've made a GitHub repository! Right now it's blank, but GitHub offers some suggestions for starting our repository. Since we want our local `lesson1/` to be tracked by GitHub, we will follow the directions under **…or push an existing repository from the command line**.

The first of two commands will set up your GitHub **lesson1** repo to be the standard, or **origin** remote for our local `lesson1/` repo. It will then push the **master** branch to **origin**. The **-u** tells git that **master** should always be pushed to **origin** from now on.
```bash
git remote add origin https://github.com/<your_github_username>/lesson1.git
git push -u origin master
```

You will need to input your GitHub username and password, and if all went well, you should get a message like:
```bash
# To https://github.com/cjtu/lesson1.git
#  * [new branch]      master -> master
# Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Now head back to GitHub and click on the **Code** tab or on **lesson1**.

![code tab](./data/code_tab.png)

Do you see your beautiful `file1.txt`? Congrats on your first GitHub repo!

### Push and Pull

Now that your repository is set up to track at GitHub, we can `push` updates to our code to GitHub at any time. If we are working alone, this can serve as a quick backup, or a way to make our code available to our other machines. If we are working with others, or have a public repository for the community, pushing our code to GitHub is how we will share it with the world.

Pushing is how we will keep our remote repos up to date with our local repos. So it would make sense that `pulling` will update our local repo with changes to our remote repo. Let's give this a shot.

GitHub is pestering me to add a `README` to my repository. Let's indulge it so that there will be a change for us to pull in. From the `Code` tab of your **lesson1** repository on GitHub click on the green `Add README` button, or click `Create New File`.

![add README](./data/add_readme.png)

You will be given a text field to add a README to your project. On GitHub, the README is the first thing a visitor will see when they look at your repository. GitHub also auto-formats your README based on the rules of a simple text mark-up language contrarily named MarkDown. Fun fact: this whole couse is written in MarkDown, and it's super easy to pick up (see [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for a great cheatsheet with all you need to know).

![readme text](./data/readme_text.png)

You can be creative, or here is what I wrote in mine.
```MarkDown
# Welcome to lesson1!

Hello World.

This is my first GitHub repository!

![woohoo](https://media.giphy.com/media/l2JdTAyoFqDY6nEis/giphy.gif)
```

Finally, write a desriptive commit message and click the commit button.

![commit readme](./data/commit_readme.png)

Now we have a commit in our **lesson1** repo on GitHub that is not yet reflected in our local `lesson1` repo.

Let's get our repositories back in sync. From your `lesson1` directory, type the `git pull` command.
```bash
git pull
# Unpacking objects: 100% (3/3), done.
# From https://github.com/cjtu/lesson1
#    8a7625f..b280ade  master     -> origin/master
# Updating 8a7625f..b280ade
# Fast-forward
#  README.md | 7 +++++++
#  1 file changed, 7 insertions(+)
#  create mode 100644 README.md
```

Finally let's verify that everything is in order with `git log`.
```bash
git log --oneline
# b280ade (HEAD -> master, origin/master) Add README.md
# 8a7625f Add hello world to file1.txt
```
Great! The last thing we will do is learn to check out an existing repository on GitHub.

### Cloning and Forking

You can check out your `lesson1` repo at any time from any machine by clicking the green `clone or download` button, and then typing `git clone https://github.com/<user>/lesson1.git`.

![clone lesson1](./data/clone_lesson1.png)

Only you will be able to clone your private repository because you need to supply your GitHub username and password. 

What if you want to clone somebody else's public repository on GitHub, either to use their work or to contribute to their repo?

In this case, we will first need to **fork** the repository on GitHub. This will make a complete copy of the repository under your GitHub profile, and then you can clone into your copy of it and edit at will.

To demonstrate this, head over to the sci_coding repository at https://github.com/cjtu/sci_coding. 

Important: before forking a repository, make sure you check for a [LICENSE](../../LICENSE) file, which should be in the top-level directory. The LICENSE tells you how you may use the contents of a repository and who to cite when using it.

Since open source licenses can be full of legal jargon, https://choosealicense.com is a great resource for choosing or understanding a license. The sci_coding repo is made available through the MIT License. Here is the Choose a License TL;DR (you can read more [here](https://choosealicense.com/licenses/mit/):

![mit](./data/mit.png)

According to the MIT License, anybody can use and distribute this entire course, as long as they cite the authors, Christian Tai Udovicic and Alexandre Boivin. This is great news! We're free to fork.

On the main page of the [sci_coding](https://github.com/cjtu/sci_coding) repository, you should see a **Fork** button in the upper right.

![fork button](./data/fork_button.png)

Click this button to make a copy of the repository. After a few seconds you should end up on a page that looks like the original sci_coding repository, but in the upper left, you will see `<your_user>/sci_coding` and below that, `forked from cjtu/sci_coding`.

Great. Now that you have a fork, you can clone the `sci_coding` repo locally. Again, you can click the `Clone or download` button to get a link to the repository, then in the shell.
```bash
git clone https://github.com/<user>/sci_coding.git
# Cloning into 'sci_coding'...
# remote: Enumerating objects: 69, done.
# remote: Counting objects: 100% (69/69), done.
# remote: Compressing objects: 100% (47/47), done.
# remote: Total 69 (delta 25), reused 56 (delta 16), pack-reused 
# Unpacking objects: 100% (69/69), done.
```

Now you have a copy of the coding course locally! 

## Whew
Now that you know the basics of git, version control, and setting up remotes to GitHub, we're all set to start making reproducible scientific code with Python!

Remember the pre-class homework for next week is [Learn Python](https://www.codecademy.com/learn/learn-python), modules 1-3. 

## Refs
Credits for the commit diagram go to [A Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-en.html) by marklodato on GitHub. The is a great resource for visual learners to visualize how Git works.