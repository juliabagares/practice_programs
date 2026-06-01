text = input("enter string: ")
word = input("enter word: ")

for index in range(len(text) - len(word), -1, -1):
    if text[index:index + len(word)] == word:
        print(index)
        break