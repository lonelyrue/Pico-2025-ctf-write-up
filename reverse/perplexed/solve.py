ref = bytes.fromhex("e1a71ef875237b61b99dfc5a5bdf69d2fe1bedf4ed67f4")

idx, k = 0, 0
bits_needed = {}

for block in range(0, 0x17):
    for j in range(0, 8):           
        if k == 0:
            k += 1
        mask1_bitpos = 7 - j
        mask2_bitpos = 7 - k
        ref_bit = (ref[block] >> mask1_bitpos) & 1
        bits_needed.setdefault(idx, {})[mask2_bitpos] = ref_bit
        k += 1
        if k == 8:
            k = 0
            idx += 1

password = bytearray(27)
for i, bits in bits_needed.items():
    b = 0
    for bitpos, val in bits.items():
        if val:
            b |= (1 << bitpos)
    password[i] = b

print(bytes(password))