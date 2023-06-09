def is_number(var):
    """Returns True if the variable can be changed to a float"""
    if var is None:
        return False
    try:
        float(var)
        return True
    except ValueError:
        return False


def format_num(num):
    """Return a float is the variable is a mixed number, returns an integer otherwise"""
    if num % 1 == 0:
        return round(int(num), 6)
    else:
        return round(num, 6)


def ask_operation():
    """Asks the user for an operator until valid
    Returns the operator"""
    op = input("What operation do you want to perform? ")
    while not (op == "+" or op == "-" or op == "*" or op == "/") or op == "":
        op = input(f"\"{op}\" is not a valid operation. Use one of four possible operators: ")
    return op


def ask_num(message):
    """Asks the user for a number until valid
    Returns the number"""
    num = input(message)
    while not is_number(num):
        num = input(f"\"{num}\" is not a number. Type in a number: ")
    if float(num) % 1 == 0 or float(num) == 0:
        return int(float(num))
    else:
        return float(num)

 
def calculate(n1, n2, op):
    if op == "/" and num2 == 0:
        print("Division by 0 is not allowed")
    elif op == "+":
        return format_num(n1 + n2)
    elif op == "-":
        return format_num(n1 - n2)
    elif op == "*":
        return format_num(n1 * n2)
    else:
        return format_num(n1 / n2)


continue_calc = "y"
print("Welcome to the calculator app!\n")
print("  + ADD          - SUBTRACT")
print("  * MULTIPLY     / DIVIDE\n")
num1 = ask_num("Type in the first number: ")
while continue_calc == "y":
    operation = ask_operation()
    num2 = ask_num("Type in the second number: ")
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")
    continue_calc = input(f"Type \"y\" if you want to do more operations with the result {result}? ").lower()
    if continue_calc == "y":
        num1 = result
