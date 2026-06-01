number = int(input("Enter a number: "))

if 0 <= number <= 1000:
    print(f"your number in 6 digit format: {number:06}")
else:
    print("number out of range")