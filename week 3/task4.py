def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

num = a * d
den = b * c

g = gcd(num, den)

print("Result:", num // g, "/", den // g)



def inside(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 < r*r


a = float(input("Center a: "))
b = float(input("Center b: "))
r = float(input("Radius r: "))

count = 0

x = float(input("P x: "))
y = float(input("P y: "))
if inside(x, y, a, b, r): count += 1

x = float(input("F x: "))
y = float(input("F y: "))
if inside(x, y, a, b, r): count += 1

x = float(input("L x: "))
y = float(input("L y: "))
if inside(x, y, a, b, r): count += 1

print("Points inside:", count)