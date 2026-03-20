full_name = input("Enter your full name in incorrect casing: ")

snake = full_name.lower().replace(" ", "_")
print(snake)