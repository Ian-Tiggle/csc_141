"""
I am removing people from the dinner list. Ian Tiggle
"""
guests = ['LeBron', 'Curry', 'Harden', 'Shaq']

for guest in guests:
    print(f'Yo {guest}, I would be honored if you joined me for dinner.')
    print('Good news everyone! I have found a bigger table, so I can invite more people.')
    guests.insert(0, 'Kyrie')
    guests.insert(2, 'Kevin')
    guests.append('Smith')
    for guest in guests:
        print(f'Yo {guest}, I would be honored if you joined me for dinner.')
        while len(guests) > 2:
            removed_guest = guests.pop()
            print(f"Sorry, {removed_guest}, the invite you have recieved has been revoked.")
            for guest in guests:
                print(f"{guest}, you're still invited to the dinner.")
                del guests[0]
                del guests[0]
                print("\nFinal guest list:")
                print(guests)