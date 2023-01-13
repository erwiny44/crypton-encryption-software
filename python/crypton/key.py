"""
Generate your secret key.

"""

import os

# Generate a 16/32/64 byte key
key = os.urandom(32)

print(key)
