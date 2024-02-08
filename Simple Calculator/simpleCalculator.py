# Defining four arithmetic functions 'Add', Subtract, 'Multiply', 'Divide'
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:

        return x / y
    else:
        return "cannot divide by zero"

# Operations users to select from 
print("Select operation: ")
print("+. Add")
print("-. Subtract")
print("*. Multiply")
print("/. Divide")

# ask user to select one of choices
choice = input("Enter choice (+,-,*,/): ")

# User input 2 numbers for operation
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

# Switch case calculator operator

if choice == '+':
    print(number1, " + ", number2, " = ", add(number1, number2))

elif choice == '-':
    print(number1, " - ", number2, " = ", subtract(number1, number2))

elif choice == '*':
    print(number1, " * ", number2, " = ", multiply(number1, number2))

elif choice == '/':
    print(number1, " / ", number2, " = ", divide(number1, number2))

else:
    print("Invalid")




