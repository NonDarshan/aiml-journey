# Simple basic Calculator
while True:  
    print("\n")
    print("1. Add" "\n"
    "2. Subtract" "\n"
    "3. Multiply" "\n"
    "4. Divide" "\n"
    "5. Exit")
    print("\n")

    operation = int(input("Enter your choice (1/2/3/4/5): "))

    if operation == 5:
        print("Calculator closed, Bye.")
        break
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("\n")
    if operation == 1:
        print(num1 + num2)          
    elif operation == 2:
        print(num1 - num2)    
    elif operation == 3:
        print(num1 * num2)    
    elif operation == 4:
        if num2 == 0:
            print("Cannot divide by Zero.")
        else:
            print(num1 / num2)    
    else:
        print("Invalid argument.")
