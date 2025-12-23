s1 = input("Enter first word: ")
s2 = input("Enter second word: ")

l1 = list(s1)
l2 = list(s2)

l1.sort()
l2.sort()

if l1 == l2:
    print("YES")
else:
    print("NO")