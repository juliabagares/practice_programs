numbers = []

while True:
    try:
        number=(int(input("enter a number: ")))
        numbers.append(number)

    except ValueError:
        break

if numbers:
    lowest=min(numbers)
    print("lowest number:", lowest)
else:
    print("no valid numbers")