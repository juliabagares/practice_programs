numbers = []

while True:
    try:
        number=(int(input("Enter a number: ")))
        numbers.append(number)

    except ValueError:
        break

if numbers:
    average = sum(numbers)/len(numbers)
    print("The average is", average)
else:
    print("No valid numbers entered")