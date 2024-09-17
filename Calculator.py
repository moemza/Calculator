#def calculator(num1, operator, num2):

def add(a,b):
    total = a + b
    return total 

def sub(a,b):
    total = a - b
    return total 

def div(a,b):
    total = a / b
    return total 

def mult(a,b):
    total = a * b
    return total 

listop = ['+','-','*','/']
num1 = int(input("Please enter your first number: ")) 
operator = input("Please enter an operator: ")
num2 = int(input("Please enter your second number: "))
 
if operator == '+':
      answer = add(num1,num2)
      print(answer)
elif operator == '-':
        answer = sub(num1,num2)
        print(answer)
elif operator == '*':
        answer = mult(num1,num2)
        print(answer)
elif operator == '/':
        answer = div(num1,num2)
        print(answer)
else:
      print("Please enter a valid operator")


    