full_name = input("Enter your full name in incorrect casing: ")

pascal = full_name.title().replace(" ", "")
print(pascal)