#making the lists
available_coffee = ['Capachino', 'Latte', 'Espresso']
available_shots = ['Single shot', 'Double shot', 'Third shot']
available_sizes = ['small', 'medium', 'large']
available_sides = ['biscuits', 'waffles', 'pastry']
side_prices = {'biscuits': 10, 'waffles': 250, 'pastry': 95}
size_prices = {'small': 100, 'medium': 150, 'large': 200}
coffee_prices = {'Capachino': 50, 'Latte': 50, 'Espresso': 50}
shot_prices = {'Single shot':1, 'Double shot': 2, 'Third shot':3}
sub_total = []
final_order = {}
customer_adress = {}


#ordering a coffee
print("Hi welcome to Rownak's coffee")
print("est. yesterday")

order_coffee = True
while order_coffee:    
    print("Please choose a coffee: ")
    print()
    for coffees in available_coffee:
        print(coffees)
        print()
    while True:
        coffee = input("which coffee would you like to order?")
        if coffee in available_coffee:
            print(f"You have ordered a {coffee}.")
            sub_total.append(coffee_prices[coffee])
            break
        if coffee not in available_coffee:
            print(f"I am sorry, we currently do not have {coffee}.")

    #asking for size
    order_size = True
    print("This is the list of available sizes: ")

    for sizes in available_sizes:
        print(sizes)
        print()
    while order_size:
        size = input("Which size would u like?")
        if size in available_sizes:
                final_order.setdefault(coffee, [])
                final_order[coffee].append(size)
                print(f"I have give u a {size}.")
                sub_total.append(size_prices[size])
        break
    if size not in available_sizes:
            print(f"I am sorry, we currently do not have {size}.")



    #asking for shot
    order_shot = True
    print("This is the list of available shots: ")

    for shots in available_shots:
        print(shots)
        print()
    while order_shot:
        shot = input("Which shot would u like?")
        if shot in available_shots:
                final_order.setdefault(coffee, [])
                final_order[coffee].append(shot)
                print(f"I have given u a {shot}.")
                sub_total.append(shot_prices[shot])
        break
    if shot not in available_shots:
            print(f"I am sorry, we currently do not have {shot}.")
#sides
    order_side = True
    print("This is the list of available sides: ")
    for sides in available_sides:
        print(sides)
        print()
    while order_side:
        extra_side = input("Would you like an extra side? yes or no?")
        if extra_side == "yes":
            side = input("Which one would you like to add?")
            if side in available_sides:
                final_order.setdefault(coffee, [])
                final_order[coffee].append(side)
                print(f"I have added {side}.")
                sub_total.append(side_prices[side])
            else:
                print(f"I am sorry, we don't have {side} available.")

        elif extra_side == "no":
            break
    extra_coffee = input("Would you like to order another coffee?")
    if extra_coffee == "no":
        for key, value in final_order.items():
            print(f"\nYou have order a {key} coffee with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_coffee = False
            if order_correct == "no":
                print(final_order)
                add_remove = input("would you like to add or remove? ")
                if add_remove == "remove":
                    remove = input("Which coffee would you like to remove? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "add":
                    check_order = False

#finalizing the order
print(final_order)
print(f"\nYour total order price is: TTAKA {sum(sub_total)}")
print("Please provide us with your name")
customer_adress['name'] = input("what is your name?")
customer_adress['phonenumber'] = input("What is your phonenumber?")


print()
print(f"Thank you for your order {customer_adress['name']}.")
print()
print("pls take a seat")
print(f"and come to the counter after 5mins")
print()
print(f"you can play homemade snake in the meanwhile")
print()
print(f"we will contact you on {customer_adress['phonenumber']} if we cant find u.")   
print()
print(f"if u dont come we're keeping it!!")
print()
print(f"NO REFUNDS!!")