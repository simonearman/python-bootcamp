def is_number(input):
    '''Returns True if the variable can be changed to a float'''
    if input is None:
        return False
    try:
        float(input)
        return True
    except ValueError:
        return False


def format_num(num):
    '''Return a float is the variable is a mixed number, returns an integer otherwise'''
    if num % 1 == 0:
        return round(int(num), 6)
    else:
        return round(num, 6)


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
    if float(num)%1 == 0 or float(num) == 0:
        return int(float(num))
    else:
        return float(num)

print("Welcome to the calculator app!\n")
print("  + ADD          - SUBSTRACT")
print("  * MULTIPLY     / DIVIDE\n")
num1 = ask_num("Type in the first number: ")
operation = ask_operation()
num2 = ask_num("Type in the second number: ")

if num2 == 0 and operation == "/":
    print("Division by 0 is not allowed")
elif operation == "+":
    print(f"The sum of {num1} and {num2} is {format_num(num1 + num2)}")
elif operation == "-":
    print(f"The difference of {num1} and {num2} is {format_num(num1 - num2)}")
elif operation == "*":
    print(f"The product of {num1} and {num2} is {format_num(num1 * num2)}")
else:
    print(f"The quotient of {num1} and {num2} is {format_num(num1 / num2)}")
