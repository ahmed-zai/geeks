"""" 
 Let’s create some personalized shirts !

Goal: Create a function to describe a shirt’s size and message, with default values.

Key Python Topics:

    Functions with parameters and default values
    Keyword arguments


Step 1: Define a Function with Parameters

    Define a function called make_shirt().
    This function should accept two parameters: size and text.


Step 2: Print a Summary Message

    Set up the function to display a sentence summarizing the shirt’s size and message.


Step 3: Call the Function


Step 4: Modify the Function with Default Values

    Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.


Step 5: Call the Function with Default and Custom Values

    Call make_shirt() to make a large shirt with the default message.
    Call make_shirt() to make a medium shirt with the default message.
    Call make_shirt() to make a shirt of any size with a different message.


Step 6 (Bonus): Keyword Arguments

    Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).


Expected Output:

The size of the shirt is large and the text is I love Python.
The size of the shirt is medium and the text is I love Python.
The size of the shirt is small and the text is Custom message.



"""
def make_shirt(size="large", text="I love Python"):
    print(f"the size of the shirt is {size} and the text is {text} ")
make_shirt()
make_shirt("medium")
make_shirt("small", "is a defrent text")