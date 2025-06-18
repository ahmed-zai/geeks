"""Tuple

Key Python Topics:

    Tuples (immutability)


Instructions:

    Given a tuple of integers, try to add more integers to the tuple.
    Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

"""
Tuple = (1, 2 , 22 )
Tuple_list = list(Tuple)
Tuple_list.extend([3, 21])
Tuple = tuple(Tuple_list)
print(Tuple)