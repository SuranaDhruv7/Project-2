print("Welcome to the Pattern Generator and Number Analyzer !\n ")
is_on= True
while is_on :
    choice=int(input("Select an option:\n 1. Generate a Pattern\n 2. Analyze a Range of Numbers\n 3. Exit\n Enter your choice: "))
    if choice == 1:
        pattern_type=int(input("\nChoose a pattern type:\n1. Right-angled Triangle\n 2. Pyramid\n3. Left-angled Triangle\n Enter your choice:"))
        c=int(input("Enter the number of rows for the pattern: "))
        if pattern_type==1:
            for i in range(1, c+1):
                for j in range(1, i+1):
                    print("*", end="", sep=" ")
                print()
        elif pattern_type==2:
            for i in range(1, c+1):
                for k in range(c,i,-1):
                    print(" ",end="",sep="")
                for j in range(1, i+1):
                        print("*   ", end="", sep=" ")
                print()
        elif pattern_type==3:
            for i in range(1, c+1):
                for k in range(c,i,-1):
                    print(" ",end="",sep="")
                for j in range(1, i+1):
                    print("*", end="", sep=" ")
                print()
    elif choice == 2:
        d=int(input("Enter the start of the range: "))
        e=int(input("Enter the end of the range: "))
        total = 0
        for i in range(d,e+1):
            if i%2==0:
                print(i,"Number is even")
            else:
                print(i,"Number is odd")
            total= total+i
        print("Sum of all number from 10 to 15 is: ", total)
    elif choice == 3:
        print("\n Exiting the program. GOODBYE! ")
        is_on= False
    else:
        print("\n You have entered the wrong input.")
        is_on= False
