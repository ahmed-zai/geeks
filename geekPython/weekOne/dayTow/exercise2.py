"""Exercise 2: Cinemax #2

Key Python Topics:

    Looping through dictionaries
    Conditionals
    Calculations


Instructions

Write a program that calculates the total cost of movie tickets for a family based on their ages.

    Family members’ ages are stored in a dictionary.
    The ticket pricing rules are as follows:
        Under 3 years old: Free
        3 to 12 years old: $10
        Over 12 years old: $15


Family Data:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


    Loop through the family dictionary to calculate the total cost.
    Print the ticket price for each family member.
    Print the total cost at the end.


Bonus:

Allow the user to input family members’ names and ages, then calculate the total ticket cost.
"""
family = {}
print("enter your name and age ")
print("enter done if you finished ")

while True :
    name = input("enter the name : ")
    if "done" == name.lower():
        break
    age_input = input("enter you age ")
    if not age_input.isdigit() :
        print("enter corect age ")
        continue
    if int(age_input) <0 :
        print("enter correct age")
        continue
    age = int(age_input)
    family[name]= age


totalPrice = 0 
for name , age in family.items():
    if age < 3 :
        price = 0 
    elif 3 <= age <= 10 :
        price = 10
    else:
        price = 12 
    print(f"{name.title()}: ${price}")
    totalPrice += price

print(f"total cost is ${totalPrice}")

