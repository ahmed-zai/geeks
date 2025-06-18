""" Exercise 4 : Tall enough to ride a roller coaster

    Write code that will ask the user for their height in centimeters.
    If they are over 145cm print a message that states they are tall enough to ride.
    If they are not tall enough print a message that says they need to grow some more to ride.
    """


while True :
    user_input = input("enter your input ")
    try :
        height = int(user_input)
        break 
    except ValueError :
        print("not valid number try agin ")
if height >= 145 :
    print(f"your tall {height}cm is enough for ride  ")
else :
    print(f"your tall {height}cm  your tall is not enough for ride ")