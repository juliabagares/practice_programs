text = input("Enter string: ")
suffix_text = input("Enter suffix string: ")

if text[-len(suffix_text):] == suffix_text:
    print(text[:-len(suffix_text)])
else:
    print(text)