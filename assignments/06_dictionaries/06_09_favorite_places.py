"""
Ian Tiggle
Chapter 6
Looping people's favorite places in a dictionary
"""

favorite_places = {
    "Sarah": ["Paris", "New York", "Tokyo"],
    "Michael": ["Grand Canyon", "Miami Beach"],
    "Lily": ["London", "Rome", "Barcelona"]
}

for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places:")
    for place in places:
        print(f" - {place}")