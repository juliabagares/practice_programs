text = input("Enter string: ")
upper_text = ""

for char in text:
    if 'a' <= char <= 'z':
        upper_text += chr(ord(char) - 32)
    else:
        upper_text += char

print(upper_text)