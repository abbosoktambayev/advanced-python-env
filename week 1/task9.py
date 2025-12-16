ticket = input(
    "Enter a 6-digit ticket number to check whether it is lucky or not: "
)

if len(ticket) != 6 or not ticket.isdigit():
    print("Error: you must enter exactly 6 digits.")
else:
    sum_first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])

    sum_last = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if sum_first == sum_last:
        print("YES — this ticket is lucky.")
    else:
        print("NO — this ticket is not lucky.")