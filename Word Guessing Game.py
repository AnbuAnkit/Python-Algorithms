import random
import re
#print(type("a"))
def nameChecker():
    global name
    name = str(input("Please enter a name:"))
    x = re.search("\ ", name)
    if len(name) < 2:
        print("Name cannot be this small, try somthing else")
        nameChecker()
    elif x != None:
        print("Name cannont cannot spaces... Write a single word.")
        nameChecker()
    else:
        print("You've got 5 chances to guess the correct word! Good luck!")
nameChecker()

name = name.upper()
l = []
r = random.randint(0, len(name) - 1)
c = 4

for i in name:
    l.append(i)

randomLetter = l[r]

def wordGame():
    global c
    global response

    print("Your word =", name)

    response = str(input("Please enter a letter:"))
    response = response.upper()


    if c == 0:
        print("Game over! Better luck next time.")
    elif c == 1:
        print("Last Chance!")
        c -= 1
        wordGame()
    else:
        if response != randomLetter:
            c -= 1
            print("Wrong!")
            wordGame()
        else:
            print("You won! Your answer is correct.")

wordGame()
