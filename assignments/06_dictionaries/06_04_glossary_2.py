"""
Ian Tiggle
Chapter 6
Looping items in a dictionary using a loop
"""

glossary = {
    "variable": "A name that stores a value which can change.",
    "list": "An order collection of items stored in a singlem variable.",
    "dictionary": "A collection of key-value pairs used to store related items.",
    "loop": "A structure that repeats a block of code multiple times.",
    "conditional": "A statement that runs code only when certain conditions are met.",
    "function": "A block of reusable code that performs a specific task.",
    "string": "A sequence of characters used to represent text.",
    "integer": "A whole number, postitive or negative, without decimals.",
    "boolean": "A data data type that can be either True or False.",
    "module": "A file containing Python code that can be imported into a program"
}

for word, meaning in glossary.items():
    print(f"{word}:\n {meaning}\n")