text = input("Enter a text: ")

is_all_uppercase = True

for character in text:
    if 'a' <= character <= 'z':
        is_all_uppercase = False
