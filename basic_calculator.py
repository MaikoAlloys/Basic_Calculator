def add(a,b):
    answer=a+b
    print(f"Sum of {a} and {b} is {answer}")
    return answer

def  sub(a,b):
    answer=a-b
    print(f"The difference of {a} and {b} is {answer}")
    return answer

def mult(a,b):
    answer=a*b
    print(f"The multiplication of {a} and {b} is {answer}")
    return answer

def div(a,b):
    answer=a/b
    print(f"The division of {a} and {b} is {answer}")
    return answer

while True:
    print("Select the operation you want to perform")
    print("1.Sum")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice=int(input("Enter your choice 1,2,3 or 4 to proceed: "))

    if choice==1:
        print("You selected addition")
        a = int(input("Enter Value1: "))
        b = int(input("Enter value2: "))
        add(a, b)

    elif choice==2:
        print("You selected subtraction")
        a = int(input("Enter Value1: "))
        b = int(input("Enter value2: "))
        sub(a,b)

    elif choice==3:
        print("You selected multiplication")
        a = int(input("Enter Value1: "))
        b = int(input("Enter value2: "))
        mult(a,b)

    elif choice==4:
        print("You selected division")
        a = int(input("Enter Value1: "))
        b = int(input("Enter value2: "))
        div(a,b)

    elif choice==5:
        print("Program aborted!")
        quit()

    else:
        print("Sorry! You made an invalid choice!")