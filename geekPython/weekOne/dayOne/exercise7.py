"""  Exercise 7: List Manipulation

Key Python Topics:

    Lists
    List methods: append, remove, insert, count, clear


Instructions:

    You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
    Remove "Banana" from the list.
    Remove "Blueberries" from the list.
    Add "Kiwi" to the end of the list.
    Add "Apples" to the beginning of the list.
    Count how many times "Apples" appear in the list.
    Empty the list.
    Print the final state of the list.


"""
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
Apples_count = basket.count("Apples")
basket.clear()
print(basket)
