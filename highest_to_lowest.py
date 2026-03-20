numbers = []

while True:
    try:
        number=int(input("enter the number:"))
        numbers.append(number)
    except ValueError:
        break

