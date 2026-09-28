"""
Ian Tiggle
Chapter 5
Printing out stages of life using elif statements
"""

age = 18

if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a teenager.")
elif age < 30:
    print("This person is a young adult.")
elif age < 45:
    print("This person is an adult.")
else:
    print("This person is an elder")