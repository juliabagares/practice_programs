text = input("Enter a string: ")

start_text = input("Enter start: ")
if text[:len(start_text)] == start_text:
    print(True)
else:
    print(False)