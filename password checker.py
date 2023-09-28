import re


def password_strength(password):
    # Define regular expressions to check for various criteria
    length_regex = r'.{8,}'  # At least 8 characters
    uppercase_regex = r'[A-Z]'  # At least one uppercase letter
    lowercase_regex = r'[a-z]'  # At least one lowercase letter
    digit_regex = r'[0-9]'  # At least one digit
    special_char_regex = r'[!@#$%^&*()\-_=+{};:,<.>?]'  # At least one special character

    score = 0
    if re.search(length_regex, password):
        score += 1
    if re.search(uppercase_regex, password):
        score += 1
    if re.search(lowercase_regex, password):
        score += 1
    if re.search(digit_regex, password):
        score += 1
    if re.search(special_char_regex, password):
        score += 1

    if score >= 4:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    elif score >= 2:
        return "Weak"
    else:
        return "Very Weak"


user_password = input("Enter a password: ")

strength = password_strength(user_password)

print(f"Password Strength: {strength}")
