
print("Welcome to the To-Do List")
input()
print("")
tasks = []
while True:
    print("What Would you like to do:")
    print("Add/View/Remove/Exit")
    print("")
    user_input=input().strip()

    if (user_input == "Add" or user_input == "add"):
        print("So you would like to ADD a new task to the to-do list?")
        print("Y/N")
        x=input().strip()
        if (x=="y" or x=="Y"):
            print("Enter the task:")
            task = input().strip()#removes the extra space
            tasks.append(task)
            print(f"Task added: {task}")
            print("")
        else:
            continue
            print("")



        
    # View tasks    
    elif (user_input == "View" or user_input == "view"):
        print("So you would like to CHECK your to-do list?")
        print("Y/N")
        x=input()
        if (x=="y" or x=="Y"):
            if len(tasks)==0:
               print("LIST IS EMPTY")
               print("")
               
            else:
                print("Your tasks:")
                for i,t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
                    print("")
        else:
            continue
            print("")

            
    elif (user_input == "Remove" or user_input == "remove"):
        print("So you would like to REMOVE a task from the to-do list?")
        print("Y/N")
        x=input()
        if (x=="y" or x=="Y"):
            if len(tasks)==0:
               print("LIST IS EMPTY")
               print("")
               
            else:
                print("")
                print("Press the no. of the task, you would like to remove")
                print("Your tasks:")
                for i,t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
                print("")
                a=int(input())
                tasks.pop(a-1)
                print("")
                print("Task Removed")
                print("")
            
        else:
            continue
            print("")

            
    elif (user_input == "Exit" or user_input == "exit"):
        print("Do you wish to quit the application?")
        print("Y/N")
        x=input()
        if (x=="y" or x=="Y"):
            print("")
            print("Goodbye!")
            break
            
        else:
            continue
            print("")


            
    else:
        print("That is not a feature...Please select again")
        continue
        print("")
