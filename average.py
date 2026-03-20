numbers = []

while True:
    try:
        number=(int(input("Enter a number: ")))
        numbers.append(numbers)

    except ValueError:
        break

if numbers:
    average = sum(numbers)/len(numbers)
    print("The average is", average)
