# PlaidCTF 2019

## can you guess me (Misc 100 pts)
Source:
```python
    val = 0
    inp = input("Input value: ") #input
    count_digits = len(set(inp))
    if count_digits <= 10:          # Make sure it is a number
        val = eval(inp)
    else:
        raise
    if val == secret_value_for_password:
        print(flag)
```
Ta có thể dễ dàng thấy input bị hạn chế không quá 10 kí tự khác nhau, và sẽ được xử lí qua hàm eval(). Nên input sẽ là 1 đoạn code nhỏ tận dụng hàm eval() để in ra flag.
```python
Input value: help(flag)
No Python documentation found for 'PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

Nope. Better luck next time.
```

Còn đây là 1 input khác do teamate nghĩ ra:
```python
Input value: print(vars())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fed04e799e8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/guessme/can-you-guess-me.py', '__cached__': None, 'exit': <built-in function exit>, 'secret_value_for_password': 'not even a number; this is a damn string; and it has all 26 characters of the alphabet; abcdefghijklmnopqrstuvwxyz; lol', 'flag': 'PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}', 'exec': <function exec at 0x7fed04dc2158>, 'val': 0, 'inp': 'print(vars())', 'count_digits': 10}
Nope. Better luck next time.
```

## i can count (Reversing 50 pts)
Tại main ta có thể thấy sau flag_buf sẽ được tăng lên 1 sau đó qua hàm check_flag, và cứ thế lặp lại. Nên hàm trọng tâm sẽ là check_flag.
Tại hàm check_flag có được định dạng của flag, đơn giản bây giờ chỉ cần biết giá trị của flag_buf:
```c
if ( i > 19 ){
      printf("PCTF{%s}\n", flag_buf);
      exit(0);
}
```
Ta sẽ thấy thêm từng kí tự trong flag_buf sẽ bị mã hoá và cuối cùng check giá trị với check_buf.
```c
if ( *((_BYTE *)check_buf + i) != (BYTE1(flag_buf_encoded) ^ (unsigned __int8)flag_buf_encoded) )
      break;
```
Giá trị của check_buf
```assembly
.text:56601F64                 mov     edx, (check_buf - 56604000h)[esi]
.text:56601F6A                 mov     eax, [ebp+i]
.text:56601F6D                 add     eax, edx
.text:56601F6F                 movzx   edx, byte ptr [eax]
```
```assembly
gdb-peda$ x/20b $eax
0x5655637d:     0x93    0x42    0x05    0x93    0x04    0xcd    0x7f    0x78
0x56556385:     0x42    0x78    0x05    0xcd    0xcd    0x42    0x42    0x78
0x5655638d:     0xcd    0xb5    0xb5    0x89
```

Vậy giờ ta chỉ cần debug biết từng giá trị của flag_buf sau khi đã mã hoá:
```assembly
0 -> 0x42
1 -> 0xCD
2 -> 0x93
3 -> 0xCA
4 -> 0x04
5 -> 0x05
6 -> 0x78
7 -> 0xB5
8 -> 0x29
9 -> 0x7F
```

Flag:
```
PCTF{2052419606511006177}
```

## Plaid Party Planning III (Reversing 500 pts)
Nói thật thì bài này 500pts nhưng thật sự rất dễ không biết tác giả của ý đồ gì khác hay không.

```c
v32 = "bluepichu";
v36 = "mserrano";
sleep((__int64)&v32, 5uLL);
printt(
    &v32,
    (__int64)"Sorry we're late. There wasn't enough meat here, so I decided to go\n\tmake some spaghetti with alfredo sauce, mushrooms, and chicken at home.", v2, v3, v4, v5, a2);
sleep((__int64)&v32, 1uLL);
printt(&v36, (__int64)"I decided to tag along because, as you know, cheese is very desirable.", v6, v7, v8, v9);
sleep((__int64)&v36, 1uLL);
printt(&v32, (__int64)"And I bought a ton of extra parmesan!", v10, v11, v12, v13);
sleep((__int64)&v32, 5uLL);
printt(&v36, (__int64)"Anyway, we brought you guys a gift.", v14, v15, v16, v17);
sleep((__int64)&v36, 1uLL);
printt(&v32, (__int64)"It's a flag!", v18, v19, v20, v21);
sleep((__int64)&v32, 5uLL);
ptr = sub_558797A30524(a1);
sprintt(
    (_QWORD *)(a1 + 256),
    (__int64)"Let me take a look. It seems to say\n\tPCTF{%s}.",
    (__int64)ptr,
    a1 + 256,
    v23,
    v24);
```
Chỉ cần ta gặp được 2 vị khách đến trễ này là có được flag.
```c
  for ( i = 0; i <= 14; ++i ){
    if ( pthread_create((pthread_t *)&th[i], 0LL, start_routine, (void *)(a1 + 32LL * i)) )
      abort();
  }
  for ( j = 0; j <= 14; ++j ){
    if ( pthread_join(th[j], 0LL) )
      abort();
  }
```
Để ý chúng ta sẽ thấy 2 vòng for này khiến chương trình của chúng ta bị cancel. Vậy đơn giản chỉ cần bypass qua đoạn code này là ta đã có được flag...
```
Alphabetical it is, I guess.
Simulating the dinner...

bluepichu: Sorry we're late. There wasn't enough meat here, so I decided to go
        make some spaghetti with alfredo sauce, mushrooms, and chicken at home.
mserrano: I decided to tag along because, as you know, cheese is very desirable.
bluepichu: And I bought a ton of extra parmesan!
mserrano: Anyway, we brought you guys a gift.
bluepichu: It's a flag!
strikeskids: Let me take a look. It seems to say
        PCTF{1 l1v3 1n th3 1nt3rs3ct1on of CSP and s3cur1ty and parti3s!}.
strikeskids: Hopefully that's useful to someone.
```

## A Whaley Good Joke (Misc 150 pts)
```sh
$ file pctf-whales_169aeb74f82dcdceb76e36a6c4c22a89 
pctf-whales_169aeb74f82dcdceb76e36a6c4c22a89: gzip compressed data, last modified: Sat Apr 13 21:56:25 2019, from Unix, original size 119234560
```
Ở đây ta thấy đây file `tar.gz`, khi extract ta sẽ thấy thư mục và file với tên đã là mã sha256, file `manifest.json` và `repositories`. Tìm hiểu thêm vào các file thì mình biết đây là 1 docker imagine nhưng khi thử chạy trên docker thì không được.
Sau đó đọc trong file `manifest.json` ta thấy 2 layer cuối cùng là `24d12bbeb0a9fd321a8decc0c544f84bf1f6fc2fd69fa043602e012e3ee6558b` và `b94e5d83dbbff95e883f0f53bcf47c017471b13d81325697be6e22cdc8c369aa`. Vì lúc extract mình đã bị lỗi không thể ra được file `layer.tar` trong `24d12bb...` nên xem trong `b94e...` thì ta thấy file `flag.sh`
```sh
#!/bin/bash

for i in {1..32}
do
    test -f $i
    if [[ $? -ne 0 ]]
    then
        echo "Missing file $i - no flag for you!"
        exit
    fi
done

echo pctf{1_b3t$(cat 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32)}
```

Vậy ta chỉ cần tìm thêm các file `1` `2`... nữa nhưng vì ở có quá nhiều file trùng nhau, và cũng không thể biết được thứ tự thực hiện nên mình quyết định brute force.
```python
a1 = ['t', 'k', '_']
a2 = ['t', '4', 'u']
a3 = ['z', '_']
a4 = ['a', 'c', 's', '_']
a5 = ['l', 'o', 'u']
a6 = ['u', 'k']
a7 = ['l', 'z']
a8 = ['t', 'g', 'd']
a9 = ['n']
a10 = ['_', '7', 'n']
a11 = ['0', 't', '7', '_', 'v']
a12 = ['s', 'c']
a13 = ['0']
a14 = ['l', 'n']
a15 = ['t', 'k']
a16 = ['4', 'n', '3']
a17 = ['q', 'm', 'i']
a18 = ['6', '7', 'n']
a19 = ['_', 't', 'n', '8', '3']
a20 = ['e', '_', 'r']
a21 = ['_', 't']
a22 = ['u']
a23 = ['i', 't', 'r']
a24 = ['2', 'e', '_']
a25 = ['l', '_']
a26 = ['4', '7', '_']
a27 = ['u']
a28 = ['_', 'b', 'g']
a29 = ['h']
a30 = ['t', '_']
a31 = ['e', '3']
a32 = ['r']

flag = 'pctf{1_b3t'
```
Từ đây dữ kiện trên thực hiện bf và sẽ đoán được flag là `pctf{1_b3t_u_couldnt_c0nt4in3r_ur_l4ught3r}`
