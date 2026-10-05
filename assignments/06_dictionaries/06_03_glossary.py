"""
Ian Tiggle
Chapter 6
Using Python's dictionary as a dictionary
"""
glossary = {
    "variable": "A name that stores a value which can change.",
    "list": "An order collection of items stored in a singlem variable.",
    "dictionary": "A collection of key-value pairs used to store related items.",
    "loop": "A structure that repeats a block of code multiple times.",
    "conditional": "A statement that runs code only when certain conditions are met."
}

for word, meaning in glossary.items():
    print(f"{word}:\n {meaning}\n")