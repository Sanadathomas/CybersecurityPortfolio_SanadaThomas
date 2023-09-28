import hashlib
import getpass
import os


def hash_password(password):
    salt = os.urandom(16)
    password = password.encode()
    hashed_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    return salt + hashed_password


def verify_password(password, hashed_password):
    salt = hashed_password[:16]
    password = password.encode()
    hashed_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    return hashed_password == hashed_password[16:]


def get_password(prompt):
    password = getpass.getpass(prompt)
    password_confirm = getpass.getpass("Confirm password: ")
    if password != password_confirm:
        print("Passwords do not match, try again")
        return get_password(prompt)
    return password


def login():
    username = input("Username: ")
    password = get_password("Password: ")
    hashed_password = hash_password(password)
    # save username and hashed_password to a database for later verification


def main():
    print("Welcome to the password manager")
    print("1. Login")
    print("2. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        login()
    elif choice == 2:
        print("Goodbye")


if __name__ == '__main__':
    main()
