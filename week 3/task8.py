n = int(input("Enter n: "))

for num in range(1, n + 1):
    ok = True
    for d in str(num):
        d = int(d)
        if d == 0 or num % d != 0:
            ok = False
            break
    if ok:
        print(num, end=" ")




def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]


m = int(input("Enter array length: "))
A = []

for i in range(m):
    A.append(int(input("Enter element: ")))

print("Original array:", A)

swap_first_last(A)

print("Resulting array:", A)