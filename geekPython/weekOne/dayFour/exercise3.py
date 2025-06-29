"""
Exercise 3: Dogs Domesticated

Goal: Create a PetDog class that inherits from Dog and adds training and tricks.


Key Python Topics:

    Inheritance
    super() function
    *args
    Random module


Instructions:

Step 1: Import the Dog Class

    In a new Python file, import the Dog class from the previous exercise.


Step 2: Create the PetDog Class

    Create a class called PetDog that inherits from the Dog class.
    Add a trained attribute to the __init__ method, with a default value of False.
    trained means that the dog is trained to do some tricks.
    Implement a train() method that prints the output of bark() and sets trained to True.
    Implement a play(*args) method that prints “ all play together”.
    *args on this method is a list of dog instances.
    Implement a do_a_trick() method that prints a random trick if trained is True.
    Use this list for the ramdom tricks:
    tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
    Choose a rendom index from it each time the method is called.


Step 3: Test PetDog Methods

    Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.


Example:

# In a new file
# import the Dog class

class PetDog(Dog):
    def __init__(self, name, age, weight): <mark> no need to put the details in the function, you are giving the solution</mark>
        super().__init__(name, age, weight)
        self.trained = False

    def train(self): <mark> no need to put the details in the function, you are giving the solution</mark>
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # ... code to print play message ...

    def do_a_trick(self): <mark> no need to put the details in the function, you are giving the solution</mark>
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

"""
from exercise2 import Dog 
import random 


class PetDog(Dog):
    def __init__(self, name, age, weight): 
        super().__init__(name, age, weight)
        self.trained = False
    def train(self): 
        print(self.bark())
        self.trained = True

    def play(self, *args):
        self.dogs = args 
        print("all play together ")
        [print(dog.bark()) for dog in self.dogs]

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll!",
                f"{self.name} stands on two legs!",
                f"{self.name} shakes your hand!",
                f"{self.name} plays dead!"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} hasn't been trained yet.")

dog = PetDog("rex", 2, 20)   
dog.train()


dog.do_a_trick() 


    
