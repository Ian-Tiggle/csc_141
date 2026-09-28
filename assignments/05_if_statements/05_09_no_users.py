"""
Ian Tiggle
Chapter 5
Removing all the users in a list
"""

usernames = ["admin", "ian", "james", "peter", "brian"]
if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see the status reports?")
        else:
            print(f"Hello {user.title()}, thank you for logging in.")
else:
    print("We need to add some users!")

usernames = []
if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see the status reports?")
        else:
            print(f"Hello {user.title()}, thank you for logging in.")
else:
    print("We need to add some users!")