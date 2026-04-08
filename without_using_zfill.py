text = input("Enter string: ")
length = int(input("Enter length: "))

while len(text) < length:
    text = "0" + text

print(text)