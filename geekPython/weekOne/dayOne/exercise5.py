"""Exercise 5 : Favorite Numbers

Key Python Topics:

    Sets
    Adding/removing items in a set
    Set concatenation (using union)


Instructions:

    Create a set called my_fav_numbers and populate it with your favorite numbers.
    Add two new numbers to the set.
    Remove the last number you added to the set.
    Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
    Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
        Note: Sets are unordered collections, so ensure no duplicate numbers are added.
"""

my_fav_numbers = {1 , 2 , 3, 4, 5, 6, 7, 8 }
my_fav_numbers.update([9, 10])
my_fav_numbers.remove(10)
friend_fav_numbers = {22, 223 ,3, 2 ,9 }
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

