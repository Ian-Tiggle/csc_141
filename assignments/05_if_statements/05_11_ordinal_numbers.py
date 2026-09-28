"""
Ian Tiggle
Chapter 5
Printing numbers and their place on a list
"""

numbers = list(range(1, 9 + 1))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")