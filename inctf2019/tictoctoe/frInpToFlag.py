key_xor = [0x0C9, 0x0E1, 0x121, 0x169, 0x1A, 0x0D, 0x0A1, 0x7F, 0x7, 0x9, 0x157, 0x116, 0x0B9, 0x0B8, 0x15D, 0x86, 0x8C, 0x0DF, 0x161, 0x0B3, 0xF8, 0xEF, 0x167, 0x80, 0x17, 0xF6, 0x119, 0x79, 0x84, 0x82, 0x66, 0x9A]
key = [20, 40, 15, 26, 11, 39, 22, 33, 21, 35, 13, 34, 14, 32, 25, 28]
flag = ''
z = []
for i in range(16):
    z.append(key[i] * 8)
    z.append(key[i] * 7)
for i in range(32):
    flag += chr((z[i] ^ (i + key_xor[i]))%256)
print(flag)