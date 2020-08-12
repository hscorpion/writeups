#!/usr/bin/env python

from z3 import *
s = Solver()

n = 25
X = [BitVec('x_%s' % i, 8) for i in range(n)]

def checksum(hexcode, i, num):
    return hexcode[i + num*4] == hexcode[i + num*3] ^ hexcode[i + num*2] ^ hexcode[i + num] ^ hexcode[i]

s.add(X[0] == 0x32)
s.add(X[1] == 0x32)
s.add(X[2] == 0x30)
s.add(X[3] == 0xb)

s.add(X[5] == 0x66)
s.add(X[6] == 0x31)
s.add(X[7] == 0x3f)
s.add(X[8] == 0x39)

s.add(X[10] == 0x38)
s.add(X[11] == 0x7e)
s.add(X[12] == 0x36)
s.add(X[13] == 0x69)

s.add(X[15] == 0x39)
s.add(X[16] == 0x63)
s.add(X[17] == 0x67)
s.add(X[18] == 0x40)

for i in range(5):
    s.add(checksum(X, i, 5))
    s.add(checksum(X, 5*i, 1))

if s.check() == sat:
    print('sat')
    print(s.model())
else:
    print('unsat')

# 3232300b3b
# 66313f3951
# 387e366919
# 396367407d
# 551e5e1b0e
