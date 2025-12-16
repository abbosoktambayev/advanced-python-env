word = input("Please enter a word. Each letter of this word will be processed one by one: ")
n = int(input("Please enter a number. Each letter will be repeated this many times: "))

for ch in word:
    print(ch * n)