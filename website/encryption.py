import sys
import os
import subprocess
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import string
from base64 import b64encode


try:

    message = sys.argv[1]




    def aes(message):
        letters = string.ascii_lowercase
        secret_key1 = ''.join(random.choice(letters) for i in range(32))

        iv = b'\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'

        secret_key=secret_key1.encode()

        BLOCK_SIZE = 32
        padded_message = pad(message.encode(), BLOCK_SIZE)


        cipher = AES.new(secret_key, AES.MODE_CBC, iv) 
        encrypted_message = cipher.encrypt(padded_message) 
        base64_encrypted_message = base64.b64encode(encrypted_message) 

        encstr = base64_encrypted_message.decode()
        print("Hash is :"+encstr+"                   Secret key is:"+secret_key1)

    aes(message)
except IndexError as e:
    print("Please write something")