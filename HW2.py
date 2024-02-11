# HW2.py
# Author: Vadym Didukh


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:
number = float(input("Please enter your age: "))
if number < 13:
    print("You are a child.")
elif number > 12 and number < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")          

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."

# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
for i in range (6):
    for j in range (1, i + 1):
        print(j, end= '')
    print()    
       
# Question 3:
# Write some code that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.

# Hint 1: You will need to use a for loop and a counter variable to keep track of the total sum of the numbers.
# Hint 2: You will need to use an if statement to keep track of the highest and lowest numbers.
total = 0
highest = 0
lowest = 0

for i in range(10):
    number = float(input("Please enter number: "))
    total = total + number
    average = total / 10
    if highest is 0 or number > highest:
        highest = number
    if lowest is 0 or number < lowest:
        lowest = number
print("The highest number is ", highest)
print("The lowest number is", lowest)
print("The average of the numbers is", average)

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement
string = input("Please enter string ")
lower_case = (string.lower())
counter = 0

for char in lower_case:
    
    if char in "aeiou":
      counter += 1      
print("The number of vowels is", counter)        