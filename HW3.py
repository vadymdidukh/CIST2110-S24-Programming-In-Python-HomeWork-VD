# HW3.py
# Author: Vadym Didukh

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.
  
# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
 
def number_squared(num: int) -> int:
    num = int(input("Please enter number: "))
    """Input number and return the number squared
    Args:
        num(int): the number to square
    Returns:
        int: the number squared
        """
    return num**2    
print("Your squared number is: " + str(number_squared(0)))

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
word = input("Please enter string: ")
letter = input("Please enter a letter: ")
number = int(input("Please enter a number: "))
                   
string = word 
index = number
new_character = letter
new_string = string[:index] + string[index:].replace(string[index], new_character, 1)
print(new_string)

# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True

def number_checker(number: int, lower_bound: int, upper_bound: int):
    if lower_bound <= number <= upper_bound:
        return True
    else:
        return False   
number = int(input("Enter number: "))
lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))
result = number_checker(number, lower_bound, upper_bound)
print (result)   
 
# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
   
def greeting(name, age, color):
    return "Hello, my name is " + name + ". I am " + str(age) + " years old. My favorite color is " + color + "."    

name = "Vadym"
age = 35
color = "Blue"      
result = greeting(name, age, color)

print(result)
    
# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4
def user_greeting(name, age, color):  
    return "Hello, my name is " + name + ". I am " + str(age) + " years old. My favorite color is " + color + "."   
name = input("What is your name? ")
age = int(input("What is your age? "))
color = input("What is your favorite color? ")
result2 = user_greeting(name, age, color)
print(result2)

# Question 6:
# import the random module and use it to generate a random number between 1 and 100
import random

def random_number():
    """Returns a random number between 1 and 100
    
    Returns:
        int: random number between 1 and 100
        """
        
    return random.randint(1, 100)

print("The random number is: " + str(random_number()))    

# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
from math import sqrt
def square_root(num: int):
    
    return num**2    
print("Squared root of " + str(16) + " is: " + str(square_root(16)))

# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as system
print("Python version: ", system.version)

# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
from os import getcwd
current_directory = getcwd()
print("Current working directory: ", current_directory)