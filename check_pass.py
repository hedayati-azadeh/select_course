import argparse
import csv
import hashlib


def password_hashing(password):
    hashed_password = hashlib.sha256(password.encode())
    return hashed_password.hexdigest()


my_parser = argparse.ArgumentParser(description="Hashing")
my_parser.add_argument('username')
my_parser.add_argument('password')
dict_args = vars(my_parser.parse_args())
with open("user_info.txt", "r") as file_reader:
    reader = csv.DictReader(file_reader)

    user_found = False
    for item in reader:
        if item["username"] == dict_args["username"]:
            temp = password_hashing(dict_args['password'])
            user_found = True
            if temp == item["password"]:
                print("Well done!")
            else:
                print("Wrong password!")
    if not user_found:
        print("User does not exist!")
