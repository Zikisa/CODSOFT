import random
import string


def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation
    characters = letters + numbers + special_chars
    password_len = int(input('Enter password length: '))
    password = ''
    for i in range(password_len):
        password += ''.join(random.choice(characters))
    print(f"Generated password is: {password}")


generate_password()
