# Lesson 2: Python basics
Welcome to the first *real* coding lesson! In this lesson we will explore the basics of Python, as well as learn to work in *interactive Python* or **iPython** notebooks.

## Why Python?
Many programming languages exist, but Python has quickly risen in popularity among programmers and scientists alike. Different sources will cite different reasons why Python continues to grow in popularity and will soon be the [third most popular programming language](https://www.tiobe.com/tiobe-index/), but I'd boil it down to one main reason: it's *relatively easy to learn*. While many programming languages punish you for forgetting strange brackets `{}`, and allow you to get away with ugly code (you can jam 1000 lines of bash into one line and it would work fine), Python was designed to put style and readibility first, making it easier to pick up for beginners. 

Python is also a great first programming language because it is intuitive (for English speakers). Some scripts you write could be read word-for-word as plain-English commands to the computer. This is not to say that learning the ins-and-outs of Python is easy. Like any language, it takes a lot of practice and mistakes to learn. But we use it for this introductory course in part because it is much more accessible than other programming languages for beginners.

The other reason we use Python is because it is free and a large community has grown around developing excellent open-source (free) **packages** for it. So many, in fact, that a good part of this course will be dedicated to finding, installing and managing packages with Anaconda.

## Jupyter (iPython notebooks)
Python differs from some other programming languages in that it is not **compiled**, but **interpreted**. When you write code in **C** or **Java**, that code is first *compiled* (translated into machine code), and then run. On the other hand, a Python program is *interpreted* line by line, completely skipping the compiling step. What does this mean for us?

The fact that Python is interpreted allows us to work with it *interactively*. We can run one line of code, see what happens, and then run another line of code. I nrough terms, this is much harder in C or Java where you would need to run a line of code, compile, check the output, add another line of code, compile, check the output, etc.

To take advantage of this interaction, the *IPython Notebook* was developed. Now called the **Jupyter Notebook**, this tool will allow us to write code, run it, and create pretty documents to share, all from the same place. At the end of this lesson, you will be able to write up something to the effect of [this](http://nbviewer.jupyter.org/gist/jhemann/4569783) and give someone a link to view it.

Starting a Jupyter notebook is simple on your own computer. With Anaconda installed, you simply type `jupyter notebook` and then in a web browser (prefereably *Mozilla Firefox* or *Google Chrome*) head to `localhost:8080`. If you are working over **ssh**, there are a couple extra steps.


### Configuring Jupyter for ssh
If you are connecting to a remote computer (e.g. with **ssh**), we will need to add an additional step. If you have tried to open a browser over ssh or in a virtual machine before, you may have noticed that it is very slow and will lag when typing. This is because the entire view of the reomte computer's screen must be sent over the internet, second by second. We can get around this hitch by using some special options to configure Jupyter, and then using **ssh** to see the output on our local web browser. This part is a little technical, but at the end of it, you will have a nice interface to write and test code on a remote server.


## Patient Python practice prepares proficient Pythonistas
Now that we all have a **Jupyter** environment running in a browser, we can get to practicing some Python.

