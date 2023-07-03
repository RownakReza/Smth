#making the lists
available_pizzas = ['mr.beast golden pizza', 'pollo', 'special rownak ultra combo', 'bolognese', 'vegetarian']
available_toppings = ['mushroom', 'onions', 'green pepper', 'extra cheese']
pizza_prices = {'mr.beast golden pizza': 10000, 'pollo': 10000, 'special rownak ultra combo': 100000, 'bolognese': 100000, 'vegetarian': 10000}
topping_prices = {'mushroom':1, 'onions': 2, 'green pepper':3, 'extra cheese':4}
sub_total = []
final_order = {}
customer_adress = {}


#ordering a pizza
print("Hi, welcome to Rownak's pizza")
order_pizza = True
while order_pizza:    
    print("Please choose a pizza: ")
    print()
    for pizzas in available_pizzas:
        print(pizzas)
        print()
    while True:
        pizza = input("which pizza would you like to order?")
        if pizza in available_pizzas:
            print(f"You have ordered a {pizza}.")
            sub_total.append(pizza_prices[pizza])
            break
        if pizza not in available_pizzas:
            print(f"I am sorry, we currently do not have {pizza}.")

    #asking for extra toppings
    order_topping = True
    print("This is the list of available extra toppings: ")
    for toppings in available_toppings:
        print(toppings)
        print()
    while order_topping:
        extra_topping = input("Would you like an extra topping? y or n?")
        if extra_topping == "y":
            topping = input("Which one would you like to add?")
            if topping in available_toppings:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                print(f"I have added {topping}.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"I am sorry, we don't have {topping} available.")

        elif extra_topping == "n":
            break
    extra_pizza = input("Would you like to order another pizza?")
    if extra_pizza == "n":
        for key, value in final_order.items():
            print(f"\nYou have order a {key} pizza with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? y/n ")
            if order_correct == "y":
                check_order = False
                order_pizza = False
            if order_correct == "n":
                print(final_order)
                add_remove = input("would you like to add or remove? ")
                if add_remove == "remove":
                    remove = input("Which pizza would you like to remove? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "add":
                    check_order = False

#finalizing the order
print(f"\nYour total order price is: ${sum(sub_total)}")
print("ok so this is mr.beast and im paying for the pizza")
print("Enjoy the pizza")
print("and if u haven't subscribe to mr.beast yet")
print("SUBSCRIBE!! OR I TAKE UR PIZZA AWAY")
