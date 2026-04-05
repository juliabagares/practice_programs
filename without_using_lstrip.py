text = input("Enter text: ")

index = 0
while index < len(text) and text[index] == " ":
    index += 1

print(text[index:])