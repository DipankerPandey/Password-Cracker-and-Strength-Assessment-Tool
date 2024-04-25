import itertools
import string
from md5 import md5
from sha1 import sha1
from sha256 import generate_hash as sha256


def guess_password(real, a, b, type):
    # string of every possible character in a password
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    for password_length in range(a, b):
        # creates all possible combinations of characters of increasing length
        for guess in itertools.product(chars, repeat=password_length):
            guess = ''.join(guess)
            # checking if we found the password, will be replaced with hash function later on
            if type == 0 or type == 3 and md5(guess) == real:
                return guess
            elif type == 1 or type == 3 and sha1(guess) == real:
                return guess
            elif type == 2 or type == 3 and sha256(guess) == real:
                return guess
            print(guess)
    return "Password not found"


if __name__ == '__main__':
    print(guess_password('bcbcc8be7132ba4329e52e707bce0f7f', 8, 64))  # dummy values, will be changed later
