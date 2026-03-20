numbers=[]

while True:
    try:
        number=(int(input("enter a number: ")))
        numbers.append(number)

        if numbers.count(number) == 1:
            print("unique")
        else:
            print("duplicate")

    except ValueError:
        break
