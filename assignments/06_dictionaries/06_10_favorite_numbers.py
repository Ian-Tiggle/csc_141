"""
Ian Tiggle
Chapter 6
Storing people's favorite numbers using dictionaries while using lists inside the dictionary
"""

favorite_numbers = {
    "Jack": [17, 20, 15],
    "James": [100, 101, 202],
    "Peter": [33, 66, 70],
    "Mike": [23, 46, 72],
    "Dennis": [1738]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")