"""
Exercise 2 : Dogs

Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.


Key Python Topics:

    Classes and objects
    Object instantiation
    Methods
    Attributes
    Conditional statements (if)


Instructions:

Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.


Step 1: Create the Dog Class

    Create a class called Dog.
    In the __init__ method, take name and height as parameters and create corresponding attributes.
    Create a bark() method that prints “ goes woof!”.
    Create a jump() method that prints “ jumps cm high!”, where x is height * 2.


Step 2: Create Dog Objects

    Create davids_dog and sarahs_dog objects with their respective names and heights.


Step 3: Print Dog Details and Call Methods

    Print the name and height of each dog.
    Call the bark() and jump() methods for each dog.


Step 4: Compare Dog Sizes

"""
class Dog:
    def  __init__(self , name , height):
        self.name = name 
        self.height = height 

    def brak(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        Jump = self.height * 2 
        print(f"{self.height} jumps { Jump} cm high ")


    
dog1 = Dog("bob", 9)
dog2 = Dog("soone", 12)
dog3 = Dog("messi", 13)
dog4 = Dog ("nataniaho", 32)

print(f"the name of dog is {dog1.name} and it height is {dog1.height}")
dog1.brak()
dog1.jump()
print(f"the name of dog is {dog2.name} and it height is {dog2.height}")
dog2.brak()
dog2.jump()
