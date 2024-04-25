import pandas as pd
from md5 import md5
from sha1 import sha1
from sha256 import generate_hash as sha256
from numpy import loadtxt



def dictionary_password(password, type):

    words = loadtxt('list_1.txt', dtype=str)
    
    for word in words:
        print(word)
        if type==0 and md5(word) == password or type == 3 and md5(word) == password:
            return word
        if type == 1 and sha1(word) == password or type == 3 and sha1(word) == password:
            return word
        if type == 2 and str(sha256(word).hex()) == password or type == 3 and str(sha256(word).hex()) == password:
            return word
        
    return "Password not found"
    

if __name__ == '__main__':
    print(dictionary_password('bcbcc8be7132ba4329e52e707bce0f7f', 3))  # dummy values, will be changed later
   

