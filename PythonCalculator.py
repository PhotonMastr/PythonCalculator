import os 

number1 = float(input("Enter first number: "))
os.system('cls' if os.name == 'nt' else 'clear')
operatorr = input("Enter Operator (+, -, *, /): ")
os.system('cls' if os.name == 'nt' else 'clear')
number2 = float(input("Enter second number: "))
os.system('cls' if os.name == 'nt' else 'clear')

if operatorr == "+":
    print(number1 + number2)
elif operatorr == "-":
    print(number1 - number2)
elif operatorr == "/": 
    print(number1 / number2)
elif operatorr == "*":
    print(number1 * number2)
else:
    print("You have entered an invalid operator!")
