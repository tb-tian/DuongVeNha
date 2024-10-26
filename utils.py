import csv

def check_credentials(username, password):
    with open('database.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False

def register_user(username, password):
    with open('database.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'password'])
        writer.writerow({'username': username, 'password': password})