"""
Encryption part of the software.

"""

import sys
import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import string

from base64 import b64encode

message = input("Message:")

letters = string.ascii_lowercase
secret_key1 = ''.join(random.choice(letters) for i in range(32))

iv = b'\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'

print("Secret key is : "+secret_key1)
secret_key=secret_key1.encode()

BLOCK_SIZE = 32
padded_message = pad(message.encode(), BLOCK_SIZE) # --> PKCS7 padding.


cipher = AES.new(secret_key, AES.MODE_CBC, iv) # --> Create a cipher object using the secret key and the IV
encrypted_message = cipher.encrypt(padded_message) # --> Encrypts the padded message by using cipher.
base64_encrypted_message = base64.b64encode(encrypted_message) # --> Encode the encrypted message to base64

encstr = base64_encrypted_message.decode()
print("Encrypted message is :"+encstr)
