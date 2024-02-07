import itertools
import string


def guess_password(real, a, b):
    # string of every possible character in a password
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    for password_length in range(a, b):
        # creates all possible combinations of characters of increasing length
        for guess in itertools.product(chars, repeat=password_length):
            guess = ''.join(guess)
            # checking if we found the password, will be replaced with hash function later on
            if guess == real:
                return 'password is {}'.format(guess)
            print(guess)


if __name__ == '__main__':
    print(guess_password('pA#$', 8, 64))  # dummy values, will be changed later
