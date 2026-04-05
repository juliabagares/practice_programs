text = input("Enter string: ")
swapped = ""

for char in text:
    if 'a' <= char <= 'z':
        swapped += chr(ord(char) - 32)