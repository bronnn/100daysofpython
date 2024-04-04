from art import logo

print(logo)

# Calculator

# Add

def add (n1, n2):
    return n1 + n2

# Subtract
def subtract (n1, n2):
    return n1 - n2

# Multiply
def multiply (n1, n2):
    return n1 * n2

# Divide
def divide (n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input ("What's the first number: "))
    for operator in operations:
        print (operator)
    should_continue = True

    while should_continue:
        chosen_operator = input("Pick an operator: ")
        num2 = float(input("What's the next number: "))
        answer = operations[chosen_operator](num1, num2)

        print(f"{num1} {chosen_operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()