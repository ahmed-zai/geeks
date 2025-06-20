"""
 Exercise 3 : Who’s the song producer?

Goal: Create a Song class to represent song lyrics and print them.


Key Python Topics:

    Classes and objects
    Object instantiation
    Methods
    Lists


Instructions:

Create a Song class with a method to print song lyrics line by line.


Step 1: Create the Song Class

    Create a class called Song.
    In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
    Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


Example:

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]




"""
class Song():
    def __init__(self , lyrics):
        self.lyrics = lyrics 
    def sing_me_a_song(self):
         [print(x)  for x in self.lyrics]

list_song = Song ([
    "ti takli ou techarbi wana herat 3eliya ",
     "ya ba3e la betat ou khalaha wta ",
     "lawla te farach la frach ou taneya te sakhan le ma9rage ou talta 3eraftoha lach "
])
list_song.sing_me_a_song()