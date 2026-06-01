numbers=[]

while True:
    try:
        number=int(input("enter a number:"))
        numbers.append(number)
    except ValueError:
        break

numbers.sort()
print("the lowest to highest numbers: ", numbers)