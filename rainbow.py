import csv

def rainbow_password(password, path):
    with open(path, mode= 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if password == row[0]:
                password = row[1]
        return password
    
if __name__ == '__main__':
    print(rainbow_password('bcbcc8be7132ba4329e52e707bce0f7f'))  # dummy values, will be changed later