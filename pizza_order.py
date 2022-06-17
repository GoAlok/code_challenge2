"""
    Task -  You got job at python pizza. Your first job is to build an automatic pizza app.
            based on user order, work out their final bill.

                - small: ₹95
                - medium: ₹145
                - large: ₹185

                    - pepperoni for small pizza : +₹2
                    - pepperoni for medium or large pizza : +₹10
                    - extra cheese for any pizza: ₹25
                    
"""

print("Pizza here!")
price = 0
small_pizza_price = 95
medium_pizza_price = 140
large_pizza_price = 185

pepperoni_small = 20 
pepperoni_large = 35

xtra_cheese = 40

size = input("What size pizza do you want? S, M, L: ").capitalize()
add_pepperoni = input("Do you want pepperoni? Y or N: ").capitalize()
extra_cheese = input("Do you want extra cheese? Y or N: ").capitalize()

if size == "S":
    price = small_pizza_price
    if add_pepperoni == "Y":
        price = small_pizza_price + pepperoni_small
    if extra_cheese == "Y":
        price = price + xtra_cheese
    print(price)
elif size == "M":
    price = medium_pizza_price
    if add_pepperoni == "Y":
        price = medium_pizza_price + pepperoni_large
    if extra_cheese == "Y":
        price = price + xtra_cheese
    print(price)
elif size == "L":
    price = large_pizza_price
    if add_pepperoni == "Y":
        price = large_pizza_price + pepperoni_large
    if extra_cheese == "Y":
        price = price + xtra_cheese
    print(price)
else:
    print("Sorry, please choose the valid options. Happy Ordering :)")