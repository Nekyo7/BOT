import sys
def loda():
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

print("Do you want a Calc?")
x=input()
if x=="y":
    loda()
else:
    sys.exit()
