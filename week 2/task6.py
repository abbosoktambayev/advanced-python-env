def all_eq(lst):
    mx = 0
    for x in lst:
        if len(x) > mx:
            mx = len(x)

    res = []
    for x in lst:
        diff = mx - len(x)
        res.append(x + "_" * diff)

    return res


raw = input("Enter words to equalize separated by space: ")
words_list = raw.split()
result = all_eq(words_list)
print("Result:", result)