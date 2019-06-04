# Facebook CTF 2019

## imageprot

Bài này mình quyết định debug để hiểu rõ flow của chương trình nên làm khá tốn thời gian.

Đầu tiền main gọi `std::rt::lang_start_internal::h578aadb15b8a79f8` - hàm này đơn giản chỉ là obfuscate để dấu việc trực tiếp gọi hàm `imageprot::main::h60a99eb3d3587835` (hàm main thật sự)

Trong hàm main chính này, sử dụng hàm `imageprot::decrypt::h56022ac7eed95389` làm phương thức obfuscate chính.

Hàm `imageprot::decrypt::h56022ac7eed95389()` này nhận 3 argument và tiến hành decrypt. Thuật toán khá đơn giản là decode_base64(arg3) XOR với arg2

I spent a lot of time to debugging to clearly understanding the control flow of the program.

Firstly, the main() function calls `std::rt::lang_start_internal::h578aadb15b8a79f8` function - this function just do the work that hidding the direct `imageprot::main::h60a99eb3d3587835` function call (which is the real main() function) by using obfuscation technique.

This real main() function using `imageprot::decrypt::h56022ac7eed95389` function as the major obfuscation method. So what does `imageprot::decrypt::h56022ac7eed95389` function do?

The answer is this function takes 3 arguments then start to decrypt by using a simple algorithm: decode_base64(arg3) XOR arg2

```c
base64::decode::decode::h5b239420e35447bb(&a3_base64, arg3);
```

```c
decode_i = *(_BYTE *)(arg3_base64_ + i) ^ *(_BYTE *)(arg2_ + i % len_arg2);
```

Ở vòng lặp đầu tiên, chương trình sử dụng hàm `imageprot::decrypt::h56022ac7eed95389` decrypt ra 4 string là `gdb`, `vmtoolsd`, `vagrant` và `VBoxClient` (Cái này mình không chắc nhưng lúc debug tiếp thì có 1 đoạn check 4 string này, có vẻ là require để chạy chương trình)

Ngay sau đó, chương trình tiếp tục sử dụng hàm `imageprot::decrypt::h56022ac7eed95389` decrypt ra 1 url là `http://challenges.fbctf.com/vault_is_intern` sau đó gọi hàm `imageprot::get_uri::h3e649992b59ca680` để get url này. Vì trang này đã down nên chương trình sẽ ngắt tại đây (lí do chương trình không thể chạy)

On the first loop, the program uses `imageprot::decrypt::h56022ac7eed95389` function and decrypt. It returns 4 strings: `gdb`, `vmtoolsd`, `vagrant` and `VBoxClient` (I'm not sure about this but when I continue debugging I found a check 4 strings part, it seems like a requirement of running the program).

Shortly, the program continuing uses `imageprot::decrypt::h56022ac7eed95389()` function. It returns an url. Then the program call `imageprot::get_uri::h3e649992b59ca680` function to get this url. Because the site `http://challenges.fbctf.com/vault_is_intern` is down so the program will break at this point.

![vault_is_intern](https://i.imgur.com/IKbS0Uv.png)

Tiếp theo hoàn toàn tương tự với 1 url khác `http://httpbin.org/status/418` nhưng trang hoàn toàn bình thường nên sẽ lấy dữ liệu từ trang này.

Simmilar to a different url but now the site is available so program can get its data.

![httpbin](https://i.imgur.com/tzLkhVo.png)

Cuối cùng, hàm `imageprot::decrypt::h56022ac7eed95389()` xử lí 1 mã base64 khá lớn với dữ liệu được get từ `http://httpbin.org/status/418` (mình thấy sau sau đó có gọi một số hàm md5 tưởng vẫn chưa hết nên lan man đoạn cuối này khá lâu)

Finally, the `imageprot::decrypt::h56022ac7eed95389()` function analyzes a quite large base64 code with the data receive from `http://httpbin.org/status/418` (After that I found some md5 functions that makes me think the program still not end. Hence, it took me many times to completing the challenge).

![end](https://i.imgur.com/tGpzYP5.png)

Vì đoạn mã base64 khá lớn và đề cũng yêu cầu `...get the photo back out` nên mình đoán đây là 1 file. Nên tiến hành export nó ra và giãi mã nó.

Because the base64 code is fairly large and the desciprtion of the challenge is `...get the photo back out` so I guessed this is a file. Export it then decode to get flag.

Đây là đoạn script giải mã:

Here is a script to decode it:

[restore-image.py](/fbctf2019/imageprot/restore-image.py)

![image-back](https://raw.githubusercontent.com/hscorpion/writeups/master/fbctf2019/imageprot/image-back.png)

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
Hàm main này đơn giản chỉ là check argument với `my_sUp3r_s3cret_p@$$w0rd1` và in ra 1 flag giả là `Nope{Lolz_this_isnt_the_flag...Try again...}`. Stuck đoạn này khá lâu thì có 1 hint của anh m3kk_kn1ght: `Binary check debugger by using ptrace. Ptrace call in sub_4005A0(a function in init_array of elf)`. `Chạy bình thường với chạy debug nó khác nhau -> Ko bình thường. Chắc là có đoạn check debug ở đâu đó mà main không có đoạn check debug nên nó nằm ở chỗ khác.`

Sau đó mình tìm các initialization functions trong `.init_array`, thấy hàm `sub_4005A0` có sử dụng hàm `ptrace` (sub__44EC50) để anti-debug nên tiến hành debug hàm này. (Để bypass qua `ptrace` có rất nhiều cách, ở đây mình đơn giản là set cờ ZF = 0)

Sau khi bypass qua ta sẽ thấy binary đọc file `/tmp/key.bin` và check dữ liệu từ key.bin trước khi in flag. Vì mình muốn lấy flag nên bypass qua thay vì decrypt để biết require của key.bin

This main() function basically checking argument with `my_sUp3r_s3cret_p@$$w0rd1` and printing a fake flag: `Nope{Lolz_this_isnt_the_flag...Try again...}`. I'd got stuck for a long time until got a hint from @m3kk_kn1ght: `Binary check debugger by using ptrace. Ptrace call in sub_4005A0(a function in init_array of elf)`.

After that I looked for initialization functions on `.init_array`, then I found `sub_4005A0` function used `ptrace` (sub_44EC50) function to anti-debug so I started to debug this function (There are many ways to bypass through `ptrace` function, basically I set ZF flag value to zero)

After bypassing ptrace function successfully, easily found that the binary read file `/tmp/key.bin` and check data from key.bin before print the flag. In conclusion, to get the flag, all the thing we need is bypass the check data from `/tmp/key.bin` part.     


access file /tmp/key.bin
![/tmp/key.bin](https://i.imgur.com/WNjPu38.png)
check /tmp/key.bin data
![check-key-bin-data](https://i.imgur.com/V5Sl4qV.png)
```
=========================================================
[11] Accepting connection from 192.168.85.1...
Warning: Bad ELF byte sex 2 for the indicated machine
fb{7h47_W4sn7_S0_H4Rd}
```

## go_get_the_flag
Bài này khá đơn giản, vì cho sau nên đoán là này chỉ để cho điểm.

Binary là dạng ELF đã tripped. Nên mình xử lí bằng `radare2`

Check function tìm được các hàm chính:

This challenge is quite simple. The binary file has a ELF format and it was tripped. And so I decided to use `radare2` to analyze it.  

To begin with, I checked function and found many important function below:
```python
0x004916b0  341 sym.go.main.main
0x00491810  537 sym.go.main.checkpassword
0x00491a30 1092 sym.go.main.decryptflag
0x00491e80  151 sym.go.main.wrongpass
0x00491f20  117 sym.go.main.init
```

Ở hàm `sym.go.main.checkpassword`, ta thấy có kiểm tra argument qua hàm memequal với `s0_M4NY_Func710n2!`

Then, I found that at `sym.go.main.checkpassword` function had a check argument through memequal with `s0_M4NY_Func710n2!`

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
Now it's easy to get flag:

```sh
[hsc@hscorpion dist]$ ./ggtf s0_M4NY_Func710n2!
fb{.60pcln74b_15_4w350m3}
```
