"""
Ian Tiggle
Chapter 8
Difficulty 4/10
"""

def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")


make_sandwich('ham', 'cheese')
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')