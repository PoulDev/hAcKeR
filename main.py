import random, sys


def lamer(phrase):
    done = ""
    up = False
    for letter in phrase:
        if up == False:
            up = True
            letter = letter.upper()
        else:
            up = False
        done += letter
    x = ""
    if done.endswith("!"):
        y = ["!", "1"]
        for i in range(random.randint(3, 7)):
            x += y[random.randint(0, 1)]
    return done + x

try:
    lamer(sys.argv[1])
except:
    lamer(input("text ->"))
