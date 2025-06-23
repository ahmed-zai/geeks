"""
Exercise 2: Dogs

Goal: Create a Dog class with methods for barking, running speed, and fighting.


Key Python Topics:

    Classes and objects
    Methods
    Attributes


Instructions:

Step 1: Create the Dog Class

    Create a class called Dog with name, age, and weight attributes.
    Implement a bark() method that returns “ is barking”.
    Implement a run_speed() method that returns weight / age * 10.
    Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.


Step 2: Create Dog Instances

    Create three instances of the Dog class with different names, ages, and weights.


Step 3: Test Dog Methods

    Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.



"""


class Dog:
    def __init__(self, name , age , weight):
        self.name = name 
        self.age = age 
        self.weight = weight 
    def bark(self):
        return f'{self.name} is branking'
    
    def run_speed(self):
        return self.weight / self.age * 10 
    
    def fight(self , other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a draw"
        
dog1 = Dog("Max", 4, 20)
dog2 = Dog("Rocky", 5, 25)

print(dog1.bark())           
print(dog2.bark())          

print(dog1.fight(dog2))      

