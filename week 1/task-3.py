A = float(input(
    "Enter a real number with two digits after the decimal point. "
    "The program will swap the integer and fractional parts of this number: "
))

integer_part = int(A)
fractional_part = int((A - integer_part) * 100)

new_number = fractional_part + integer_part / 100

print("The new number after swapping the integer and fractional parts is:", new_number)