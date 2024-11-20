from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

# Function to encrypt a file
def encrypt_file(input_path, output_path):
    key = get_random_bytes(32)  # 256-bit key
    cipher = ChaCha20.new(key=key)
    nonce = cipher.nonce
    
    with open(input_path, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = cipher.encrypt(plaintext)
    
    with open(output_path, 'wb') as f:
        f.write(nonce + ciphertext)
    
    return key.hex()  # Return the key in hexadecimal format

# Function to decrypt a file
def decrypt_file(input_path, output_path, hex_key):
    key = bytes.fromhex(hex_key)  # Convert key back to bytes
    with open(input_path, 'rb') as f:
        nonce = f.read(8)  # ChaCha20 nonce is 8 bytes
        ciphertext = f.read()
    
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    
    with open(output_path, 'wb') as f:
        f.write(plaintext)
