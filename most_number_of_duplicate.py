numbers = []

while True:
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        break

duplicates = [n for n in numbers if numbers.count(n) > 1]]
duplicates = max(duplicates)
print("the most number of duplicates is ", duplicates)