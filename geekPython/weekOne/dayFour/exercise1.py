

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} "

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Saimese(Cat):
     def __init__(self, name , age ):
         super().__init__(name , age )

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(f"{animal.walk()} is wlaking ")

bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Misty", 4)
siamese_obj = Saimese("Luna", 2)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)

sara_pets.walk()