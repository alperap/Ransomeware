import os
from cryptography.fernet import Fernet

file_list = []

def create_file_list():
    global file_list
    for file in os.listdir():
        if file == "key.key" or file == "ransomeware_simple_decrypt.py":
            continue
        if file == "ransomeware_simple_crypt.py":
            continue
        if os.path.isfile(file):
            file_list.append(file)
    print(file_list)

def need_key(key_file_path):
    with open(key_file_path,"rb") as keys:
        key = keys.read()
        return key

def decrypt_files(key):
    global file_list
    for file_name in file_list:
        with open(file_name,"rb") as file:
            read_c = file.read()
        decrypt = Fernet(key).decrypt(read_c)
        with open(file_name,"wb") as file:
            file.write(decrypt)

create_file_list()
path = input("You have to give me a key path: ")
key = need_key(path)
decrypt_files(key)
