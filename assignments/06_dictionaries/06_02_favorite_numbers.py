"""
Ian Tiggle
Chapter 6
Storing people's favorite numbers using dictionaries
"""

favorite_numbers = {
    "Jack": 17,
    "James": 100,
    "Peter": 33,
    "Mike": 23,
    "Dennis": 1738
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")