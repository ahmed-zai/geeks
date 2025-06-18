"""Exercise 1: Converting Lists into Dictionaries

Key Python Topics:

    Creating dictionaries
    Zip function or dictionary comprehension


Instructions

You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.


Lists:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


Expected Output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
""" 
results = {}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for i in range(len(keys)):
    results[keys[i]] = values [i] 
print(results)