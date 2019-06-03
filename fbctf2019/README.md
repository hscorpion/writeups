# Facebook CTF 2019

## SOMBRERO ROJO (part 1)
main:
```c
if ( argc <= 1 ) {
  printt("Give me some args!", argv);
  returnn(1LL);
}
if ( argc == 2 ) {
  decod3((__int64)&fake_flag);
  decod3((__int64)&check_str);
  if ( (unsigned int)str_cmp((__int64)&check_str, (__int64)argv[1]) )
  {
    pr1nt(1, (__int64)"Hmmm...");
    printt("Try again!", "Hmmm...");
    returnn(1LL);
  }
  argv = (const char **)"%s{%s}\n";
  v3 = (__int16 *)1;
  LOBYTE(pre_fake_flag) = pre_fake_flag + 8;
  BYTE1(pre_fake_flag) += 3;
  BYTE2(pre_fake_flag) += 15;
  HIBYTE(pre_fake_flag) -= 2;
  LOBYTE(v11) = v11 - 2;                      // decode str to Nope
  pr1nt(1, (__int64)"%s{%s}\n", &pre_fake_flag, &fake_flag);
}
else {
  v3 = &v8;
  v8 = 10554;
  v9 = 0;
  printt(&v8, argv);                          // print ':)'
}
```
Hàm main này đơn giản chỉ là check argument với `my_sUp3r_s3cret_p@$$w0rd1` và in ra 1 flag giả là `Nope{Lolz_this_isnt_the_flag...Try again...}`
Stuck đoạn này khá lâu thì có 1 hint của anh m3kk_kn1ght: `m3kk_kn1ght: Binary check debugger by using ptrace. Ptrace call in sub_4005A0(a function in init_array of elf)`
Sau đó mình tìm các hàm tiền khởi tạo ở .init_array thấy hàm sub_4005A0 có sử dụng hàm ptrace (sub__44EC50) để antidebug nên tiến hành debug hàm này để bypass qua ptrace có rất nhiều cách, ở đây mình đơn giản là set cờ ZF = 0
Sau khi bypass qua ta sẽ thấy binary đọc file /tmp/key.bin và check trước khi in flag vì mình muốn lấy flag nên bypass qua thay vì decrypt để biết require của key.bin
![/tmp/key.bin](https://i.imgur.com/WNjPu38.png)
```
=========================================================
[11] Accepting connection from 192.168.85.1...
Warning: Bad ELF byte sex 2 for the indicated machine
fb{7h47_W4sn7_S0_H4Rd}
```
## go_get_the_flag
Bài này khá đơn giản, vì cho sau nên đoán là này chỉ để cho điểm.
Binary là dạng ELF đã tripped. Nên mình xử lí bằng radare2
Check function tìm được các hàm chính:
```python
0x004916b0  341 sym.go.main.main
0x00491810  537 sym.go.main.checkpassword 
0x00491a30 1092 sym.go.main.decryptflag
0x00491e80  151 sym.go.main.wrongpass
0x00491f20  117 sym.go.main.init
```
Ở hàm sym.go.main.checkpassword, ta thấy có kiểm tra argument qua hàm memequal với `s0_M4NY_Func710n2!`
```assembly
0x00491868      488b8c24c800.  mov rcx, qword [arg_c8h]    ; [0xc8:8]=-1 ; 200                                                                  
0x00491870      48890c24       mov qword [rsp], rcx                                                                                             
0x00491874      488d15d05803.  lea rdx, [0x004c714b]       ; "s0_M4NY_Func710n2!streams pipe errorsystem page size (tracebackancestorsuse of clo
0x0049187b      4889542408     mov qword [var_8h], rdx                                                                                          
0x00491880      4889442410     mov qword [var_10h], rax                                                                                         
0x00491885      e8660bf7ff     call sym.go.runtime.memequal ;[2]                                                                                
0x0049188a      807c241800     cmp byte [var_18h], 0       ; [0x18:1]=255 ; 0                                                                   
0x0049188f      74c2           je 0x491853
```
```sh
[hsc@hscorpion dist]$ ./ggtf s0_M4NY_Func710n2!
fb{.60pcln74b_15_4w350m3}
```
