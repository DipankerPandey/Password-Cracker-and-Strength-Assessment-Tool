import pandas as pd
from md5 import md5
from sha1 import sha1
from sha256 import generate_hash as sha256
from numpy import loadtxt



def dictionary_password(password):

    words = loadtxt('list_1.txt', dtype=str)
    
    for word in words:
        print(word)
        if md5(word) == password:
            return word
        elif sha1(word) == password:
            return word
        elif sha256(word) == password:
            return word
    

if __name__ == '__main__':
    print(dictionary_password('bcbcc8be7132ba4329e52e707bce0f7f'))  # dummy values, will be changed later

