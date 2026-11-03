"""
Ian Tiggle
Chapter 8
Difficulty 4/10
"""

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'Ian',
    'Smith',
    school='Boys Latin',
    grade='9th',
    hobby='Programming'
)

print(user_profile)