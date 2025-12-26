print("Choose a shape:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter choice: ")

if choice == "1":
    a = float(input("Enter width: "))
    b = float(input("Enter height: "))
    print("Area =", a * b)

elif choice == "2":
    a = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area =", a * h / 2)

elif choice == "3":
    r = float(input("Enter radius: "))
    print("Area =", 3.14 * r * r)

else:
    print("Wrong choice")



for i in range(3):
    nums = input("Enter numbers separated by space: ")
    arr = list(map(int, nums.split()))

    s = sum(arr)
    avg = s / len(arr)

    print("Sum =", s)
    print("Mean =", avg)