# Lesson 0: Bash Basics

This "pre-lesson" will help familiarize you with the shell, a tool that we will use throughout the scientific coding course!


## Talking to your computer at a low level

If you have mainly used a Windows or Mac computer your whole life like me, you might get a tightness in your chest every time you see something like this:

![terminal angst](./data/terminal.gif)

Even though the pretty graphical user interfaces we're used to using are excellent for most things, the plain old shell can be your best friend if we can get over the anxiety of using it. The motivation for making this part of the course is 3-fold:

1) As someone who is interested in scientific coding, you will probably encounter a shell promt at some point (maybe you have already). Might as well get over the shell angst now while we're all learning!

2) Working in the shell makes things like version control with Git much easier (stay tuned until lesson1 for my motivation behind making Git a part of this course). 

3) Using the shell makes you look like a total hacker!


### Terminal? Command line? Shell? Bash?

I've thrown the word shell around a lot, so let's take a quick step back to understand what we'll be doing.

Every click, scroll, and letter typed on your computer gets translated to a basic language of 0s and 1s that your computer can understand. While we won't be learning binary for this course, nor should you ever have to, we will learn to talk to the computer on a slightly lower level that we might be used to.

All operating systems come with a text based prompt that you can use to talk to your computer on a level between clicks and binary. This prompt has different names on different machines. On Windows, it is called the **Command Prompt**, on Macs, it is called the **Terminal**, and on Linux it is called the **shell** or **Bash**. 

Each type of shell has slight differences in its *shell-scripting* language. The one I will use is **bash**, and I recommend that you do the same for the following reasons: 

1) We will be speaking the same language.

2) Windows command prompt is not a powerful when it comes to installing new software and handling file permissions (more on both of these later).

3) Bash is the default shell you will see on many servers, cloud computing platforms, superclusters, etc. Knowing the basics of bash is the first step to running your code on computers many times faster than the one you are reading this on.

*Disclaimer*: Bash and the Mac Terminal are different flavors of the standard UNIX shell, so this lesson is probably also doable on a Mac (but I have not tested this). I highly reccommend that you use a Linux distribution (e.g. Ubuntu) for this course.

If your computer is running Windows or OS X, see below for how to get a bash shell on your computer.

### Lament not, ye weary and burdened Windows and Mac users
There are many ways to get access to a Linux environment for this course. 

#### Edwards group
If you are in the Edwards Research Group, I suggest using a **vpn** to gain access to the computer lab network from your laptop, and then using **ssh** to "talk" to one of the lab computers. This will open a bash shell on your laptop that you will use to run commands on the lab computer. 

A consequence of doing the course this way is that, in less than 6 weeks, you will have a Python environment set up on the speedy lab computers that you can access from the comfort of your own home (or your favorite coffee shop, or anywhere with internet). Also, you couldn't ask for a better way to learn to do "cloud computing", because you will literally be running all of your code on a computer that isn't yours (e.g. *in the cloud*). How exciting!


#### Alternatives to the vpn + ssh method:

If you do not have a convenient Linux machine to ssh to, you have a couple options which I will contrast briefly (but don't take my word for it, you can do your own research too).

| Option                | Pros   | Cons |
| --------------------- | ------ | ----------------------------- |
| Running a *Virtual Machine* (VM) on your computer | You have access to your familiar operating system while your Linux machine just runs in a window. | VM's are limited resource-wise like any other program on your computer, meaning they can be quite slow (depending on your PC). Some are also expensive. |
| Dual-booting your OS (Windows/Mac) and Linux | You get the full Linux experience with your PC's full resources. | This requires you to split your hard drive in two, which may not be feasible if you're low on space. Also, any time you mess with your hard drive you run the risk of corrupting all of your data. |
| Use a cloud service (Google, Amazon, Microsoft) to make you a Linux VM | You can whip up a simple VM for pretty cheap that you can make more powerful as you need it (scalable). | A bit more technical setup than the others. Generally charges by the hour. Starting a VM in the cloud and forgetting it can lead to unexpected monthly bills. |
| *Windows only*: Windows Subsystem for Linux (aka WSL, aka "Bash on Ubuntu on Windows") | Setup is easy and free. You get the best of bash and can still access your Windows files (imposible when using a VM) |Certain things *just don't quite work* yet. Programs are tricked into thinking they are running on Ubuntu, but might malfunction unexpectedly because under the hood it's still Windows. |


## Let's bash it up

Now that we're all on the same page, open up your bash shell and let's practice some basic navigation.

Throughout this course, code you should type yourself will be written in blocks like these (while you can copy and paste these blocks, I encourage typing them out to build some muscle memory):

```bash
echo "Hello World"
```

Did you type it into your bash shell? Seriously try it! Coding is a language and you need to practice it to become fluent.

### Navigation

Before we decide where to go, we can always check where we are with the `pwd` (print working directory) command. 

(Note: the `#` (hash) symbol below denotes a comment in bash. I will use comments to show my output so that you can compare. You don't need to type the comment into your shell, but you can try it and see what happens!):

```bash
pwd
#/home/ctaiudovicic
```

The *path* shows me I am in my *home directory* (or folder). Each user on a Linux computer has their own home directory. The symbol `~` (tilde) is shorthand for your home directory. To make sure we're on the same page, we can use the `cd` (change directory) command to navigate to home (`~`).

```bash
cd ~
pwd
#/home/ctaiudovicic
```

Your computer's file system can be thought of as a tree. We will learn to navigate up and down directories (branches) and make new files (leaves). Your home directory is the trunk from which all your files and folders branch out. This isn't the start of the tree, though. 

All Unix filesystems branch out from a single **root directory** (get it? like tree the root of a tree?). The root directory is simply the `/` at the start of every file path. 

![file_tree, CSE 124 Fall 2017. (c) George Porter 2017](./data/file_tree.png)

Let's go to the root directory.

```bash
cd /
pwd
#/
```

Okay, our path is now `/` so we know we're in root, but what if we want to know what files and folders we can go to from here? Try using the `ls` (list) command.

```bash
ls
#bin             lib         net   srv
#boot            lib64       nfs   sys
#data            local       opt   tmp
#dev             localdata   proc  usr
#etc             lost+found  root  var
#home            media       run   vmlinuz
#initrd.img      misc        sbin  vmlinuz.old
#initrd.img.old  mnt         snap  work
```

Here are the non-hidden files and folders that branch out from root. Many of them are system files that you don't need to worry about. 

Recall the path to your home directory `/home/<your_username>`. Let's see if we can get there from the root directory. First we want to change directory to `/home/`.

```bash
cd home # or 'cd home/' works too
pwd
# /home
```

If we want to check out which other users are on this machine, we can use list to see all of the home directories.

```bash
ls
#ctaiudovicic  jbuz
```

Now we're one step away from our home directory (replace `<your_username>` with your username).

```bash
cd <your_username>
pwd
#/home/ctaiudovicic
```

We made it back home! Now let's check out two shortcuts bash has for navigating, `.` and `..`. Try to change directory to `.`.

```bash
cd .
pwd
#/home/ctaiudovicic
```

Were you surprised you didn't move? The `.` is shorthand for the current directory that we are in. Why would we ever want to do this? Well, we probably wouldn't want to change directory to our current one, but it will be convenient to use `.` to refer to our current path later on.

Now let's try to cd to `..`

```bash
cd ..
pwd
#/home
```

This appears to have moved up one level to the `/home` directory. The `..` is shorthand for the parent directory of the diectory you are currently in. In our tree analogy `..` is a way to move up the branches towards root `/`. Now change directory to `..` once more.

```bash
cd ..
pwd
#/
```

Great! What do you think happens if we cd **..** while we are in the root directory?

```bash
cd ..
pwd
#/
```

Since root is the highest level directory, it has no parent directory, so cd **..** keeps us here at `/`.

Now let's take our handy shortcut back to home and start making our own directories.

```bash
cd ~
pwd
#/home/ctaiudovicic
```

### Making files and directories

If this is your first time on this Linux machine, your home directory might look pretty empty. 

```bash
ls
#
```

There may be some hidden files, though. Let's check with the `-a` option to the list command.

```bash
ls -a
#.bash_profile .bashrc
```

Your `.bashrc` lets you customize your local bash shell (i.e. on your computer), and your `.bash_profile` lets you customize your remote bash shell (i.e. one that you ssh to). We won't worry about them for now.

Let's make a directory that we can practice in. We do this with the **mkdir** (make directory) command. I will call mine "test".

```bash
mkdir test
```

You can check if you were successful with the **ls** command.

```bash
ls
#test
```

Now navigate to your new directory.

```bash
cd test
pwd
#/home/ctaiudovicic/test
```

Now let's make a new file. A combination of the `echo` (print) command and bash's `>` (redirection) command can do this quite quickly. Let's make a new file called `test_file.txt` containing one line with the words `Hello World`.

```bash
echo 'Hello world' > test_file.txt
```

We know how to check if the file was created,

```bash
ls
#test_file.txt
```

And we can quickly view (but not edit) a file with the `less` command.

```bash
less test_file.txt
#
#
#Hello World
#(END)
q
```

Press `q` to exit less. Great! We've now learned to navigate directories, make our own directories and files, and read files, all without leaving the shell.

### Manipulating files

Say we want to duplicate  we use the `cp` command. Let's give our copy a creative new name like `test_file2.txt`. 

```bash
cp test_file.txt test_file2.txt
ls
#test_file.txt test_file2.txt
```

You can check using `less` that your important file contents got copied over too.

```bash
less test_file2.txt
#
#
#Hello World
#(END)
q
```

Let's try to move our new file to our home directory. The `mv` (move) command. As we know, there are many way to specify the home directory. Try one of the following:

```bash
mv test_file2.txt ~ 
mv test_file2.txt ..
mv test_file2.txt /home/<your_username>
```

To test if we were successful, we *could* `cd ~` to go to home and run `ls` to see what is there. But we can also check without changing directories a path to `ls`.

```bash
ls ~
#test test_file2.txt
```

Great! The `mv` command also has another fun trick which is renaming files. To do this, you "move" the file to the same directory, but with a new name. Rename `test_file.txt` to `awesome_file.txt`.

```bash
mv test_file.txt awesome_file.txt
ls
#awesome_file.txt
```

What if we want to delete a file or directory? We do this with the **rm** (remove) command.

```bash
rm awesome_file.txt
ls
#
```

We deleted our file, now let's delete our directory. First navigate up to the parent directory then remove the test directory with **rm**.

```bash
cd ..
rm test/
#rm: cannot remove 'test/': Is a directory
```

Here, rm is looking out for us in case we accidentally try to delete a directory full of files we may need. To proceed with removing a directory we need to add an **option** to the `rm` command. Options are used to modify the behavious of bash commands. To see what options are available, we can use the `info` (information)command.

```bash
info rm
# 11.5 ‘rm’: Remove files or directories
# ... Lots of boring info ...
# '-d'
# '--dir'
#      Remove the listed directories if they are empty.
# ...
q
```

Remember to hit `q` to leave most scary dialogs in the shell. Did you notice the `-d` or `--dir` option? It sounded like the one we need. Both `-d` and `--dir` do the same thing, as do other options that you see listed together. The `-d` is just shorter (because programmers are lazy and typing the 3 extra characters is too much work).

Let's give it a shot.

```bash
rm -d test
ls
#
```

And it's gone! Great, you now know how to move, copy, and delete files and directories. You also know how to get help on any command with `info`. Now let's cover one more important basic shell option.

### Permissions
Each file and folder in a UNIX filesystem has specific perissions defined for who on the system can read, write or execute that file.

To show this, let's make a special type of text file called a **bash script**. A bash script is a text file that you can put bash commands into, and run by *executing* that file. All bash scripts start with a **shebang** (yes that's what it is called) and have a filename ending in `.sh`. Print the shebang ('#!/bin/bash') to a new file called `test_script.sh`. Make sure to use single quotes.

```bash
echo '#!/bin/bash' > test_script.sh
```

We added the shebang, but we haven't added any commands yet. Let's open `test_script.sh` to edit it (there are different programs that can be used for this. I use `vim`, but `emacs` looks more like a regular text editor).

```bash
emacs test_script.sh # or 'vim test_script.sh'
```

In the text editor, start a new line after the shebang and add `echo "Hello World"`.

```bash
"#!/bin/bash"
echo "Hello World"
```

Make sure to save and then quit the text editor. Now let's run our bash script. We do this by specifying the file location with the `.` shorthand we learned earlier.

```bash
./test_script.sh
# -bash: ./test_script.sh: Permission denied
```

What happened? We ran into a permission issue. To diagnose what is going on, let's list the permissions of the files in our directory with `ls -l`.

```bash
ls -l
# -rw-r--r-- 1 ctaiudovicic users  12 Oct 29 13:09 test_script.sh
```

The permissions of your files and folders are shown in the first 10 characters. It may look like gibberish, but we'll break it down.

Char 1: `d` means directory, `-` means file.

Chars 2-10: `rwx` means yes that person has permission to `read/write/execute` and `-` means no they cannot do that action.

![File Permissions in Linux (c) 2017 Clofus innovations](./data/permissions.jpg)

To visualize this in a table:

For our test_script.sh, the first character is `-`, so we know it is a file.

| Type |
| ---- |
| - |

| Who | Read | Write | Execute |
| --- | ---- | ----- | ------- |
| User | r | w | - |
| Group | r | - | - |
| Others | r | - | - |

**User**: you, because you made and own the file.

**Group**: other users on this machine that are lumped into the same group.

**Others**: everyone else that can access this machine, that isn't you and doesn't belong to your group.

So, bringing it back to executing the command in `test_script.sh`, what happened? Notice the permissions `-rw-r--r--`. We can translate this to: the user, group and others (i.e. everyone) has permission to read `test_script.sh`, while only the owner has permission to write (edit) it, and nobody has permission to execute it.

Now let's get to the fun part of giving ourself permission to run our script. We do this with the `chmod` (change mode) command. To specicy who to change permissions for (user / group / others / all) we will use `u/g/o/a`, and to specify which permission to change, we will use `r/w/x`. To add a permission, we use `+`, and to remove a permission, we use `-`.

Let's give (`+`) ourselves (user or `u`) permission to execute (`x`) the file `test_script.sh`.

```bash
chmod u+x test_script.sh
ls -l
#-rwxr--r-- 1 ctaiudovicic users  12 Oct 29 13:09 test_script.sh
```

Notice the `x` in your user permissions? Now try to run the script.

```bash
./test_script.sh
#Hello World
```

There's a whole rabbit hole of permissions you can read about, but the key takeaways are:

- when you make a new file, nobody else can change it unless you give them permission, and not even you can execute it until you give yourself explicit permission
- you can make your own bash scripts executable with `chmod u+x file.sh`
- you don't have to worry about inadvertantly editing or deleting system files or other users' file on your shared computer, *because you don't have permission*

### Wrapping up
I hope this foray into the basics of bash has helped with your aversion to using the shell. We will build on these basics and apply them to actual scientific coding through the next 5 lessons. 

I think a big source of shell anxiety comes from thinking you'll destroy the computer that you are using if you start typing into the black box. Now that you know about permissions, you know literally couldn't erase all the data on the machine if you tried. You can inadvertantly delete all of *your* data (never run (`rm -rf ~`), which is why it is useful to always have a backup and snapshots of your super important files.

How you ask?

Tune in next time when we learn about the power of Git and version control. Don't forget to work through the [Learn Git](https://www.codecademy.com/learn/learn-git) modules before the next class!