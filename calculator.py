#python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))

if operator == "+":
    print(f"the result is {num1 + num2}")
elif operator == "-":
    print(f"the result is {num1 - num2}")
elif operator == "*":
    print(f"the result is {num1 * num2}")
else:
    print(f"the result is {num1 / num2}")
