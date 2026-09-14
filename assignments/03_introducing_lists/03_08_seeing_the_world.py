"""
I am naming places and sorting them
in alphabetical order, reverse,
and reverse alphabetical order.
Ian Tiggle
"""

places = ["Canada", "Japan", "Italy", "Africa", "Mexico"]

print("Original list:")
print(places)

print("\nSorted list (alphabetical order):")
print(sorted(places))

print("\nOriginal list still unchanged:")
print(places)

print("\nSorted list (reverse alphabetical):")
print(sorted(places,reverse=True))

print("\nOriginal list still unchanged:")
print(places)

places.reverse()
print("\nList after reverse():")
print(places)

places.reverse()
print("\nList after second reverse():")
print(places)

places.sort(reverse=True)
print("\nList after sort() (reverse alphabetical):")
print(places)