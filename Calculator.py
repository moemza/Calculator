def add(a, b): # Add function
    return a + b 

def sub(a, b): # Subtraction function
    return a - b 

def div(a, b): # Division function
    if b == 0:
        return None  # Indicate an error with None
    return a / b 

def mult(a, b): #Multiplication function
    return a * b 

def valid_equation(equation):
   
    valid_chars = set("0123456789.+-*/ ")
    if not equation:  # Check for empty input
        print("Input cannot be empty.")
        return False

    # Check for valid characters
    for char in equation:
        if char not in valid_chars:
            print(f"Invalid character '{char}' found in input.")
            return False

    # Check for consecutive operators or operators at the start/end
    last_char = ''
    for char in equation:
        if char in listop:
            if last_char in listop:
                print("Consecutive operators are not allowed.")
                return False
            last_char = char
        else:
            last_char = ''
    
    if equation[0] in listop or equation[-1] in listop:
        print("Input cannot start or end with an operator.")
        return False

    return True
    
def get_equation():
    while True:
        equation = input("Please enter your equation: ")
        if valid_equation(equation):
            break
        print("Please enter a valid equation.")
    list_equation = []
    nums = ''
    for char in equation:
        if char.isdigit() or char == '.':  # Handle numbers and decimals
            nums += char
        else:
            if nums:
                list_equation.append(float(nums))  # Add the complete number to the list
                nums = '' # clears my temporary number string
            list_equation.append(char)  # Add the operator to the list

    if nums:  # Add the last number if there is any
        list_equation.append(float(nums))
    return list_equation

# List of valid operators
listop = ['*', '/', '+', '-']

# Main calculation loop
def calculator():
    equation = get_equation()
    for operator in listop:
        while operator in equation:
            indexi = equation.index(operator)
            num1 = equation[(indexi-1)]
            num2 = equation[(indexi+1)]
            
            if operator == '/':
                result = div(num1, num2)
            elif operator == '*':
                result = mult(num1, num2)
            elif operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = sub(num1, num2)     
            equation[indexi - 1: indexi + 2] = [result] 
            
    return equation[0]
    

# Start the calculator
#calculator()
print(calculator())