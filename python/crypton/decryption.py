"""
Decryption part of the software.

"""

import os
import subprocess
import base64
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Get the encrypted message from the command line.
if len(sys.argv) == 1:
    print('Add argument')
    sys.exit()

encrypted_message = sys.argv[1]


# Key - IV
inpt = input("Give me the secret key: ").encode()
secret_key = inpt
iv = b'\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'


# Decode the base64 encoded message.
decoded_message = base64.b64decode(encrypted_message)

# Create a cipher object using the secret key and the IV
cipher = AES.new(secret_key, AES.MODE_CBC, iv)

# Decrypt the message
decrypted_message = cipher.decrypt(decoded_message)
# Remove the padding
BLOCK_SIZE = 32
decrypted_message = unpad(decrypted_message, BLOCK_SIZE)

decstr = decrypted_message.decode()
# Print the decrypted message
print(decstr)
