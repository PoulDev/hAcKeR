import random, sys


def lamer(phrase):
    done = ""
    for letter in phrase:
        if phrase.index(letter) % 2 == 1:
        	done += letter.upper()
        else:
        	done += letter.lower()
    x = "!"
    if x in done:
        x = ""
        y = ["!", "1"]
        for _ in range(random.randint(3, 15)):
            x += y[random.randint(0, 1)]
    return done.replace("!", x)

if len(sys.argv) > 1:
    lamer = lamer(sys.argv[1])
else:
    lamer = lamer(input("text ->"))

print(lamer)
