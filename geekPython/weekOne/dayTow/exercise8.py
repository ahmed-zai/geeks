def pizza_order():
    toppings = []
    base_price = 10
    topping_price = 2.5

    while True:
        topping = input("Enter a pizza topping (type 'quit' to finish): ").strip()
        if topping.lower() == 'quit':
            break
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

    total_cost = base_price + topping_price * len(toppings)

    print("Your pizza toppings are:")
    for t in toppings:
        print(f"- {t}")

    print(f"Total cost of the pizza is: ${total_cost:.2f}")

pizza_order()