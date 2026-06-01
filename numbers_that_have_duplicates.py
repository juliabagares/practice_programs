numbers=[int(input(f"number {i+1}:")) for i in range (10)]

duplicates = [n for n in numbers if numbers.count(n) > 1]
duplicates = list(dict.fromkeys(duplicates))
print("duplicate numbers:", duplicates)