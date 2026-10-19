"""
Ian Tiggle
Chapter 7
Difficulty 2/10
"""

sandwich_orders = ["tuna", "pastrami", "ham", "veggie", "turkey"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")