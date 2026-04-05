text = input("Enter string: ")
swapped = ""

for char in text:
    if 'a' <= char <= 'z':
        swapped += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        swapped += chr(ord(char) + 32)