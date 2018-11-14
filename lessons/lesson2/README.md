# Lesson 2: Python basics
In this lesson we will explore the basics of Python, as well as learn to work in **Jupyter notebooks** (formerly known as *interactive Python* or **iPython** notebooks).

## Why Python?
Python has quickly risen in popularity among programmers and scientists alike. It is a relatively new language compared to heavy-hitters like **C** and **JAVA**, but it will soon be the [third most popular programming language](https://www.tiobe.com/tiobe-index/). One of the main reasons Python has become so popular is that it is *relatively easy to read and learn*. Python was designed to put style and readibility first, making it easier to pick up for beginners. It is also quite intuitive (at least for English speakers), as many programs you write will read almost word-for-word as you would describe them in plain English. This is not to say that learning the ins-and-outs of Python is easy. Like any language, it takes a lot of practice and mistakes to learn.

Other reasons we use Python is because it is free and well supported. A large community has grown around developing excellent open-source (free) code for Python. Many well-tested packages for scientific analysis, image processing, and machine learning have been written specifically for Python and are freely available to the public. A good portion of this course will focus on finding, installing, and managing Python packages with Anaconda to take advantage of the huge body of open source code that you can use for your research.


## Jupyter (iPython notebooks)
A **Jupyter Notebook** is a very cool tool that you can use to write, test, and create pretty documents of your code, all from your favorite web browser. At the end of this course, you will write up something to the effect of [this](http://nbviewer.jupyter.org/gist/jhemann/4569783) and post it to GitHub so that anyoe can view and reproduce your results.

For now, we'll use a cool website called [mybinder](https://mybinder.org/) that lets you share interactive Jupyter notebooks with others. This is a great way to show off your science analysis and allow anybody to step through each part of your code to reproduce your results.

The first part of this lesson is the following quick tutorial on Jupyter notebooks: Feel free to play around until you are comfortable. More documentation is available [here](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html)

[Part 1: Jupyter Tutorial](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Fjupyter_tutorial.ipynb)


## Making your own Jupyter Notebook

### Running Jupyter locally with Anaconda installed
Starting a Jupyter notebook is simple on your own computer. With Anaconda installed, you simply type `jupyter notebook` into the shell and then in a web browser (prefereably *Mozilla Firefox* or *Google Chrome*) head to `localhost:8080`. If the Jupyter environment prompts you to log in, find the `TOKEN` in the shell where you started the Jupyter notebook and copy/paste it into the password field. 

To stop a Jupyter environment, type `ctrl+c` into the shell, then type `y` when it prompts you.

If you are working over **ssh**, there are a couple extra steps.

### Configuring Jupyter for ssh
If you are writing your code on a remote ocomputer (with Anaconda installed), we will need a couple additional steps. This part is a little technical, but at the end of it, you will have a nice Jupyter environment set up that will run your code on the remote server.

#### startjupyter
First we need to start Jupyter on the remote server, but we will do this in a particular way. The following command will start Jupyter on a particular `port` on the remote computer that we can then ssh to from our local computer.
```bash
#!/bin/bash
jupyter notebook --no-browser --port=8080'
```

#### connectjupyter
Now we need to ssh to the port that we started Jupyter on, and tell our local computer which local port we will go to in order to see the remote port. This is called **port forwarding**. If you have a UNIX shell / Terminal, run the command below. If on Windows, you can see a guide on port forwarding with Putty [here](https://www.linode.com/docs/networking/ssh/ssh-connections-using-putty-on-windows/#port-forwarding-ssh-tunnels-with-putty).
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
jupyter notebook --no-browser --port=8080'
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

Make `startjupyter` executable with `chmod u+x`.
```bash
chmod u+x `/usr/local/bin/startjupyter`
```

Now you can connect to your remote Jupyter environment with the `connectjupyter` command. If for some reason the remote port 8080 was taken, you can specify a remote port with te first option, i.e. `connectjupyter -8081`. If your local port 8080 is taken, you can specify it with the second option, i.e. `connectjupyter -8081 -8081`.

Now open up your web browser and head to `localhost:8080` (or whichever localport you specified in `connectjupyter`).

## Python Practice
Hopefully you were able to get a Jupyter environment up and running (if not let me know so that I can update the instructions above). If you're having trouble, you can complete the rest of today's tutorial online at the link below:

[Part 2: Python Practice](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Flesson2.ipynb).


## That's it!
Once you have completed the two Jupyter tutorials, you are finished for today! If you were unable to get a Jupyter environment running, let me know and I can give you a hand!

Reminder that the pre-class homework for next lesson is Codecademy's [Learn-Python](https://www.codecademy.com/learn/learn-python) modules 4 and 5.
