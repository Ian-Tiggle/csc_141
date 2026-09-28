"""
Ian Tiggle
Chapter 5
Checking names in a list
"""

current_users = ["Admin", "Ian", "James", "Peter", "Brian"]
new_users = ["john", "james", "ADMIN", "jacob", "steve"]

current_users_lower = [user.lower() for user in current_users]
print(current_users_lower)

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please schoose a different username.")
    else:
        print(f"The username '{new_user}' is available")