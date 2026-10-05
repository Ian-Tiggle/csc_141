"""
Ian Tiggle
Chapter 6
Extending program 06_11_cities
"""

cities = {
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "Known for the Eiffel Tower and world-class art museums.",
        "famous_foods": ["croissants", "macarons", "baguettes"],
        "founded": 300
    },
    "tokyo": {
        "country": "japan",
        "population": "13.9 million",
        "fact": "One of the most technologically advanced cities in the world.",
        "famous_foods": ["ramen", "sushi", "tempura"],
        "founded": 1603
    },
    "new york": {
        "country": "united states",
        "population": "8.3 million",
        "fact": "Home to the Statue of Liberty and Times Square.",
        "famous_foods": ["pizza", "bagels", "hot dogs"],
        "founded": 1624
    }
}

for city, info in cities.items():
    print(f"\n=== {city.title()} ===")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Founded: {info['founded']}")
    print(f"Fact: {info['fact']}")
    print("Famous Foods:")
    for food in info["famous_foods"]:
        print(f"  - {food}")