numbers = [float(input(f"number{i+1}: "))for i in range (10)]

odd = len([n for n in numbers if n % 2 == 1])
print(f"The odd number in total is: {odd}")