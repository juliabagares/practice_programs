numbers = []

while True:
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        break