import hashlib
import csv


def password_hashing(password):
    hashed_password = hashlib.sha256(password.encode())
    return hashed_password.hexdigest()


user_input = input("Enter username: ")
password_input = input("Enter password: ")
hash_password = password_hashing(password_input)

dict_info = {"username": user_input, "password": hash_password}

with open("user_info.txt", "a") as file_writer:
    fields_name = ["username", "password"]
    writer = csv.DictWriter(file_writer, fieldnames=fields_name)
    if file_writer.tell() == 0:
        writer.writeheader()
    writer.writerow(dict_info)