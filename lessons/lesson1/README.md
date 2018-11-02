# Lesson 1

## Downloading and Installing Anaconda

### Downloading with wget

### Installing without permissions?

### Exporting a path in .bashrc or .bash_profile


## Version control

Has one of these happened to you?

- "I accidentally deleted my code and now I'm sad"
- "I changed something in my code and now everything is broken but I can't remember how it was"
- "I don't know if I meant to send my collaborator `code_v3_oct31_2018_A1.py` or `code_v3_oct31_2018_B7.py`"
- "My collaborator changed half of my code, but I've updated it a bunch since I sent it to them 6 months ago and now I don't know how to combine them"


Version control systems were developed to solve the challenges of collaborating and having code that changes over time. Different version control systems differ in the nitty gritty of their inner workings, but they all allow multiple collaborators to work on the same code, and to revert code to old snapshots if something breaks.

### Why bother
If you mostly work on your science and your code by yourself (how??), you might wonder why you would ever need version control. Non-collaboration bonuses:

1) You always have snapshots of your code that you can revert to if something breaks. Also, everything is time-stamped so you can prove you had an idea/analysis first (may not hold up in the court of academia, but can be a fun trick to pull out at conferences).

2) If you host your code somewhere (e.g. GitHub), you always have a backup in case your computer dies (you can also host privately so your precious science doesn't get scooped early - more on this later).

3) You can easily check out code on multiple machines, say, if you're working via ssh on a remote computer or in the cloud. :wink:

4) When it comes time to share your beautiful science results and/or code with the community, *you're already on a platform that is built for this*


## WTG?! (What the Git)
You should have an idea of what Git *does* from the pre-class homework, but what *is* Git? **Git: the software** is a super efficient and popular choice of version control system. But **Git: the philosophy** is a workflow and set of practices about how to develop and share code. We will practice some of the aspects of this philosophy today and over the next 4 lessons.

### The basics: repos
A Git **repository** or **repo** is a directory that is set up to be tracked by Git. Any old directory can be turned into a repository with the `git init` command. This command dumps some files in a hidden `.git` folder, and from then on Git will track all changes to the new repo and its contents.

### The basics: commits
You can think of Git commits as snapshots or checkpoints in the history of your repo. You get to decide how many changes you make in your repository before you make a commit, and you also get to leave a message to descibe those changes.

Take a walk with me to the year 2020 (or <current_year>+2 in you're joining us from the future). You've been tracking your research in a git repo and somebody asks for a function, `awesome_func()` that you remember writing about 2 years ago. The problem is you deleted that function because you didn't need it, but thanks to the magic of git, you have a checkpoint with it somewhere... 

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
3) Make commits atomic 

1: How often depends on your work. If in doubt, commit more often.

2: Descriptive mesages can save a lot of headache later. Easy habit to make, while leaving bad messages is a hard habit to break. Note: convention is to start the message with a singular 1st person verb so that if I ask a commit, "What do you do?", it will respond "Fix a bug...", not "Fixed a bug..." or "Christian broke everything so I'm fixing it".

3: Commits are the building blocks of your repo. If you realize later that you broke something in the month that you added a "whoooole lotta stuff", it will be hard to extract the breaking changes from all the other stuff. This is the hardest of the 3 rules and takes a bit of practice. When in doubt, ask yourself: "Does this commit add/change/fix one thing?" if not, consider splitting it up into 2 (or more) commits.

### The basics: branches
Again with the tree metaphors... Git repos start out with one main **branch** called **master**. Branches are used to split off from the master history for awhile, with the eventual goal of **merging** back into master.

Why branch? Say you have a program `code.py` that reads a bunch of numbers from a text file and does some math on them. This code works and you're happy with it, but you want to also be able to read from Excel spreadsheets. You might be worried about breaking your code while you add this new feature, so you make a copy of your code called `code_excel.py` and add the functionality. You get it working but you had to change `code.py` a bunch and now you have two different programs to do almost the same thing.

This is where `git branch` comes in. If, instead you did a `git branch import-excel` and switched to the `import-excel` branch, you now have a copy of your whole repository that you can edit to your heart's content without ever breaking the **master** branch functionality. If it takes you awhile to make your feature, you can always switch back to **master** and keep using `code.py`. When your feature is ready, you can perform a `git merge` to get your `import-excel` feature into **master**.

Important notes on **Git: the philosophy**:
- When working with others, any experimental new features, bug fixes, or any changes should be made on their own **branch** and later, only once they definitely work and have been reviewed, merged into **master**. Following this philosophy ensures that **master** always works.

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

For Windows see [lesson 0](./lessons/lesson0) about using a UNIX based OS.

### Configuring your Git
The first thing to do when using git on a new machine is to configure your credentials so that all of your commits. To do this, use the `git config --global` command.
```bash
git config --global user.name "<Your Full Name>"
git config --global user.email "<your.email@somewhere.com>"
```

If you use the email that you used to sign up for GitHub, any commits you make to GitHub repos will automatically be associated with your account.

### Make a basic Git Repository



## Remotes and GitHub

