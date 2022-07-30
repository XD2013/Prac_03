MINIMUM_LENGTH = 5

password = input("Create your password (minimum length: 5): ")
while len(password) < MINIMUM_LENGTH:
    print("Invalid password. The minimum length of password is 5.")
    password = input("Create your password (minimum length: 5): ")
print(f"Your password: {len(password) * '*'}")

