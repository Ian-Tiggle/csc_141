"""
Ian Tiggle
Chapter 8
Difficulty 1/10
"""

def describe_city(city, country = 'Romania'):
    print(f'{city} is in {country}')

describe_city('Bucharest', 'Romania')
describe_city('Craiova')
describe_city('Oradea')
describe_city(country = 'Romania', city = 'Bucharest')