""" Exercise 3 : What’s your name ?

Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
"""
my_name = "ahmed"
your_name = input("what is your name ")

# strip() function for remove the space from the user name and the lower() for making the all later lower 
name = your_name.strip().lower()
if name == my_name:
    print("we have the same name hhh")
else :
    print(f"nice to meet you {your_name}")