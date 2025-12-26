def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

num = a * d - b * c
den = b * d

g = gcd(abs(num), den)

print("Result:", num // g, "/", den // g)



n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")