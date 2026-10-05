"""
Ian Tiggle
Chapter 6
Making multiple dictionaries
"""

pet1 = {
    "animal": "dog",
    "owner": "Jamal"
}

pet2 = {
    "animal": "cat",
    "owner": "Sarah"
}

pet3 = {
    "animal": "gold fish",
    "owner": "Jacob"
}

pet4 = {
    "animal": "turtle",
    "owner": "James"
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print()
    for key, value in pet.items():
        print(f"{key}: {value}")