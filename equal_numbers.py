first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print("the bigger number is ", first_number)
elif first_number < second_number:
    print("the bigger number is ", second_number)

else:
    print("both numbers are equal")