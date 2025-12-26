def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Enter A: "))
b = int(input("Enter B: "))

g = gcd(a, b)
l = (a * b) // g

print("GCD:", g)
print("LCM:", l)



import math

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
d = float(input("Side d: "))
e = float(input("Diagonal: "))

p1 = (a + b + e) / 2
p2 = (c + d + e) / 2

s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - e))
s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - e))

print("Area:", s1 + s2)