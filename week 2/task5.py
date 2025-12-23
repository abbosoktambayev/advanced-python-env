valid = "ABCEHKMOPTXY"

try:
    num = int(input("How many plates to check?: "))

    for i in range(num):
        s = input(f"Enter plate #{i + 1} (e.g. A123BC): ")

        if len(s) != 6:
            print("No")
            continue

        ok = True

        if s[0] not in valid:
            ok = False

        if not s[1:4].isdigit():
            ok = False

        if s[4] not in valid:
            ok = False

        if s[5] not in valid:
            ok = False

        if ok:
            print("Yes")
        else:
            print("No")
except:
    pass