numbers = [float(input(f"numbers {i+1}: ")) for i in range(10)]

first_number = numbers[0]
print("The first number is ", first_number)

sum_of_remaining_numbers = sum(numbers[1:])
print("The sum of all the remaining numbers is ", sum_of_remaining_numbers)

result = first_number - sum_of_remaining_numbers
print("The result is ", result)
