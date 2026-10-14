import re

email = input("Enter email: ")

pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*\.[a-zA-Z]{2,6}$"

if re.match(pattern, email):
    print("valid email")
else:
    print("invalid email")