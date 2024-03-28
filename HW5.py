# HW5.py
# Author: Vadym Didukh

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list
fruits = ["apple", "strawberry",  "orange", "grape", "banana"]
print(fruits)
# Question 2: Using the list from question 1, print the first and last element of the list
print(fruits[1])
print(fruits[-1])
# Question 3: Using the list from question 1, print the 3rd element of the list
print(fruits[2])
# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing
print(fruits[0:3])
# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing
print(fruits[-2:])
# Question 6: Using the list from question 1, create a for each loop that prints each element of the list
for fruit in fruits:
    print(fruit)
# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order
for fruit in reversed(fruits):
    print(fruit)
# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)
for index, fruit in enumerate(fruits):
    print("Index:", index, ", Fruit:", fruit)

# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list[1][0])

# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list
# You can not use the reverse() function

def reverse_list(input_list):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)