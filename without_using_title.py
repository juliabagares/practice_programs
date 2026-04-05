text = input("Enter string: ")
title_text = ""
start_of_word = True

for char in text:
    if char == " ":
        title_text += char
        start_of_word = True
    elif start_of_word:
        if 'a' <= char <= 'z':
            title_text += chr(ord(char) - 32)
        else:
            title_text += char
        start_of_word = False
    else:
        if 'A' <= char <= 'Z':
            title_text += chr(ord(char) + 32)
        else:
            title_text += char
    