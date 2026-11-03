"""
Ian Tiggle
Chapter 8
Difficulty 4/10
"""

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = [
    "Hello!",
    "How are you?",
    "See you later.",
    "Have a great day!",
    "Good luck!"
]

sent_messages = []

# Pass a copy of the list
send_messages(messages[:], sent_messages)

print("\nOriginal messages list:")
print(messages)

print("\nSent messages list:")
print(sent_messages)