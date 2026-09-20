from PIL import Image
import numpy as np
import base64
im = Image.open('red.png').convert('RGBA')
row = np.array(im)[0]
bits = []
for i in range(128):
    for ch in (0,1,2,3):  # R,G,B,A
        bits.append(row[i][ch] & 1)
byte_arr = bytearray()
for j in range(0, len(bits) - 7, 8):
    byte_bits = bits[j:j+8]
    val = 0
    for bit in byte_bits:
        val = (val << 1) | bit
    byte_arr.append(val)

b64_string = byte_arr.decode('ascii')
print("Base64:", b64_string)

flag = base64.b64decode(b64_string).decode('utf-8')
print("Flag:", flag)
