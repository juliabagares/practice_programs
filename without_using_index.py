text = input("enter text: ")
word = input("enter word: ")

for index in range(len(text) - len(word) + 1):
    if text[index:index + len(word)] == word:
        print(text)
        break