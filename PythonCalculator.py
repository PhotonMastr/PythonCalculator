import os

number1 = float(input("Enter first number: "))
os.system('clear')
operatorr = input("Enter Operator (you can also type multiply, or add for example): ")
os.system('clear')
number2 = float(input("Enter second number: "))
os.system('clear')

if operatorr == "+" or "add":
    print(number1 + number2)
elif operatorr == "-" or "minus":
    print(number1 - number2)
elif operatorr == "/" or "divide": 
    print(number1 / number2)
elif operatorr == "*" or "multiply":
    print(number1 * number2)
else:
    print("That's not a valid operator!")
