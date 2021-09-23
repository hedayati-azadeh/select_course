import argparse
import csv
import logging
import hash_pass

logging.basicConfig(level=logging.INFO, filename='loging.log', filemode='a')

arg_pars = argparse.ArgumentParser(description= " register person ")

arg_pars.add_argument('--inputmode')
arg_pars.add_argument('--filename', required=False)

args= arg_pars.parse_args()
a = vars(args)
# print(a)
if a['inputmode'] == 'manual':
        fname = input('firstname: ')
        lname = input('lastname: ')
        username = hash_pass.password_hashing()
        password = hash_pass.password_hashing()
        logging.info(f'{fname}, {lname} is registered by {username} as username.')

        with open('text.csv', 'a',newline='') as f :
            write = csv.DictWriter(f,fieldnames=['Firstname', 'Lastname','username','password']
            if f.tell() == 0:
                write.writeheader()
            write.writerows([{'Firstname':fname, 'Lastname':lname , 'username': username , 'password' : password}])

        
elif a['inputmode'] == 'file' :
    # filename = input('filename: ')
    with open(a['filename'], 'r') as f :
        read = csv.reader(f)
        for row in read :
            print(row)