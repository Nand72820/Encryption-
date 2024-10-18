from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Set the encryption key (must be 16 bytes for AES-128)
encryption_key = "Join - @creativeydv Channel ON TG".encode('utf-8')[:16]

# Read the content of the file to encrypt
file_to_encrypt = 'upgrade.py'
with open(file_to_encrypt, 'rb') as f:
    file_data = f.read()

# Create the AES cipher in ECB mode
cipher = AES.new(encryption_key, AES.MODE_ECB)

# Encrypt the file data (make sure it's padded to block size)
encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))

# Base64 encode the encrypted data
encrypted_data_base64 = base64.b64encode(encrypted_data)

# Save the encrypted content to a file
with open(f'{file_to_encrypt}.enc', 'wb') as f_enc:
    f_enc.write(encrypted_data_base64)

print(f"File '{file_to_encrypt}' has been encrypted and saved as '{file_to_encrypt}.enc'.")
