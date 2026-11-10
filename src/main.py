# Password Generator Pro v2.0
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
 
 
def generate_many(count, length=12):
    return [generate_password(length) for _ in range(count)]
 
 
def filter_by_strength(passwords, level):
    return [p for p in passwords if check_strength(p) == level]
 
 
def show_strong_passwords(count=10, length=12):
    strong = filter_by_strength(generate_many(count, length), "strong")
    print(f"Strong passwords: {len(strong)} of {count}")
    for password in strong:
        print(" ", password)


def menu():
    while True:
        choice = input("1 - password, 2 - PIN, 3 - strong passwords, 0 - exit: ")
        if choice == "1":
            show_password(generate_password(read_length()))
        elif choice == "2":
            print("PIN:", generate_pin())
        elif choice == "3":
            show_strong_passwords()
        elif choice == "0":
            break
 
 
if __name__ == "__main__":
    menu()
