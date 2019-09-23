from z3 import *
s = Solver()
n = 16
X = [BitVec('x_%s' % i, 8) for i in range(n)]
s.add(X[1] == 40)
s.add(X[0] == 20)
const = '!@#sbjhdn5z6sf5gqc7kcd5mck7ld=&6'

cmp0 = [0x9b, 0xcf, 0x1db, 0x1b9]
cmp1 = [0xf9, 0x174, 0x27f, 0x1a7]
cmp2 = [0xce, 0xb1, 0xa, 0x1b]
cmp3 = [0xbf, 0x9b, 0x1f1, 0x7e]
cmp4 = [0x37, 0x5d, 0x11d, 0x14b]
cmp5 = [0x104, 0x1b3, 0x3a4, 0x22a]
cmp6 = [0xad, 0xb7, 0x99, 0x9e]

#dk0
z = []
for i in range(16):
  z.append(8 * X[i])
  z.append(7 * X[i])

#for i in range(32):
#  s.add(z[i] <= 400)

#dk1
t = []
for i in range(32):
  t.append(z[i] ^ ord(const[i]))
for i in range(4):
  s.add(t[4+i] ^ t[i] == cmp0[i])
  s.add(t[12+i] + t[8+i] == cmp1[i])
  s.add(t[16+i] - t[20+i] == cmp2[i])
  s.add(t[28+i] ^ t[24+i] == cmp3[i])
  s.add(t[28+i] ^ t[4+i] ^ t[i] == cmp4[i])
  s.add(t[20+i] + t[12+i] + t[8+i] == cmp5[i])
  s.add(t[8+i] ^ t[4+i] ^ t[i] == cmp6[i])

for i in range(0,8,2):
  s.add(X[i] >= 0xa, X[i] <= 0x19)
  s.add(X[i + 1] >= 0x1a, X[i + 1] <= 0x29)

pos = []
if s.check() == sat:
    m = s.model()
    for i in range(n):
        pos.append(m[X[i]])
    print(pos)
else:
    print("unsat")
