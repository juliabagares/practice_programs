text = input("Enter a string: ")
target_length = int(input("length: "))

total_spaces = target_length - len(text)
left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces

