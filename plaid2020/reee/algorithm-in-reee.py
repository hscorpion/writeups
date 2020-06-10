#!/usr/bin/env python

flag = ''
xor_num = 0x50
arr_check1 = [0x48, 0x5F, 0x36, 0x35, 0x35, 0x25, 0x14, 0x2C, 0x1D, 0x01, 0x03, 0x2D, 0x0C, 0x6F, 0x35, 0x61, 0x7E, 0x34, 0x0A, 0x44, 0x24, 0x2C, 0x4A, 0x46, 0x19, 0x59, 0x5B, 0x0E, 0x78, 0x74, 0x29, 0x13, 0x2C]

arr_check = []
# tmp = "pdta{hkXnoshii`XsooXffncy_sheub!z"
tmp = "pctf{ok_nothing_too_fancy_there!}"
for i in range(33):
	arr_check.append(ord(tmp[i]))

# Algorithm in this challenge
for key in range(1337):
	for i in range(len(arr_check)):
		arr_check[i] = arr_check[i] ^ xor_num
		xor_num = arr_check[i] ^ xor_num
for i in range(len(arr_check)):
    if arr_check[i] != arr_check1[i]:
        print("failed!")
        break

print(arr_check, "\n", arr_check1)
