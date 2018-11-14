# Lesson 2: Python basics
In this lesson we will explore the basics of Python and learn to work in **Jupyter notebooks** (formerly known as **iPython** or *interactive Python* notebooks).

## Why Python?
Python has quickly risen in popularity among programmers and scientists alike. It is a relatively new language compared to heavy-hitters like **C** and **JAVA**, but it will soon be the [third most popular programming language](https://www.tiobe.com/tiobe-index/). One of the main reasons Python has become so popular is that it is *relatively easy to read and learn*. Python was designed to put style and readibility first, making it easier to pick up for beginners. It is also quite intuitive (at least for English speakers), as many programs you write will read almost word-for-word as you would describe them in plain English. This is not to say that learning the ins-and-outs of Python is easy. Like any language, it takes a lot of practice to learn.

Two other reasons we use Python is because it is **free** and **well supported**. A large community has grown around developing excellent **open-source** (free) code for Python. Many well-tested packages for scientific analysis, image processing, and machine learning have been written specifically for Python and are freely available to the public. A good portion of this course will focus on finding, installing, and managing Python packages with Anaconda to take advantage of the huge body of open source code that you apply to your research.



## Jupyter (iPython notebooks)
The **Jupyter Notebook** is a web app that you can use to write, test, and create pretty documents of your code, all from your favorite web browser. At the end of this course, you will write up something to the effect of [this](http://nbviewer.jupyter.org/gist/jhemann/4569783) and post it to GitHub so that anyone can view and reproduce your results.

For now, we'll use a cool website called [mybinder](https://mybinder.org/) that lets you share interactive Jupyter notebooks with others. This is a great way to show off your science analysis and allow anybody to step through each part of your code to reproduce your results.

The first part of this lesson is the quick tutorial on Jupyter notebooks below. Feel free to play around until you are comfortable. 

[Part 1: Jupyter Tutorial](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Fjupyter_tutorial.ipynb)

More documentation on Jupyter notebooks is available [here](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html)

## Making your own Jupyter Notebooks

### Running Jupyter locally with Anaconda installed
Jupyter is installed by default with Anaconda. On your Linux or Mac computer with Anaconda installed, simply type `jupyter notebook` into the shell and wait for it to start running. You will see a bunch of text that looks something like this.
```bash
jupyter notebook
# A bunch of setup lines
[I 11:59:16.597 NotebookApp] The Jupyter Notebook is running at:
http://localhost:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01
```

Open a web browser (the Jupyter team recommends *Mozilla Firefox* or *Google Chrome*) and go to the full url it specifies (including the token). If it prompts you to log in, return to the shell and find the `token`, a random string of characters after `?token=`, and enter it into the password field.

Now you should see the directory where you started the notebook. Jupyter notebooks are saved as `.ipynb`. You can open and edit existing notebooks, or start a new one by clicking `New -> Python 3`.

To stop a Jupyter environment, return to the shell where it is running and type `ctrl+c`. You will then need to confirm by typing `y` when it prompts you.

This is great if you are working on a Linux or Mac with Anaconda installed. If you are working with Anaconda over **ssh**, there are a couple extra steps.

### Configuring Jupyter for ssh
If you are writing your code on a remote ocomputer (with Anaconda installed), we will need a couple additional steps. This part is a little technical, but at the end of it, you will have a nice Jupyter environment set up that will run your code on the remote server.

#### startjupyter
First we need to start Jupyter on the remote server, but we will do this in a particular way. The following command will start Jupyter on a particular `port` on the remote computer that we can then ssh to from our local computer.

On the **remote computer**:
```bash
#!/bin/bash
jupyter notebook --no-browser --port=8080
```

**Note**: Leave this shell running!

#### connectjupyter
Now we need to open a new shell on our **local computer** to connect a local port to the port we opened on the remote computer. This is called **port forwarding**. If you are working on a Mac / Linux computer. If on Windows, you can see a guide on port forwarding with Putty [here](https://www.linode.com/docs/networking/ssh/ssh-connections-using-putty-on-windows/#port-forwarding-ssh-tunnels-with-putty).

In a **new shell** on your **local computer**:
```bash
ssh -v -N -L 8080:localhost:8080 <YOUR_SSH_ID>@<REMOTE_HOST>
```

Now you can head to a local web browser (again, Firefox and Chrome work best), and head to `localhost:8080`. You should see the Jupyter environment that you started on the remote computer! If it asks you to log in, copy the `TOKEN` from the remote shell into the password field. 

### Creating bash scripts to simplify the above
The above two commands are hard to remember and can be confusing since one needs to be run locally and one via ssh. We know from previosu lessons how to make executable bash scripts, so let's make a couple simple scripts that are easier to remember.

#### bash scripting startjupyter
Create a directory in your home directory of the **remote machine** called `bin/`
```bash
mkdir ~/bin
```

Create a file in the  `~/bin` directory called `startjupyter`. Copy the following into it.
```bash
#!/bin/bash
jupyter notebook --no-browser --port=8080
```

Make `startjupyter` executable with `chmod u+x`.
```bash
chmod u+x ~/bin/startjupyter
```

Add the `~/bin` directory to your `PATH` by adding the following to your `.bash_profile`.
```bash
export PATH=$PATH:/home/<your_username>/bin
```

Source your `.bash_profile` so that the change takes effect.
```bash
source ~/.bash_profile
```

Now you can start a Jupyter environment on port 8080 by typing `startjupyter` on your remote machine.

#### bash scripting connectjupyter
Create a file on your **local machine** in the  `/usr/local/bin/` directory called `connectjupyter`. Copy the following into it.
```bash
#!/bin/bash
remoteport=${1:-8080}
localport=${2:-8080}
ssh -v -N -L ${localport}:localhost:${remoteport} <YOUR_SSH_ID>@<REMOTE_HOST>
```

Make `connectjupyter` executable with `chmod u+x`.
```bash
chmod u+x `/usr/local/bin/connectjupyter`
```

Now you can connect to your remote Jupyter environment with the `connectjupyter` command. If for some reason the remote port 8080 was taken, you can specify a remote port with the first option, i.e. `connectjupyter 8081`. If your local port 8080 is taken, you can specify it with the second option, i.e. `connectjupyter 8081 8081`.

Now open up your web browser and head to `localhost:8080` (or whichever localport you specified in `connectjupyter`).

## Finally, the Python Practice
Hopefully you were able to get a Jupyter environment up and running. If not, skip this section and complete today's lesson on mybinder (link below). When you are finished, let me know and I can help get Jupyter set up.

Now we need to get today's lesson onto your computer. We will do this by checking out the most up-to-date version of the [sci_coding](https://github.com/cjtu/sci_coding/) repository.

### Forking the repository
If you did not fork the repository last week, you will need to go to [lesson1](../lesson1) and follow the directions to fork the repository on GitHub and then clone it to your computer.

### Getting your fork up to date
When you fork a repository, you copy it at a specific **commit** or snapshot. If the original repository changes, your fork will get out of sync. A quick Google of "syncing fork GitHub" reveals this tutorial: https://help.github.com/articles/syncing-a-fork/ (when in doubt, Google! Your question has probably been asked before).

Following the directions in the tutorial, we first need to cd to the `sci_coding` directory. 

Then we `git fetch upstream`. This will check the upstream (the original repo) for changes, and then store them on a new branch called `upstream/master`.

Then we need to switch to the `master` branch with `git checkout master`.

Finally, we merge the **upstream changes** into `master` with `git merge upstream/master`. 

The tutorial also notes that this only updates your local repository. To reflect the update in your fork on GitHub, you need to `git push`.

To summarize:

```bash
cd /path/to/local/sci_coding
git fetch upstream
git checkout master
git merge upstream/master
git push
```

Now your fork should be up to date and you should be able to find the `lesson2/data` directory.

Navigate to `sci_coding/lesson2/data` and start a Jupyter environment. Then open up Jupyter in the web browser and select `lesson2.ipynb`. Work through today's lesson in the interactive notebook!

### Mybinder version of part 2 of today's lesson
If you're having trouble getting Jupyter to work, you can complete the rest of today's tutorial online at the link below:

[Part 2: Python Practice](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Flesson2.ipynb).


## That's it!
Once you have completed the two Jupyter tutorials, you are finished for today! If you were unable to get a Jupyter environment running, let me know so I can give you a hand!

Reminder that the pre-class homework for next lesson is Codecademy's [Learn-Python](https://www.codecademy.com/learn/learn-python) modules 4 and 5.
