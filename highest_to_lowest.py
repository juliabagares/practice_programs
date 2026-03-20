numbers = []

while True:
    try:
        number=int(input("enter the number:"))
        numbers.append(number)
    except ValueError:
        break

numbers.sort(reverse=True)
print("the highest to lowest number is", numbers)