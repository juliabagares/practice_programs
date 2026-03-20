numbers = [int(input(f"number{i+1}:")) for i in range(10)]

unique_numbers = list(set(numbers))
print("numbers (remove duplicate, keep first):", unique_numbers)
