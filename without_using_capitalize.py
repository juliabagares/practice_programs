text = input("Enter string: ")
capitalize = ""

for index in range(len(text)):
    if index == 0 and 'a' <= text[index] <= 'z':
        capitalize += chr(ord(text[index]) - 32)
    elif 'A' <= text[index] <= 'Z':
        capitalize += chr(ord(text[index]) + 32)
    else:
        capitalize += text[index]

print(capitalize)
