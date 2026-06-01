text = input("enter text: ")
word = input("enter word: ")
count = 0

for index in range(len(text) - len(word) + 1):
    if text[index:index + len(word)] == word:
        count += 1

print(count)