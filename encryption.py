"""
Encryption part of the software.

"""

import sys
import os
import subprocess
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# The plaintext message to encrypt
message = sys.argv[1]


# Key - IV
secret_key = b"\xca\xd0\x12n\xd3\xfbW\xb3_A\x19\xab\xe5\x99\xc4?\x08\xccu{\xb5 \xed\x82\x93\xd2/\xa5\xfb\x98\xad'"

iv = b'\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'



BLOCK_SIZE = 32
padded_message = pad(message.encode(), BLOCK_SIZE) # --> PKCS7 padding.


cipher = AES.new(secret_key, AES.MODE_CBC, iv) # --> Create a cipher object using the secret key and the IV
encrypted_message = cipher.encrypt(padded_message) # --> Encrypts the padded message by using cipher.
base64_encrypted_message = base64.b64encode(encrypted_message) # --> Encode the encrypted message to base64


print(base64_encrypted_message)
