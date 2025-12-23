s = input("Enter a sequence of arrows (>, <, -): ")

cnt = 0
target1 = ">>-->"
target2 = "<--<<"

for i in range(len(s) - 4):
    sub = s[i : i+5]
    if sub == target1 or sub == target2:
        cnt += 1

print("Count of arrows:", cnt)