# HW4.py
# Author: Vadym Didukh

### README
# This file contains buggy functions that you need to fix.
# There are 10 buggy functions in total.
# run test.py to see which functions are buggy and what the expected output is.
# remember you can run test.py with the -v flag to see more details about the tests.
# also remember that you can run a specific test by specifying the test name after the -k flag.
# you should not change the test.py file.

# Each function has a comment above it that describes what the function should do.
# Answer each question asking where the bug is in the buggy function.
# Provide your answer as what line the bug is on and what the bug is.
# For example, if the bug is on line 5 and the bug is that the function is missing a colon, you would write:
# 5: Missing colon
# After you fix the function, you should run test.py to make sure that the function is fixed.


def add(a: float, b: float) -> float:
    """Add two numbers together

    Args:
        a (float): number to add
        b (float): number to add

    Returns:
        float: the sum of a and b
    """
    return a + b


# Where is the bug in the buggy function?
# A: the return has a - b instead of a + b on line 30


def subtract(a: float, b: float) -> float:
    """Subtract two numbers

    Args:
        a (float): number to subtract from
        b (float): number to subtract

    Returns:
        float: the difference of a and b
    """
    return a - b


# Where is the bug in the buggy function?
# A: the return has a + b instead of a - b on line 47


def divide(a, b):
    """Divide two numbers

    Args:
        a (float): number to divide
        b (float): number to divide by

    Returns:
        float: the quotient of a and b
    """
    return a / b


# Where is the bug in the buggy function?
# A: the return has a * b instead of a / b on line 64


def multiply(a: float, b: float) -> float:
    """Multiply two numbers

    Args:
        a (float): number to multiply
        b (float): number to multiply by

    Returns:
        float: the product of a and b
    """
    return a * b


# Where is the bug in the buggy function?
# A: the return has a / b instead of a * b on line 81


def greet(name: str) -> str:
    """Greet a person

    Args:
        name (str): name of the person to greet

    Returns:
        _type_: the greeting message
    """
    return "Hello, " + name + "!"


# Where is the bug in the buggy function?
# A: typo in word "Hello" on line 97


def square(num: int) -> int:
    """Square a number

    Args:
        num (int): number to square

    Returns:
        int: the square of the number
    """
    return num ** 2


# Where is the bug in the buggy function?
# A: the return has num + num instead of num ** 2 on line 113


def is_even(num: int) -> bool:
    """Check if a number is even

    Args:
        num (int): number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return num % 2 == 0


# Where is the bug in the buggy function?
# A: return has num % 2 == 1 instead of num % 2 == 0


def grade_calculator(score: float) -> str:
    """Calculate the grade based on the score

    Args:
        score (float): score to calculate the grade for

    Returns:
        str: the grade for the score
    """
    if  90 <= score and score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid Score"


# Where is the bug in the buggy function?
# A: missing "and score" in if statement and instead of <79 should be <=79 on line 149


def speed_check(speed: float) -> str:
    """Check if the speed is within the speed limit

    Args:
        speed (float): speed to check

    Returns:
        str: the speed check result
    """
    # Assuming general speed limits: min: 20, max: 70 (in mph)
    if speed <= 20:
        return "Too slow"
    elif 20 <= speed <= 70:
        return "Within limit"
    elif speed > 70:
        return "Over speed limit"
    else:
        return "Unknown"


# Where is the bug in the buggy function?
# A: line 175 need to change max speed limit from 60 to 70


def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year

    Args:
        year (int): year to check

    Returns:
        bool: True if the year is a leap year, False otherwise"""
        
    

# Where is the bug in the buggy function?
# A: set up the conditions in the right order for checking leap years, starting with 400, then 100, and 4.
# and changed bool in line 204 from True to False.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def main():
    print(is_leap_year(1900))


if __name__ == "__main__":
    main()
