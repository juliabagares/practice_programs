text = input("Enter string: ")
is_all_lowercase = True

for char in text:
    if 'A' <= char <= 'Z':
        is_all_lowercase = False

print(is_all_lowercase)