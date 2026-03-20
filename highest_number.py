numbers = []

while True:
    try:
        number=int(input("enter a number: "))
        numbers.append(number)

    except ValueError:
        break

highest_number = max(numbers)
print("the highest number is ", highest_number)