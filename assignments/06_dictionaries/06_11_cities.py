"""
Ian Tiggle
Chapter 6
Printing facts about citites using dictionaries
"""

cities = {
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "Known for the Eiffel Tower and world-class art museums."
    },
    "tokyo": {
        "country": "japan",
        "population": "13.9 million",
        "fact": "One of the most technologically advanced cities in the world."
    },
    "new york": {
        "country": "united states",
        "population": "8.3 million",
        "fact": "Home to the Statue of Liberty and Times Square."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")