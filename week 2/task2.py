
a = input("Enter the text where we look for shifts: ")
b = input("Enter the string to shift: ")

if len(b) > len(a):
    print(0)
else:
    cnt = 0
    bb = b + b
    lb = len(b)

    for i in range(len(a) - lb + 1):
        sub = a[i: i + lb]
        if sub in bb:
            cnt += 1

    print("Number of cyclic shifts found:", cnt)