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

For now, we'll use a cool website called [mybinder](https://mybinder.org/) that lets you share interactive Jupyter notebooks with others. This is a great way to show off your science analysis in a reproducible way. Head over to
[mybinder jupyter tutorial](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Fjupyter_tutorial.ipynb) to get started with Jupyter notebooks.

## Making your own Jupyter Notebook
Starting a Jupyter notebook is simple on your own computer. With Anaconda installed, you simply type `jupyter notebook` into the shell and then in a web browser (prefereably *Mozilla Firefox* or *Google Chrome*) head to `localhost:8080`. If you are working over **ssh**, there are a couple extra steps.


### Configuring Jupyter for ssh
If you are connecting to a remote computer (e.g. with **ssh**), we will need to add an additional step. If you have tried to open a browser over ssh or in a virtual machine before, you may have noticed that it is very slow and will lag when typing. This is because the entire view of the reomte computer's screen must be sent over the internet, second by second. We can get around this hitch by using some special options to configure Jupyter, and then using **ssh** to see the output on our local web browser. This part is a little technical, but at the end of it, you will have a nice interface to write and test code on a remote server.


## Patient Python practice prepares proficient Pythonistas
Hopefully you were able to get a Jupyter environment up and running. If not let me know after class so that I can help you set it up, but for now you can complete the rest of today's tutorial online [here](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Flesson2.ipynb).

Now that we all have a **Jupyter** environment running in a browser, we can get to practicing some Python. This time the code in the following code blocks should be written in a `code` cell in Jupyter. Remember you can run code by pressing the `>| Run` button.

### Data structures
One of the most important things to learn about a programming language is how it stores data. Data can take many forms (True/False, integer, letters), and each programming language has different **data structures** that can store this data. In science, most of our computations rely on effectively gathering, manipulating and plotting data. Choosing the correct data structure for the job can also improve the speed of our code. Because data structures are so important, we will spend the next couple lessons practicing Python's basic data types.

#### Strings
The pre-class homework should have familiarized you with the **string**, a basic data type in Python. Strings are how we store charaters or text in Python. 

*Note*: While the single quotes `''` and double quotes `""` are interchangeable in Python, it is good *style* to stay consistant in the type of quotes you use to create strings. I use single quotes `''` so that if I need quotations, I can write `'...and he said, "Hello World"'`

#### Booleans


#### if - elif - else (control flow)

