numbers = []

while True:
    try:
        number=(int(input("enter a number: ")))
        numbers.append(number)

    except ValueError:
        break

