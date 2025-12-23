line = input("Enter shopping list items (apple banana ...): ").split()
d = {}

for x in line:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

print("\nPurchase frequency:")
for k in d:
    print(k + ": " + str(d[k]))

mx = 0
best = ""
for k in d:
    if d[k] > mx:
        mx = d[k]
        best = k
print("Most popular item: " + best)

singles = []
for k in d:
    if d[k] == 1:
        singles.append(k)
print("Purchased once: " + " ".join(singles))

print("Sorted by frequency:")
srt = sorted(d.items(), key=lambda item: item[1], reverse=True)

for item in srt:
    print(item[0], item[1])