# last_name = input("Your last name? ")
# first_name = input("Your first name? ")
# age = input("How old are you? ")
# phone_number = input("Your phone number? ")
#
# print(f"Your {first_name}, {last_name}")
# print(f"Your {age}")
# print(f"Your {phone_number}")
#
#
# print("Hello World!")


s = input("Enter a sequence of arrows (>, <, -): ")

cnt = 0
target1 = ">>-->"
target2 = "<--<<"

for i in range(len(s) - 4):
    sub = s[i : i+5]
    if sub == target1 or sub == target2:
        cnt += 1

print("Count of arrows:", cnt)