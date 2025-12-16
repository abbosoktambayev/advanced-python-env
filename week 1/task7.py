a = int(input("Enter the first number. This is the number for the calculation: "))
op = input("Enter the operation (+, -, *, /) you want to perform: ")
b = int(input("Enter the second number. This number will be used with the operation: "))

result = (
    a + b if op == "+" else
    a - b if op == "-" else
    a * b if op == "*" else
    "Division by zero is not allowed!" if b == 0 else
    a / b
)

print("Result:", result)