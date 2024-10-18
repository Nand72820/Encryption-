from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Encryption key (waise hi jo pehle di gayi thi)
encryption_key = "Join - @creativeydv Channel ON TG".encode('utf-8')[:16]

# File ka path jise encrypt karna hai
file_to_encrypt = 'upgrade.py'  # Yahan pe upgrade.py ka naam

# File ko read karein
with open(file_to_encrypt, 'r') as f:
    script_content = f.read()

# AES cipher banayein (ECB mode me)
cipher = AES.new(encryption_key, AES.MODE_ECB)

# Script content ko pad karein aur encrypt karein
padded_data = pad(script_content.encode('utf-8'), AES.block_size)
encrypted_data = cipher.encrypt(padded_data)

# Encrypted data ko base64 me encode karein
encrypted_base64_data = base64.b64encode(encrypted_data)

# Encrypted file ko save karein
with open('upgrade.py.enc', 'wb') as f:
    f.write(encrypted_base64_data)

print("Encryption successful! Encrypted file saved as 'upgrade.py.enc'")
