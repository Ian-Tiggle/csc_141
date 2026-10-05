"""
Ian Tiggle
Chapter 6
Storing people's information in a dictionary and looping them
"""

person1 = {
    "first_name": "Ian",
    "last_name": "Tiggle",
    "age": 18,
    "city": "Philadelphia"
}

person2 = {
    "first_name": "James",
    "last_name": "Baldwin",
    "age": 63,
    "city": "New York"
}

person3 = {
    "first_name": "Terry",
    "last_name": "Crews",
    "age": 58,
    "city": "Michigan"
}

people = [person1, person2, person3]

for person in people:
    print()
    for key, value in person.items():
        print(f"{key}: {value}")