text = input("Enter a string: ")
ending_text = input("Enter ending text: ")

if text[-len(ending_text):] == ending_text:
    print(True)
else:
    print(False)