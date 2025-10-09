import random

print("")
print("Ok lets play a GAME")
print("")
input()
print("I will think of a 2 digit number and you can try to guess it.")
print("You have 6 chances to guess it")
print("")
input()
print("")
print("So shall we start.")
print("OK now guess the number")

x=random.randint(10,99)
i=1
print(x)
while i < 7:
    guess=int(input())
    if guess == x:
        print("GGs You gueesed it correct.")
        print("Congraulations u won")
        break
    elif guess < x:
        print("Higher")
        print("")
        i += 1
        
    elif guess > x:
        print("Lower")
        print("")
        i += 1
    else:
        print("???")

if guess == x:
    print("")
else:
    print("Sorry You Failed")
