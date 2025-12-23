line = input("Enter N (text length) and M (word length) e.g., '10 3': ").split()
n = int(line[0])
m = int(line[1])

txt = input("Enter the text: ")

words = set()

for i in range(n - m + 1):
    sub = txt[i : i + m]
    words.add(sub)

print("Unique substrings count:", len(words))