def rectangle_area(a, b):
    return a * b


def right_triangle_area(a, b):
    return a * b / 2


x = float(input("Enter X: "))
y = float(input("Enter Y: "))
z = float(input("Enter Z: "))
t = float(input("Enter T: "))

area = rectangle_area(x, y) + right_triangle_area(z, t)

print("Area of quadrilateral:", area)



n = int(input("Enter a non-negative integer: "))

octal = format(n, "010o")

print("Octal code:", octal)