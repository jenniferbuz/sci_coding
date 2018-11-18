# Lesson 3

## Objects
Python is what is called an **object oriented** programming language. This means that everything we make or interact with in Python is an **object**. We already know how to make **String** objects, and today we will learn to make **List** and **Dict** objects. Let's start with the **List**.



Say we want to make a **Person** object to store data about people in Python. Then we would define a **class** called **Person** that represents all data we can store about a given person. Then if we made a particular person, we call that an **instance** of the **Person** class. So:
```Python
class Person:
	"""An onject that stores data about people"""
	# Some implementation details here

person1 = Person()
```

Now `person1` is a given person, or an *instance of the class Person*. Now what makes a given person unique? They could have a *name*, a *date of birth*, a *country of birth*, etc. These would be **attributes** of our object. 
```Python
person1.name = 'Melissa'
person1.dob = 'March 20, 1984'
person.birthplace = 'United States'
```

Let's say there are a couple actions that a Person can can. These woul dbe defined as **methods** in the Person class, and each of these methods can be called on any instance of Person. Methods are called with `()` parentheses. Any variables that are put in the parantheses are called **arguments** of the method.
```Python
person1.walk() # Walk doesn't take any argumemts
person1.talk('Hello') # Talk has one argument, a String to say
```



## Functions


## Lists and Dictionaries


## Jupyter practice

