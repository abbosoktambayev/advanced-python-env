import math

# triangle area subroutine
def triangle_area(a):
    return (math.sqrt(3) / 4) * a * a


a = float(input("Enter side of hexagon: "))
print("Hexagon area:", 6 * triangle_area(a))


for i in range(3):
    print("Rectangle", i + 1)
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    print("Area:", a * b)