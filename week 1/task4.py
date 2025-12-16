N = int(input("Enter an integer number. The program will calculate the sum of all numbers from 1 to this number: "))

total = 0

if N >= 1:
    for i in range(1, N + 1):
        total += i
else:
    for i in range(1, N - 1, -1):
        total += i

print("The sum of numbers from 1 to the entered number is:", total)