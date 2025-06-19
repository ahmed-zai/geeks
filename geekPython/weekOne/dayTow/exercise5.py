""" Exercise 5 : Random

Goal: Create a function that generates random numbers and compares them.

Key Python Topics:

    random module
    random.randint() function
    Conditional statements (if, else)


Step 1: Import the random Module

    At the beginning of your script, use import random to access the random number generation functions.


Step 2: Define a Function with a Parameter

    Create a function that accepts a number between 1 and 100 as a parameter.


Step 3: Generate a Random Number

    Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.


Step 4: Compare the Numbers

    If they are the same, print a success message. Otherwise, print a fail message and display both numbers.


Step 5: Call the Function

    Call the function with a number between 1 and 100.


Expected Output:

Success! (if the numbers match)
Fail! Your number: 50, Random number: 23 (if they don't match)


"""
import random

def compareFunction(user_number):
    rand_number = random.randint(1, 100)
    if user_number == rand_number :
        print("success")
    else:
        print(f"your number is {user_number} and the random number is {rand_number}")

     

compareFunction(50)
compareFunction(40)