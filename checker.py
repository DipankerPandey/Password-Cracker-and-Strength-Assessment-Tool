import re
import string

def calculate_entropy(password):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    numbers = "0123456789"
    special_chars = string.punctuation

    charsets = [lowercase, uppercase, numbers, special_chars]
    entropy = sum(len(charset) for charset in charsets if any(char in password for char in charset))

    entropy *= len(password)

    return entropy

def is_weak_password(password):
    weak_patterns = [
        r"\bpassword\b",
        r"\b123456\b",
        r"\bqwerty\b",
    ]

    with open('list_1.txt', 'r') as file:
        weak_passwords = {line.strip() for line in file}

    if any(re.search(pattern, password, re.IGNORECASE) for pattern in weak_patterns):
        return True

    if password.lower() in weak_passwords:
        return True

    if password.isalpha():
        return True

    if password.isnumeric():
        return True

    return False

def password_strength_checker(password):
    length = len(password)
    entropy = calculate_entropy(password)

    if is_weak_password(password):
        return "Weak password. Please choose a stronger password."

    if length >= 8 and length < 12:
        if (any(char.islower() for char in password) and any(char.isdigit() for char in password)) or \
           (any(char.islower() for char in password) and any(char.isupper() for char in password)) or \
           (any(char.islower() for char in password) and any(char in string.punctuation for char in password)) or \
           (any(char.isupper() for char in password) and any(char.isdigit() for char in password)) or \
           (any(char.isupper() for char in password) and any(char in string.punctuation for char in password)):
            return "Moderate password. Consider increasing length and complexity for better security."

    if length >= 10 and entropy >= 60:
        return "Strong password. Well done!"

    return "Weak password. Please choose a stronger password."

def get_user_password():
    """
    Prompt the user to enter a password securely.
    """
    import getpass
    password = getpass.getpass("Enter your password: ")
    return password

def main():
    password = get_user_password()
    strength = password_strength_checker(password)
    print(strength)

if __name__ == "__main__":
    main()