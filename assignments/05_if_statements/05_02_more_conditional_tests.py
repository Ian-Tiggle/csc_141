"""
Ian Tiggle
Chapter 5
Testing more conditional statements
"""

character = "hulk"

print(character == "hulk")
print(character == "hawkeye")
print(character != "black widow")
print(character != "hulk")

age = 18

print(age == 18)
print(age == 21)

print(age != 21)
print(age != 18)

print(age > 17)
print(age > 20)

print(age < 20)
print(age < 17)

print(age >= 18)
print(age >= 20)

print(age <= 20)
print(age <= 17)

print(age >= 18 and age < 21)
print(age >=18 and age > 21)

print(age == 18 or age == 19)
print(age == 20 or age == 21)

foods = ["pizza", "chicken", "apples"]

print("pizza" in foods)
print("meatball" in foods)

print("meatball" not in foods)
print("pizza" not in foods)