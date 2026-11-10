# Password generator v1.1
import random
import string
 
CHARS = string.ascii_letters + string.digits + "!@#$%"
 
 
def generate_password(length=12):
    return "".join(random.choice(CHARS) for _ in range(length))
 
 
def check_strength(password):
    score = sum([len(password) >= 8,
                 any(c.isdigit() for c in password),
                 any(c.isupper() for c in password),
                 any(c in "!@#$%" for c in password)])
    return ["weak", "weak", "weak", "medium", "strong"][score]
 
 
def show_password(password):
    print("Password:", password, "-", check_strength(password))
 
 
def generate_pin(length=4):
    return "".join(random.choice(string.digits) for _ in range(length))
 
 
def read_length():
    while True:
        value = input("Length (4-32): ")
        if value.isdigit() and 4 <= int(value) <= 32:
            return int(value)
        print("Error: enter a number from 4 to 32")
 
 
if __name__ == "__main__":
    show_password(generate_password(read_length()))
    print("PIN:", generate_pin())
