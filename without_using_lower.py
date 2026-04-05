text = input("Enter the text: ")
lower_text = ""

for character in text:
    if 'A' <= character <= 'Z':
        lower_text += chr(ord(character)+32)
        