"""
Ian Tiggle
Chapter 6
Looping people through a dictionary and a list
"""

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

people_to_poll = ["jen", "mike", "sarah", "anna", "phil", "john"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for respoding to the poll")
    else:
        print(f"{person.title()}, please take the favorrite languages poll.")