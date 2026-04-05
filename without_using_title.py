text = input("Enter string: ")
title_text = ""
start_of_word = True

for char in text:
    if char == " ":
        title_text += char
        start_of_word = True
        