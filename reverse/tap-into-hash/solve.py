import re, ast, hashlib

data = open('enc_flag', 'r', encoding='utf-8', errors='replace').read()

key_repr = re.search(r"Key: (b'.*?')\n", data, re.S).group(1)
enc_repr = re.search(r"Encrypted Blockchain: (b[\"'].*)", data, re.S).group(1).strip()

key = ast.literal_eval(key_repr)
ciphertext = ast.literal_eval(enc_repr)

key_hash = hashlib.sha256(key).digest()

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

plaintext = b''
for i in range(0, len(ciphertext), 16):
    block = ciphertext[i:i+16]
    plaintext += xor_bytes(block, key_hash)   

print(plaintext)