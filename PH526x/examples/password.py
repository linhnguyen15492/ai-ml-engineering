import random


def password(length):
    pw = str()
    characters = 'abcdef'
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw


print(password(5))
