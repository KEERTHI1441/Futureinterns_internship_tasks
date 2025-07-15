# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import os

# KEY = b'ThisIsASecretKey'  # 16 bytes for AES-128, 32 bytes for AES-256
# BLOCK_SIZE = 16
# PADDING = b'\0'

# def pad(s):
#     return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# def encrypt_file(file_data):
#     iv = get_random_bytes(BLOCK_SIZE)
#     cipher = AES.new(KEY, AES.MODE_CBC, iv)
#     encrypted_data = iv + cipher.encrypt(pad(file_data))
#     return encrypted_data

# def decrypt_file(encrypted_data):
#     iv = encrypted_data[:BLOCK_SIZE]
#     cipher = AES.new(KEY, AES.MODE_CBC, iv)
#     decrypted_data = cipher.decrypt(encrypted_data[BLOCK_SIZE:])
#     return decrypted_data.rstrip(PADDING)


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv('ENCRYPTION_KEY').encode()
BLOCK_SIZE = 16
PADDING = b'\0'

def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

def encrypt_file(file_data):
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted_data = iv + cipher.encrypt(pad(file_data))
    return encrypted_data

def decrypt_file(encrypted_data):
    iv = encrypted_data[:BLOCK_SIZE]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data[BLOCK_SIZE:])
    return decrypted_data.rstrip(PADDING)
