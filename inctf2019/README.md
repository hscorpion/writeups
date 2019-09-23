# InCTF 2019

## cliche_crackme

Bài này input là flag được kiểm tra qua 3 function

Tạo mảng buf từ input:

![create_buf](/inctf2019/cliche_crackme/create_buf.png)

Check tổng các kí tự của input:

![check_inp](/inctf2019/cliche_crackme/check_inp.png)

Check tổng các kí tự của buf:

![check_sum](/inctf2019/cliche_crackme/check_sum.png)

Check buf:

![check_buf](/inctf2019/cliche_crackme/check_buf.png)

Script to solve: [solver.py](/inctf2019/cliche_crackme/solver.py)

Flag: `inctf{Th4ts_he11_l0t_0f_w0rk_w4s_it?}`

## Encrypt

Reverse file `drop.exe` đơn giản ta thấy, nó check tên file qua hàm `Check1` và sau đó input được mã hoá qua hàm `Transform` check với tên file và 1 mảng cho sẵn ở hàm `Check2`

Script to solve drop.exe: [get_inp.py](/inctf2019/encrypt/get_inp.py)

Sau khi pass qua `drop.exe` thì nó drop ra 1 file [encrypterY8.exe](/inctf2019/encrypt/encrypterY8.exe). Reverse sơ qua thì file này đơn giản là Encrypt AES 128 (Microsoft Enhanced RSA and AES Cryptographic Provider) sử dụng với key là tên file mà đề cho là file đã được encrypt 2 lần nên mình code lại 1 Decrypt AES 128 và tiến hành decrypt file ảnh 2 lần và ra flag.

Source Decrypt AES 128: [decrypt.cpp](/inctf2019/encrypt/decrypt.cpp)

Flag:

![flag](/inctf2019/encrypt/flag.png)
