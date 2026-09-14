"""
I am adding new people to the dinner list. Ian Tiggle
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