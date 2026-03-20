numbers = [float(input(f"numbers{i+1}: ")) for i in range(10)]

even_numbers = len([n for n in numbers if n % 2 == 0])
print(f"The even number in total is:", even_numbers)