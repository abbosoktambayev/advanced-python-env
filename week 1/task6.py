a = int(input("Enter the first number. This is the number you want to calculate with: "))

op = input("Enter the operation you want to perform (+, -, *, /): ")

b = int(input("Enter the second number. This number will be used in the calculation: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Division by zero is not allowed!" if b == 0 else "Result: " + str(a / b))
else:
    print("Invalid operation. Please enter +, -, *, or /.")