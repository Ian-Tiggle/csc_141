"""
Ian Tiggle
Chapter 9
Difficulty 4/10
"""

class Restaurant:
    'Model a restaurant with OOP'
    def __init__(self, restaurant_name, cusine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}.')
        print(f'The price is {self.price_range}.')

    def can_you_take_a_date(self):
        if self.price_range < 50:
            print(f"Don't embarras yourself. It's too sepensive!")
        else:
            print(f'You can afford {self.restaurant_name}.')

cici_place = Restaurant('Cici Shack', 'Soul Food', 'Philadelphia', 50)

cici_place.can_you_take_a_date()