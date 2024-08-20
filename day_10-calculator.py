#import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    if n2!=0:
        return n1/n2
    return "Error! You can't divide by 0!"



operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
#    print(art.logo)
    carry_on=True
    first_num = float(input("What is the first number?: "))

    while carry_on==True:
        for key in operations:
            print(key)
        operation_chose=input("Pick an operation: ")
        if operation_chose not in ['+', "-", "*", "/"]:
            return print("Error")

        another_num=float(input("What is the next number?: "))
        result=operations[operation_chose](first_num, another_num)
        print(f"{first_num} {operation_chose} {another_num} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 's' to stop: ")
        if choice == "y":
            first_num=result
        elif choice =="s":
            return print("Goodbye")
        else:
            carry_on=False
            print("\n"*20)
            calculator()

calculator()