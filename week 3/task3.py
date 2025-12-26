import math

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)


a1 = float(input("Enter first leg of triangle 1: "))
b1 = float(input("Enter second leg of triangle 1: "))

a2 = float(input("Enter first leg of triangle 2: "))
b2 = float(input("Enter second leg of triangle 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypotenuse 1:", h1)
print("Hypotenuse 2:", h2)

if h1 > h2:
    print("First hypotenuse is greater")
elif h1 < h2:
    print("Second hypotenuse is greater")
else:
    print("Hypotenuses are equal")



text = input("Enter a string: ")

words = text.split()
result = []

for word in words:
    sorted_word = "".join(sorted(word))
    result.append(sorted_word)

print("Result:", " ".join(result))