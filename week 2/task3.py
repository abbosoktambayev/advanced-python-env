eq = input("Enter equation (like x+5=7): ")


eq = eq.replace("=", "==")

res = 0
found = False


for i in range(-1000, 1000):

    s = eq.replace("x", str(i))
    try:
        if eval(s):
            print("x =", i)
            found = True
            break
    except:
        pass

if not found:
    print("No solution found in range -1000 to 1000")