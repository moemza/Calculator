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

# List of valid operators
listop = ['+', '-', '*', '/']

# Function to get a valid number from user
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to get a valid operator from user
def get_valid_operator(prompt):
    while True:
        operator = input(prompt)
        if operator in listop or operator == '=':
            return operator
        print("Invalid operator. Please enter one of: +, -, *, / or =")

# Main calculation loop
def calculator():
    num1 = get_valid_number("Please enter your first number: ")
    
    while True:
        operator = get_valid_operator("Please enter an operator (+, -, *, /) or '=' to calculate: ")
        
        if operator == '=':
            print(f"Final result: {num1}")
            break   # Stops the loop when = sign is entered
        
        num2 = get_valid_number("Please enter the next number: ")

        if operator == '+':
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = sub(num1, num2)
        elif operator == '*':
            num1 = mult(num1, num2)
        elif operator == '/':
            result = div(num1, num2)
            if result is None:  # Check for division error
                print("Error: Division by zero!")
                continue  # Ask for the next input without changing num1
            num1 = result
        
        print(f"Current result is: {num1}")

# Start the calculator
calculator()