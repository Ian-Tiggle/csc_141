"""
Ian Tiggle
Chapter 7
Difficulty 1/10
"""

pizzas = True
while pizzas:
    topping = input("What topping would you like on your pizza?")
    if topping == "quit":
        pizzas = False
    else:
        print(f"We will add {topping} to your pizza.")