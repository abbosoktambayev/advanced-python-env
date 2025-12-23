a = int(input("Enter the first salary in tenge: "))
b = int(input("Enter the second salary in tenge: "))
c = int(input("Enter the third salary in tenge: "))

max_salary = max(a, b, c)
min_salary = min(a, b, c)

print("The difference between the highest and the lowest salary is:", max_salary - min_salary)