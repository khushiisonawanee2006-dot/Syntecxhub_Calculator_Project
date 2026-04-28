#function
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a / b

#loop
while True:
    print("\n-----Calculator menu-----")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. Clear")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
            print("Calculator Cleared")
            continue

    elif choice == "6":
            print("Exiting Calculator")
            break



    elif choice in ["1", "2", "3", "4"]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == "1":
             result = add(num1, num2)
             operator = "+"

        if choice == "2":
             result = add(num1, num2)
             operator = "-"
        
        if choice == "3":
             result = add(num1, num2)
             operator = "*"

        if choice == "4":
             result = add(num1, num2)
             operator = "/"
            
        print(num1, operator, num2, "=", result)

    else:
         print("Invalid choice! please try again.")

   