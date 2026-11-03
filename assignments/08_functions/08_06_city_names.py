"""
Ian Tiggle
Chapter 8
Difficulty 1/10
"""
# 08_06_city_names
def city_country(city, country):
    print(f"{city}, is in {country}")


print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
print(city_country('tokyo', 'japan'))

#08_09_messages
def show_messages(messages):
    for message in messages:
        print(message)


text_messages = [
    'Hello!',
    'How are you?',
    'See you later.',
    'Have a great day!',
    'Good luck!'
]

show_messages(text_messages)

# 08_12_sandwiches
def make_sandwich(*items):
    print("\nMaking a sandwich with:")

    for item in items:
        print(f"- {item}")


make_sandwich('ham', 'cheese')
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich(
    'peanut butter',
    'jelly',
    'banana',
    'honey'
)