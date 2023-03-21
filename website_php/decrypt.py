"""
Decryption part of the software.

"""

import os
import subprocess
import base64
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

# Get the encrypted message from the command line.

try:

    encrypted_message = sys.argv[1]


    # Key - IV
    inpt = sys.argv[2].encode()
    secret_key = inpt

    def dec(encrypted_message,secret_key):
        # Decode the base64 encoded message.
        iv = b'\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
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
    dec(encrypted_message,secret_key)

except binascii.Error:
    print("Pleas write correctly")
except IndexError as b:
    print("Please fill blanks")
except ValueError as c:
    print("Please write correctly")    