"""
Ian Tiggle
Chapter 4
Printing out my favorite foods and my friend's favorite foods while adding items to the lists of favorite foods.
"""

foods = ["Pepperoni Pizza", "Pancakes", "Yogurt",]

friend_foods = foods[:]

foods.append("BBQ chicken")
friend_foods.append("Pineapples")

print("My favorite foods are:")
for food in foods:
    print(food)

print("\nMy friend's favorite foods are:")
for foods in friend_foods:
    print(food)