import random

# This is another file
k = random.randint(1, 200)


def rate_number(x):
    if x > 180:
        print("Wow surprising")
    elif x < 20:
        print("Damn, so small")
    else:
        print("quite average")

rate_number(k)
