text = input("Enter the text: ")
lower_text = ""

for character in text:
    if 'A' <= character <= 'Z':
        lower_text += chr(ord(character)+32)
    else:
        lower_text += character

print(lower_text)