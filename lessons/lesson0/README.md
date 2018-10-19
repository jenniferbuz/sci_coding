# Lesson 0

This lesson will help familiarize you with some tools that we will be using throughout the scientific python course!


## Talking to your computer at a low level

If you have mainly used windows your whole life like me, you might get a tightness in your chest every time you see something like this:

![terminal angst](./data/terminal.gif)

Despite huge leaps in graphical user interfaces for computers (Windows, OS X, heck even Ubuntu looks pretty good now), the plain old shell can be our best friend if we can get over the anxiety of using it. Plus it makes you look like a total hacker to anyone who doesn't know how to use it!


### Terminal? Command line? Shell? Bash?

Every click, scroll, and letter typed on your computer gets translated to a rudimentary language of 0s and 1s that your computer can understand. While we won't be learning binary or machine code for this *Python* course, we will learn to talk to the computer on a slightly lower level that we may be used to.

All operating systems come with a way for you to talk to your computer on a lower level. Though it it called different names on different machines, this usually amounts to a text based prompt with a blinking cursor (like the one above). The default prompt to run commands on Windows is called  (intuitively)  the *Command Prompt*. On OS X, the default is the *Terminal*, and on Linux, the default is *Bash*. Unfortunately for us, each of these prompts has slight differences in the commands it recognizes, so if we are on different operating systems, we could quite literally be speaking (typing) different languages.

The flavour of shell that we will use in this course is the Linux one, *Bash* (**B**ourne **A**gain **SH**ell) . My reasoning for this is three-fold. 

1) For historical reasons, Windows is organized fundamentally differently from UNIX based operating systems like Mac and Linux. I would also have to write all file paths with backslashes for Windows "\\" and forward slashes "/" for Mac and Linux (if you look at the code, you will see I had to write two \\ to get one \\ to show up for unrelated reasons and that's a pain).

2) An advantage of UNIX based filesystems is that they handle file permissions *reeeeeally* well. You cannot make a new file, folder or potentially dangerous script without knowing who can see, change or run that file. The notion of privacy and security is baked right into your every file, who knew! (more on permissions later)

3) Because of how light-weight Linux has remained compared with the bloatiness of Windows and OS X (if you've been forced to update recently you know what I mean), Linux it is the default operating system loaded on many servers, superclusters and cloud computing platforms. If you want to run away with what you learn here and start running your code on the cloud, knowing how to navigate in bash is an essential skill.

*Disclaimer*: Most of what we do will also work on OS X because the Terminal and Bash are just different flavours of the standard UNIX *Bourne Shell* (sh). I highly reccommend that you follow along on a Linux system (this course was developed on Ubuntu 16.04) so that everything works out nicely (and because of number 3 above).

### Lament not, ye weary and burdened Windows and Mac users

There are many ways to get access to a Linux environment for this course. If you happen to be in the Edwards Research Group, I suggest using your default operating system to **ssh** into one of the lab machines. This will probably require you to set up a **vpn** (virtual private network) to get access to the lab computer network so that you can "talk" to computers on that network. The advantage of doing this is that you will be able to access the lab computers from anywhere that you have an internet connection (secret advantage: the vpn makes all of your internet usage look like it's coming from the university network. Had trouble getting access to a paper? Start up your vpn and skirt that paywall).  

The ssh (**S**ecure **Sh**ell) command will connect you to a computer on your network and give you a shell that you can use to issue commands that computer. If the computer you ssh is running a flavour of Linux (all of our lab mahcines do), your secure shell will be a **bash** shell. Pretty cool huh?

#### Alternatives to the ssh method:

If you do not have a convenient Linux machine to ssh to, you have a couple options which I will list briefly. 

- Running a *Virtual Machine* (VM) on your computer is one option. 
 - Pros: you have access to your fancy operating system while your Linux machine just runs in a window. 
 - Cons: VM's are a program on a computer, not the *computer* itself. Therefore they are limited resource-wise and can be quite slow unless you have a really powerful computer. Some are also expensive.

- Dual-booting to run two separate operating systems on one computer. 
 - Pros: You get the full Linux experience on your computer (you enter it before Windows/Mac even loads). 
 - Cons: This requires you to split your hard drive in two. If your're low on hard drive space, this may not be feasible. Also, your files on one half cannot talk to the files on the other. Also, though relatively safe, fair warning that any time you mess with your hard drive you run the risk of corrupting all of your data.

- Finding a cloud service to make you a Linux VM.
 - Pros: This is the true Linux exeperience and if something goes wrong, you can nuke the VM and start from scratch. It will be a private computer to ssh to. You can say you do cloud computing like some kind of hacker.
 - Cons: Although shockingly cheap, it generally costs by the hour, and gets more expensive if you want more ram or processing power. Starting one and forgetting it can lead to unexpected monthly bills.

 - Windows only: the Windows Subsystem for Linux (WSL or "Bash on Ubuntu on Windows")
  - Pros: Setup is relatively easy and free. Though it is a separate filesystem, your files can talk to each other.
  - Cons: Though it has come a long way in the past year, certain things *just don't quite work* yet. Due to the differences between Windows and Linux mentioned before, having *anything* UNIX based run on Windows was a monumental task. But certain programs will mysteriously not function as expected, so you don't get a true Linux experience.


## Bash it up

Throughout this course, code you should try will be written in blocks like these:

```bash
echo "Hello World"
```

Did you type it into your bash shell? Seriously try it! Coding is a language and anyone who is bilingual can tell you that only reading will never make you fluent. 

Before we find out where we're going, let's first see where we are (the **#** symbol is a marker that preceeds comments in bash. I will use comments to show my output so that you can compare your result. You don't need to copy the comments into your shell, but you can try it and see what happens!):

```bash
pwd
#/home/ctaiudovicic
```

It turns out I'm in the *home* directory. Each user on a Linux computer has their own home directory, and it can also be abbreviated with the tilde **~** symbol. To make sure we're on the same page, we can use the **cd** (change directory) command to navigate to home (*~*).

```bash
cd ~
pwd
#/home/ctaiudovicic
```

While the home directory will be the start of your personal collection of files, it isn't where the computer starts. All Unix filesystems extend (kind of like the branches of a tree) down from a single **root directory** (get it? root? tree analogies?). The root directory is simply called **/**. Let's go check it out.

```bash
cd /
pwd
#/
```

Okay, so we know we're in root (**/**) but what if we want to know what files and folders root contains? here we can use the **ls** (list) command.

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

Here are all of the files and folders contained in **/**. Many of them are system files that you don't need to worry about. 

Recall the path to your home directory **/home/<your_username>**. Let's see if we can get there from the root directory. First we want to change directory to **home/**.

```bash
cd home # or 'cd home/' works too
```

If we want to check out which other users are on this machine, we can list the contents of the home directory.

```bash
ls
#ctaiudovicic  jbuz
```

Now we're one step away from our home directory.

```bash
cd <your_username>
pwd
#/home/ctaiudovicic
```

Great! We made it back. Now let's check out two shortcuts bash has for navigating, **.** and **..**. Try to cd to **.**.

```bash
cd .
pwd
#/home/ctaiudovicic
```

Were you surprised? The **.** is shorthand for the current directory that we are in. If you change directory to the current directory, you haven't moved!

Now let's try to cd to **..**

```bash
cd ..
pwd
#/home
```

This appears to have moved us back to the **/home** directory. The **..** is shorthand for the parent directory of the diectory you are currently in. Remember the filesystem tree? **..** is a way to move up the branches towards **/**. Now cd **..** once more.

```bash
cd ..
pwd
#/
```

Back at the root directory like expected. What do you think happens if we cd **..** from the root directory?

```bash
cd ..
pwd
#/
```

Since root is the highest level directory, it has no parent directory, so cd **..** kept us here at */*.

Now let's take our handy shortcut back to home.

```bash
cd ~
pwd
#/home/ctaiudovicic
```

If this is your first time on a machine, your home directory might look pretty empty.

```bash
ls
#
```

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

Let's make a new file. A combination of the **echo** (print) command and bash's **>** (redirection) command can do this quite quickly. Let's make a new file *test_file.txt* containing the words *Hello World*.

```bash
echo "Hello world" > test_file.txt
```

We know how to check if the file was created,

```bash
ls
#test_file.txt
```

And we can preview the first few lines of any file with the **less** command.

```bash
less test_file.txt
#
#
#Hello World
#(END)
q
```

Press **q** to exit less. Great! We've now learned to navigate directories, make our own directories and files.

To copy a file, we use the **cp** command. Let's give our copy a creative new name like "test_file2.txt". 

```bash
cp test_file.txt test_file2.txt
ls
#test_file.txt test_file2.txt
```

You can check using **less** that your important file contents got copied over.

```bash
less test_file2.txt
#
#
#Hello World
#(END)
q
```

Let's try to move our new file back to the home directory. The **mv** command works like the copy command, except we specify a new path for it to be moved to. As we know, there are many way to specify the home directory. Try one of the following:

```bash
mv test_file2.txt ~ 
mv test_file2.txt ..
mv test_file2.txt /home/<your_username>
```

To test if we were successful, we *could* **cd** to home and run **ls**. But we can check from right where we are if we supply a path to home to **ls**.

```bash
ls ~
#test test_file2.txt
```

Great! The **mv** command also has another fun trick which is renaming files. To do this, you "move" the file to the same directory, but with a new name.

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

Here, rm is looking out for us in case we accidentally try to delete a directory full of files we may need. To proceed with removing a directory we need to add an *option* to the **rm** command. Options are used to modify the behavious of bash commands. To see what options are available for a given command, we can check out information related to that command by typing **info** followed by the comand.

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

Remember to hit **q** to leave most scary dialogs in the shell. Did you notice the **-d** or **--dir** option? It sounded like the one we need. Both **-d** and **--dir** do the same thing, as do other options that you see listed together. The **-d** is just shorter (because programmers are lazy and typing the 3 extra characters is too much work).

Let's give it a shot.
```bash
rm -d test
ls
#
```

And it's gone! 