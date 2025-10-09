import requests
import random
from currency_converter import CurrencyConverter

def calc():
    print("Enter 1st NO.")
    num1=float(input())
    print("Enter 2nd NO.")
    num2=float(input())
    print("Choose an operation (+,-,/,*):")
    op=input()
    if (op=="+"):
        print(num1 + num2)
    elif (op=="-"):
        print(num1 - num2)
    elif (op=="/"):
        if num2 != 0:
            result = num1 / num2
            print(result)
        else:
            print("Error: Cannot divide by zero!")
    elif (op=="*"):
        print(num1 * num2)
    else:
        print("Cant follow simple instructions huh?")

def quiz():
    print("Do you want to play a quiz?")
    print("Y / N")
    choice=input()

    if choice == "Y" or choice == "y":
        print("So i'll ask you few questions and you can give your answer by choosing the correct option number")
        input()
        print("")
        print("ONLY select option letter A/B/C/D for answer")
        input()
        print("1. Which planet is known as the Red Planet?")
        print("A) Venus")
        print("B) Mars")
        print("C) Jupiter")
        print("D) Mercury)")
        ans=input()
        if (ans =="B" or ans=="b"):
                print("Correct")
        else:
                print("Wrong answer dumbass")
                print("")
                
        print("")
        print("2. Who wrote the play Romeo and Juliet?")
        print("A) Charles Dickens")
        print("B) William Shakespeare")
        print("C) Mark Twain")
        print("D) Oscar Wilde")
        ans=input()
        if (ans =="B" or ans=="b"):
                print("Correct")
        else:
                print("Wrong answer again.LMAO youre such an idiot")
        print("")
        print("3. What is the largest ocean in the world?")
        print("A) Indian Ocean")
        print("B) Arctic Ocean")
        print("C) Pacific Ocean")
        print("D) Atlantic Ocean")
        ans=input()
        if (ans =="C" or ans=="c"):
                print("Correct")
        else:
                print(name," Are you dumber than a kindergartener?")
        print("")
        print("4. How many continents are there on Earth?")
        print("A) 5")
        print("B) 6")
        print("C) 7")
        print("D) 8")
        ans=input()
        if (ans =="C" or ans=="c"):
                print("Correct")
        else:
                print(name," You need to go back to school.")



       
    else:
        print("NO? What do you want to do then?")


def joke():
    print("Here is one")
    print("")
        

    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    joke=response.json()
    print(joke["setup"])
    input()
    print(joke["punchline"])

def todo():
    print("Welcome to the To-Do List")
    input()
    print("")
    tasks = []
    while True:
        print("What ya wanna do? ")
        print("Add/View/Remove/Exit")
        print("")
        user_input = input().strip()

        if user_input.lower() == "add":
            print("So you would like to ADD a new task to the to-do list?")
            print("Y/N")
            x = input().strip()
            if x.lower() == "y":
                print("Enter the task:")
                task = input().strip()  # removes the extra space
                tasks.append(task)
                print(f"Task added: {task}")
                print("")
            else:
                print("")
                continue

        elif user_input.lower() == "view":
            print("So you would like to CHECK your to-do list?")
            print("Y/N")
            x = input()
            if x.lower() == "y":
                if len(tasks) == 0:
                    print("LIST IS EMPTY")
                    print("")
                else:
                    print("Your tasks:")
                    for i, t in enumerate(tasks, start=1):
                        print(f"{i}. {t}")
                    print("")
            else:
                print("")
                continue

        elif user_input.lower() == "remove":
            print("So you would like to REMOVE a task from the to-do list?")
            print("Y/N")
            x = input()
            if x.lower() == "y":
                if len(tasks) == 0:
                    print("LIST IS EMPTY")
                    print("")
                else:
                    print("")
                    print("Press the no. of the task you would like to remove")
                    print("Your tasks:")
                    for i, t in enumerate(tasks, start=1):
                        print(f"{i}. {t}")
                    print("")
                    a = int(input())
                    tasks.pop(a - 1)
                    print("")
                    print("Task Removed")
                    print("")
            else:
                print("")
                continue

        elif user_input.lower() == "exit":
            print("Do you wish to quit the application?")
            print("Y/N")
            x = input()
            if x.lower() == "y":
                print("")
                print("Goodbye!")
                break
            else:
                print("")
                continue

        else:
            print("That is not a feature...Please select again")
            print("")
            continue





def random_number_game():
    print("")
    print("Ok lets play a GAME")
    print("")
    input()
    print("I will think of a 2 digit number and you can try to guess it.")
    print("You have 7 chances to guess it")
    print("")
    input()
    print("")
    print("So shall we start.")
    print("OK now guess the number")

    x=random.randint(10,99)
    i=1

    while i < 8:
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

    


def currency():

    c = CurrencyConverter()

    print("Hello")
    print("This is the currency convertor")
    print("")
    input()

    print("Please enter the currency you would want to convert money from:")
    print("")
    print("1. US Dollar (USD)")
    print("2. Euro (EUR)")
    print("3. Japanese Yen (JPY)")
    print("4. British Pound Sterling (GBP)")
    print("5. Swiss Franc (CHF)")
    print("6. Canadian Dollar (CAD)")
    print("7. Australian Dollar (AUD)")
    print("8. Chinese Yuan Renminbi (CNY)")
    print("9. Indian Rupee (INR)")
    print("10. Singapore Dollar (SGD)")


    currencies = [
        "US Dollar (USD)",
        "Euro (EUR)",
        "Japanese Yen (JPY)",
        "British Pound Sterling (GBP)",
        "Swiss Franc (CHF)",
        "Canadian Dollar (CAD)",
        "Australian Dollar (AUD)",
        "Chinese Yuan Renminbi (CNY)",
        "Indian Rupee (INR)",
        "Singapore Dollar (SGD)"
    ]

    curr_code = [
        "USD",
        "EUR",
        "JPY",
        "GBP",
        "CHF",
        "CAD",
        "AUD",
        "CNY",
        "INR",
        "SGD"
    ]


    choice_from= int(input("Enter your currency(1-10): "))


    choice_to=int(input("Enter Currency you want to convert into(1-10): "))

    print("")
    print("")

    print("Enter the amount you want to convert from: ")
    print( f"{currencies[choice_from - 1]}", "---TO--->", f"{currencies[choice_to - 1]}")
    amt=int(input())


    choice_from= f"{curr_code[choice_from - 1]}"
    choice_to=f"{curr_code[choice_to - 1]}"
    x=c.convert(amt,choice_from, choice_to)
    x=round(x, 4)
    print(x)










input()
print("Hello, nice to meet you.")

print("So Uhh....Do you mind telling your name?")


name=input()
print("So",name,".  How are you?")
feel=input()
print(feel,"  I see. So let me introduce myself im MISKI and im here to waste your time by talking this meaningless talk.")

#print("Please share your Credit Card no. to continue this conversation")

#x=input()
#if x.isdigit():
#    print("... did you literally give me your credit card no?")
#else:
#    print("ok im not stupid")






    
print("------------------------------------------")
print("")
print("Ok lets get real")
print("")
print("What fuction of mine do you wish to use?")
print("")
print("")
print("1. Calculator")
print("2. Quiz")
print("3. Joke bot")
print("4. To-Do List")
print("5. Number Guessing Game")
print("6. Currency Convertor")
choice=int(input())
if choice == 1:
    calc()
elif choice == 2:
    quiz()
elif choice == 3:
    joke()
elif choice == 4:
    todo()
elif choice == 5:
    random_number_game()
elif choice == 6:
    currency()
else:
    print("Huh?")



