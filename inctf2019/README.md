# InCTF 2019 (Vietnamese) ([English](#english))

## cliche_crackme

Bài này input là flag được xử lý qua 4 function:

function1: Tạo mảng buf từ input:

![create_buf](/inctf2019/cliche_crackme/create_buf.png)

function2: Check tổng các kí tự của input:

![check_inp](/inctf2019/cliche_crackme/check_inp.png)

function3: Check tổng các kí tự của buf:

![check_sum](/inctf2019/cliche_crackme/check_sum.png)

function4: Check buf:

![check_buf](/inctf2019/cliche_crackme/check_buf.png)

Script to solve: [solver.py](/inctf2019/cliche_crackme/solver.py)

Flag: `inctf{Th4ts_he11_l0t_0f_w0rk_w4s_it?}`

## Encrypt

Reverse file `drop.exe` đơn giản ta thấy, nó check tên file qua hàm `Check1` và sau đó input được mã hoá qua hàm `Transform` check với tên file và 1 mảng cho sẵn ở hàm `Check2`

Script to solve drop.exe: [get_inp.py](/inctf2019/encrypt/get_inp.py)

Sau khi pass qua `drop.exe` thì nó drop ra 1 file [encrypterY8.exe](/inctf2019/encrypt/encrypterY8.exe). Reverse sơ qua thì file này đơn giản là Encrypt AES 128 (Microsoft Enhanced RSA and AES Cryptographic Provider) sử dụng với key là tên file, mà ở Description có nói là file ảnh đã được encrypt 2 lần nên mình code lại 1 Decrypt AES 128 và tiến hành decrypt file ảnh 2 lần và ra flag.

Source Decrypt AES 128: [decrypt.cpp](/inctf2019/encrypt/decrypt.cpp)

Flag:

![flag](/inctf2019/encrypt/flag.png)

## TIC-TOC-TOE

Tại hàm tạo bảng (`0x413AA0`), tương ứng với chỗ người đánh (X) từ 1 đến 16 input sẽ là từ `0xA` đến `0x19` và máy đánh (o) input là từ `0x1A` đến `0x29`. ( input[i], i chẵn là người đánh, lẻ là máy đánh)

![inp0](/inctf2019/tictoctoe/inp0.png)
![inp1](/inctf2019/tictoctoe/inp1.png)

Sau đó xử lý input tại hàm `0x41A0B0`. Hàm này thực hiện các thuật toán mã hoá cơ bản với input, sau đó xor input đã mã hoá với 1 mảng có sẵn để ra flag.

```c
str = '!@#sbjhdn5z6sf5gqc7kcd5mck7ld=&6';
j = 0;
for ( i = 0; i < 16; ++i )
{
  inp_mul[j] = 8 * *(_DWORD *)(arg + 4 * i);
  inp_mul[j + 1] = 7 * *(_DWORD *)(arg + 4 * i);
  j += 2;
}
for ( j = 0; j < 32; ++j )
{
  if ( inp_mul[j] > 400 )
    exit();
}
count = 0;
for ( j = 0; j < 32; ++j )
  arr_xor[j] = inp_mul[j] ^ *((char *)str + j);
for ( j = 0; j < 4; ++j )
  var_0[j] = arr_xor[j];
for ( j = 0; j < 4; ++j )
  var_4[j] = arr_xor[j + 4];
for ( j = 0; j < 4; ++j )
  var_8[j] = arr_xor[j + 8];
for ( j = 0; j < 4; ++j )
  var_12[j] = arr_xor[j + 12];
for ( j = 0; j < 4; ++j )
  var_16[j] = arr_xor[j + 16];
for ( j = 0; j < 4; ++j )
  var_20[j] = arr_xor[j + 20];
for ( j = 0; j < 4; ++j )
  var_24[j] = arr_xor[j + 24];
for ( j = 0; j < 4; ++j )
  var_28[j] = arr_xor[j + 28];
for ( j = 0; j < 4; ++j )
{
  cmp0[j] = var_4[j] ^ var_0[j];
  if ( cmp0[j] != arr0[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp1[j] = var_12[j] + var_8[j];
  if ( arr1[j] != cmp1[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp2[j] = var_16[j] - var_20[j];
  if ( arr2[j] != cmp2[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp3[j] = (char *)(var_28[j] ^ var_24[j]);
  if ( (char *)arr3[j] != cmp3[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp4[j] = (char *)(var_28[j] ^ var_4[j] ^ var_0[j]);
  if ( (char *)arr4[j] != cmp4[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp5[j] = (char *)(var_20[j] + var_12[j] + var_8[j]);
  if ( (char *)arr5[j] != cmp5[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp6[j] = (char *)(var_8[j] ^ var_4[j] ^ var_0[j]);
  if ( (char *)arr6[j] != cmp6[j] )
    exit();
  ++count;
}
if ( count != 28 )
  exit();
for ( j = 0; j < 32; ++j )
  flag[j] = LOBYTE(inp_mul[j]) ^ (j + LOBYTE(arr7[j]));
```

Script to solve: [get_inp.py](/inctf2019/tictoctoe/get_inp.py)

[frInpToFlag.py](/inctf2019/tictoctoe/frInpToFlag.py)

Flag: `inctf{w0W_Y0u_cr4ck3d_my_m3th0d}`

# English

## cliche-crackme

The input of this challenge (also a flag) is processed through 4 functions:

Function 1: Generating an buf[] array from input

![create_buf](/inctf2019/cliche_crackme/create_buf.png)

Function 2: Checking sum of all input's charaters

![check_inp](/inctf2019/cliche_crackme/check_inp.png)

Function 3: Checking sum of all buf[]'s charaters

![check_sum](/inctf2019/cliche_crackme/check_sum.png)

Function 4: Checking buf[]

![check_buf](/inctf2019/cliche_crackme/check_buf.png)

Script to solve: [solver.py](/inctf2019/cliche_crackme/solver.py)

Flag: `inctf{Th4ts_he11_l0t_0f_w0rk_w4s_it?}`

## Encrypt_

At first, I reverse the `drop.exe` file and easy to understand the work-flow of this small program:
- Firstly, it checks the file name by Check1 function
- Next, the input is encrypted by `Tranform` function -> `input1`
- Finally, `input1` is checked with filename and a given array of `Check2` function
Here is a script to solve `drop.exe` file:

Script to solve drop.exe: [get_inp.py](/inctf2019/encrypt/get_inp.py)

After passing `drop.exe` file, I have a file name [encrypterY8.exe](/inctf2019/encrypt/encrypterY8.exe). Reversing it a little bit then I found that this file is basically Encrypt AES 128
(Microsoft Enhanced RSA and AES Cryptographic Provider), using the key also a file name. Besides, the description tell us: image file is encrypted 2 times. So I decide to write some code to decrypt AES 128.  
This is my source code to decrypt AES 128:

Source Decrypt AES 128: [decrypt.cpp](/inctf2019/encrypt/decrypt.cpp)

Decrypt image file 2 times using the program above and we have Flag:

![flag](/inctf2019/encrypt/flag.png)

## TIC_TOC_TOE

At the create table function (`0x413AA0`):
- Human mark (X) from 1 to 16. The input range is from `0xA` to `0x19`
- Machine mark (O). The input range is from `0x1A` to `0x29`
(Summarize: input[i], if i is even -> human play; else machine play)

![inp0](/inctf2019/tictoctoe/inp0.png)
![inp1](/inctf2019/tictoctoe/inp1.png)

After that the input is processed at `0x41A0B0` function. This function do some encryption algorithms with input -> input1. Then it xor input1 with a given array -> Flag.

```c
str = '!@#sbjhdn5z6sf5gqc7kcd5mck7ld=&6';
j = 0;
for ( i = 0; i < 16; ++i )
{
  inp_mul[j] = 8 * *(_DWORD *)(arg + 4 * i);
  inp_mul[j + 1] = 7 * *(_DWORD *)(arg + 4 * i);
  j += 2;
}
for ( j = 0; j < 32; ++j )
{
  if ( inp_mul[j] > 400 )
    exit();
}
count = 0;
for ( j = 0; j < 32; ++j )
  arr_xor[j] = inp_mul[j] ^ *((char *)str + j);
for ( j = 0; j < 4; ++j )
  var_0[j] = arr_xor[j];
for ( j = 0; j < 4; ++j )
  var_4[j] = arr_xor[j + 4];
for ( j = 0; j < 4; ++j )
  var_8[j] = arr_xor[j + 8];
for ( j = 0; j < 4; ++j )
  var_12[j] = arr_xor[j + 12];
for ( j = 0; j < 4; ++j )
  var_16[j] = arr_xor[j + 16];
for ( j = 0; j < 4; ++j )
  var_20[j] = arr_xor[j + 20];
for ( j = 0; j < 4; ++j )
  var_24[j] = arr_xor[j + 24];
for ( j = 0; j < 4; ++j )
  var_28[j] = arr_xor[j + 28];
for ( j = 0; j < 4; ++j )
{
  cmp0[j] = var_4[j] ^ var_0[j];
  if ( cmp0[j] != arr0[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp1[j] = var_12[j] + var_8[j];
  if ( arr1[j] != cmp1[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp2[j] = var_16[j] - var_20[j];
  if ( arr2[j] != cmp2[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp3[j] = (char *)(var_28[j] ^ var_24[j]);
  if ( (char *)arr3[j] != cmp3[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp4[j] = (char *)(var_28[j] ^ var_4[j] ^ var_0[j]);
  if ( (char *)arr4[j] != cmp4[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp5[j] = (char *)(var_20[j] + var_12[j] + var_8[j]);
  if ( (char *)arr5[j] != cmp5[j] )
    exit();
  ++count;
}
for ( j = 0; j < 4; ++j )
{
  cmp6[j] = (char *)(var_8[j] ^ var_4[j] ^ var_0[j]);
  if ( (char *)arr6[j] != cmp6[j] )
    exit();
  ++count;
}
if ( count != 28 )
  exit();
for ( j = 0; j < 32; ++j )
  flag[j] = LOBYTE(inp_mul[j]) ^ (j + LOBYTE(arr7[j]));
```

Script to solve: [get_inp.py](/inctf2019/tictoctoe/get_inp.py)

[frInpToFlag.py](/inctf2019/tictoctoe/frInpToFlag.py)

Flag: `inctf{w0W_Y0u_cr4ck3d_my_m3th0d}`
