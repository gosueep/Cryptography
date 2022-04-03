# brute.py
# known-plaintext attack to brute force the key with a dictionary

# Eugin Pahk
# For CSCI 474 - Spring 2022
# Section A

import binascii
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

ptext = b'This is a top secret.'
ptext = pad(ptext, 16)

ctext = b'8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9'
init_v = b'\0'*16

f = open("words.txt", "r")


for line in f.readlines():

    key = line.strip()              #strips newline

    if len(key) > 16:               #skips word if greater than 16 characters
        continue
    for i in range(len(key), 16):   #pads key with spaces
        key += " "

    key = str.encode(key)           #convert to bytes


    cipher = AES.new(key, AES.MODE_CBC, iv=init_v)      #encrypt plaintext with current key
    ctext_i = cipher.encrypt(ptext)
    ctext_i = binascii.hexlify(ctext_i)

    if ctext_i == ctext:          
        print("Key Found!")
        print("Key: " + line)
        sys.exit()

print("Key not found")
