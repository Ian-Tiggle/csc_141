"""
I am creating a list and using each function from this chapter.
Ian Tiggle
"""

languages = ["English", "Spanish", "German", "Japanese", "Dutch"]
print(languages)

languages.append("French")
languages.insert(1, "Russian")

print(languages)

del languages[0]

popped_languages = languages.pop()
print(popped_languages)

languages.remove("Spanish")

print("Alphabetical:", sorted(languages))
print("Reverse alphabetical:", sorted(languages, reverse=True))

languages.reverse()
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(len(languages))