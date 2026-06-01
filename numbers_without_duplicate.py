numbers = [int(input(f"number{i+1}: ")) for i in range(10)]

print("Numbers without duplicates:")

for n in numbers:
    if numbers.count(n) == 1:
        print(n)