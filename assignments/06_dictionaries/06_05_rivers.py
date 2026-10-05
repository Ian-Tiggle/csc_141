"""
Ian Tiggle
Chapter 6
Making a dictionary containing rivers
"""

rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.\n")

print("Rivers in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nCountries in the dictionary:")
for country in rivers.values():
    print(country.title())