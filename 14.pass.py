import re

password = input("enter password: ")

if len(password) >= 8 and re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[0-9]",password) and re.search(r"[!@#$%^&*()_-]",password):
    print("strong password")
else:
    print("weak password")