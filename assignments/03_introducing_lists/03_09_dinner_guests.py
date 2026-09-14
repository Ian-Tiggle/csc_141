"""
I am counting out how many guests are in my list
Ian Tiggle
"""
guests = ['LeBron', 'Curry', 'Harden', 'Shaq']

for guest in guests:
    print(f'Yo {guest}, I would be honored if you joined me for dinner.')
    print('Good news everyone! I have found a bigger table, so I can invite more people.')
    guests.insert(0, 'Kyrie')
    print(f"I am inviting{len(guests)} people to dinner.")
    guests.insert(2, 'Kevin')
    guests.append('Smith')
    print(f"I am inviting{len(guests)} people to dinner.")
    for guest in guests:
        print(f'Yo {guest}, I would be honored if you joined me for dinner.')
        while len(guests) > 2:
            removed_guest = guests.pop()
            print(f"Sorry, {removed_guest}, the invite you have recieved has been revoked.")
            for guest in guests:
                print(f"{guest}, you're still invited to the dinner.")
                del guests[0]
                del guests[0]
                print(f"I am inviting{len(guests)} people to dinner.")
                print("\nFinal guest list:")
                print(guests)
                print(f"I am inviting{len(guests)} people to dinner.")