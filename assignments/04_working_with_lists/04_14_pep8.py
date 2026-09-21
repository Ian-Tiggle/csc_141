"""
Ian Tiggle
Chapter 4
Rewriting code in PEP 8
Pep 8 is the ideal way to write code in python.
It provides guidelines to keep your code organized.
PEP 8 recommends that you use four spaces for indentatation, instead of using tab.
PEP 8 recommends keeping lines under 79 characters.
PEP 8 recommends that you shouldn't keep blank lines.
"""
# From 04_10
cubes = [number**3 for number in range(1, 11)]
print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[3:6])

print("The last three items in the list are:")
print(cubes[-3:])

# From 04_11

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

# From 04_13

foods = ("pizza", "chicken", "rice", "pasta", "salad")

print("Original menu:")
for food in foods:
    print(food)
    #foods[0] = "hamburger"

foods = ("hamburger", "chicken", "rice", "tacos", "salad")

print("\nRevised menu:")
for food in foods:
    print(food)