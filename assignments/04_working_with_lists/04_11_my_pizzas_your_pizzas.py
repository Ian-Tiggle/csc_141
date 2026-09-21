"""
Ian Tiggle
Chapter 4
Printing out my favorite pizzas and my friend's favorite pizzas while adding items to the lists of our favorite pizzas.
"""

pizzas = ["Pepperoni", "Supreme", "Plain", "Meat Lovers", "Pepperoni & Sausage"]

friend_pizzas = pizzas[:]

pizzas.append("BBQ chicken")
friend_pizzas.append("Hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizzas in friend_pizzas:
    print(pizza)