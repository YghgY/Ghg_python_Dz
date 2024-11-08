num1 = input("Please enter Number1:")
Doing = input("Please enter math work:")
num2 = input("Please enter Number2:")
ned=()
mathUp ={
        '+':(int(num1) + int(num2)),
        "-":(int(num1) - int(num2)),
        "/":(int(num1) / int(num2)),
        "*":(int(num1) * int(num2)),
        "//":(int(num1) // int(num2)),
        "**":(int(num1) ** int(num2))
    }
if int(num1) / int(num2) != 0:
    print(mathUp[Doing])
else:
    print("")
    print("Nope!")
    print("Dont do '/' on Zero")
    #print("(►__◄)")
#Or
if (int(num1) / int(num2)) !=0:
    if Doing == "+":
        print(int(num1) + int(num2))
    elif Doing == "-":
        print(int(num1) - int(num2))
    elif Doing == "/":
        print(int(num1) / int(num2))
    elif Doing == "*":
        print(int(num1) * int(num2))
    elif Doing == "//":
        print(int(num1) // int(num2))
    elif Doing == "**":
        print(int(num1) ** int(num2))
else:
    #print("Nope!")
    #print("Dont do '/' on Zero")
    print("(►__◄)")