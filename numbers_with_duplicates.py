numbers = [int(input(f"number{i+1}:")) for i in range(10)]

no_duplicate_first = []
for n in numbers:
    if n not in no_duplicate_first:
        no_duplicate_first.append(n)

