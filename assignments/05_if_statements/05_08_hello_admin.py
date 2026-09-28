"""
Ian Tiggle
Chapter 5
Making a special greeting for a name in a list
"""

usernames = ["admin", "ian", "james", "peter", "brian"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see the status reports?")
    else:
        print(f"Hello {user.title()}, thank you for logging in.")