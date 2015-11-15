#!/usr/bin/env python3

'''

Generates a hash of a large file that allows a particular file authentication
system to verify the hash before the entire file is downloaded. See readme for
an explanation.

'''
import tkinter as tk
from Crypto.Hash import SHA256
import binascii

blocks = []
hashvalue = b''

root = tk.Tk()
root.withdraw()
path = tk.filedialog.askopenfilename()

def read_in_chunks(file):
    """Lazy function (generator) to read a file 1kB piece by 1kB piece."""
    while True:
        data = file.read(1024)
        if not data:
            break
        yield data

f = open(path, 'rb')

for data in read_in_chunks(f):
    blocks.append(data)

#calculating a SHA256 hash by taking each block (in reverse order),
#hashing and appending
    
for block in reversed(blocks):
    #appends hashvalue to the end of the block, both are bytes
    block += hashvalue
    sha = SHA256.new()
    sha.update(block)
    hashvalue = sha.digest()

print(binascii.hexlify(hashvalue).decode())
    
