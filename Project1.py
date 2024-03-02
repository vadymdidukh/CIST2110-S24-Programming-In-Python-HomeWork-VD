# Project1.py
# Author: Vadym Didukh


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, the correct answer, and return whether the user was correct.
# an example would be def ask_question(question:str, option_1:str, option_2:str, option_3,:str option_4:str, correct_answer:str)->bool:
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).

question_1 = "What is the capital of France?"
option_1_1, option_1_2, option_1_3, option_1_4 = "Paris", "Berlin", "London", "Rome"
correct_answer_1 = "a"

question_2 = "What is the capital of Ukraine?"
option_2_1, option_2_2, option_2_3, option_2_4 = "Kyiv", "Prague", "Ankara", "Bucharest"
correct_answer_2 = "a"

question_3 = "What is the capital of the United Kingdom?"
option_3_1, option_3_2, option_3_3, option_3_4 = "Manchester", "London", "Liverpool", "Lisbon"
correct_answer_3 = "b"

question_4 = "What is the capital of the United States of America?"
option_4_1, option_4_2, option_4_3, option_4_4 = "New York", "Washington, D.C.", "Miami", "Los Angeles"
correct_answer_4 = "b"

question_5 = "What is the capital of Portugal?"
option_5_1, option_5_2, option_5_3, option_5_4 = "Barcelona", "Porto", "Madrid", "Lisbon"
correct_answer_5 = "d"

score = 0

user_name = input ("What is your name? " )
user = user_name
print("Welcome to the Geography Quiz! " + user + "!\n")

def welcome_message():
    print("Challenge yourself with questions about world capitals and test your knowledge.")
    print("Each correct answer earns you 1 point. Let's get started!\n")
        
def ask_question(question:str, option_a:str, option_b:str, option_c:str, option_d:str, correct_answer:str) -> bool:
    print(question)
    print("a. " + option_a)
    print("b. " + option_b)
    print("c. " + option_c)
    print("d. " + option_d)
        
    global score
    user_answer = input("Chose correct answer ").lower() 
    if user_answer == correct_answer:
        print("Correct! You earned 1 point.\n")
        return True
    else:
        print("Incorrect. The correct answer is " + correct_answer.upper() + ".\n")
        return False

def display_final_score():
    print("Quiz completed! Your total score is: " + str(score))
    print("Thank you for playing the Quiz Game!")

def main():
    welcome_message()
    
    global score
    
    while True:
        user_ans = input("Are you ready to play Geography Quiz? (yes or no?) ")

        if user_ans.lower() == 'yes':
            print("Alright, Let's play! Each correct answer earns you 1 point.\n")

            if ask_question(question_1, option_1_1, option_1_2, option_1_3, option_1_4, correct_answer_1):
                score += 1
            print("After question 1, score is: " + str(score))

            if ask_question(question_2, option_2_1, option_2_2, option_2_3, option_2_4, correct_answer_2):
                score += 1
            print("After question 2, score is: " + str(score))

            if ask_question(question_3, option_3_1, option_3_2, option_3_3, option_3_4, correct_answer_3):
                score += 1
            print("After question 3, score is: " + str(score))

            if ask_question(question_4, option_4_1, option_4_2, option_4_3, option_4_4, correct_answer_4):
                score += 1
            print("After question 4, score is: " + str(score))

            if ask_question(question_5, option_5_1, option_5_2, option_5_3, option_5_4, correct_answer_5):
                score += 1

            display_final_score()

            play_again = input("Do you want to play again? (yes or no) ").lower()
            if play_again != "yes":
                print("Thank you for playing! Your final score is" + score + " points.")
                break
        elif user_ans.lower() == 'no':
            print("Not ready to play? Okay, see ya later!")
            break
        else:
            print("Type yes or no")


if __name__ == "__main__":
    main()    
            
    
