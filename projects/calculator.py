def is_number(input):
    if input is None:
        return False
    try:
        float(input)
        return True
    except ValueError:
        return False


def add(n1, n2):
    '''Returns a float if the sum is a mixed number, returns an int otherwise'''
    if (n1 + n2) % 1 == 0:
        return int(n1 + n2)
    else:
        return n1 + n2


def substract(n1, n2):
    '''Returns a float if the difference is a mixed number, returns an int otherwise'''
    if (n1 - n2) % 1 == 0:
        return int(n1 - n2)
    else:
        return n1 - n2


def multiply(n1, n2):
    '''Returns a float if the product is a mixed number, returns an int otherwise'''
    if (n1 * n2) % 1 == 0:
        return int(n1 * n2)
    else:
        return n1 * n2


def divide(n1, n2):
    '''Returns a float if the quotient is a mixed number, returns an int otherwise'''
    if (n1 / n2) % 1 == 0:
        return int(n1 / n2)
    else:
        return n1 / n2


def ask_operation():
    '''Asks the user for an operator until valid
    Returns the operator'''
    op = input("What operation do you want to perform? ")
    while not (op == "+" or op == "-" or op == "*" or op == "/") or op == "":
        op = input(f"\"{op}\" is not a valid operation. Use one of four possible operators: ")
    return op


def ask_num(message):
    '''Asks the user for a number until valid
    Returns the number'''
    num = input(message)
    while not is_number(num):
        num = input(f"\"{num}\" is not a number. Type in a number: ")
    if float(num)%1 == 0:
        return int(num)
    else:
        return float(num)

print("Welcome to the calculator app!\n")
print("  + ADD          - SUBSTRACT")
print("  * MULTIPLY     / DIVIDE\n")
num1 = ask_num("Type in the first number: ")
operation = ask_operation()
num2 = ask_num("Type in the second number: ")

if operation == "+":
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
elif operation == "-":
    print(f"The difference of {num1} and {num2} is {substract(num1, num2)}")
elif operation == "*":
    print(f"The product of {num1} and {num2} is {multiply(num1, num2)}")
else:
    print(f"The quotient of {num1} and {num2} is {divide(num1, num2)}")
