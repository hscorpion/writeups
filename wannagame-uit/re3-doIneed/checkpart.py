#!/usr/bin/env python

from z3 import *
s0 = Solver()
s1 = Solver()
s2 = Solver()
s3 = Solver()
v0, v1, v2, v3 = Reals('v0 v1 v2 v3')

# countSTR = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#""'
# table check - special value
    # 2e -> -E7
    # 5b -> -F1
    # 40 -> -EF
    # 7e -> -F9
    # 20 -> -fa
def solve(s):
    if s.check() == sat:
        print('sat')
        print(s.model())
    else:
        print('unsat')

### i == 0
s0.add(v0 + v1 + v2 + v2 + 3*v3 == -2.0)
s0.add(v1 + v1 + v0 + v0 + 3*v2 +5*v3 == -2.0)
s0.add(3*v0 - v1 + v2 + v2 + v3 == 2)
s0.add(6*v1 + v0 + v0 + v2*6 + 13*v3 == -10)
solve(s0)

# [v2 = 0, v0 = 2, v3 = -2, v1 = 2]
# key = 3232300b


### i == 1

v10 = v0 / 5
v11 = v1 / 5
v12 = v2 / 5
v13 = v3 / 5
#ghidra
s1.add(v10 - v11 + v12 + v13 == 1)
s1.add(v10 + v10 + v11 + v12 + v13 * 3.00000000 == 8)
s1.add(v10 * -3.00000000 + v11 + v11 - v12 == -5)
s1.add(v11 * 4.00000000 + v10 * 4.00000000 + v12 * 3 + v10 * 4.00000000 == 14)
solve(s1)

#[v2 = -18, v0 = 15, v3 = 9, v1 = 1]
# key = 66313f39


### i = 2
v20 = v0 / 5
v21 = v1 / 5
v22 = v2 / 5
v23 = v3 / 5
s2.add(v20 + v21 + v22 + v23 == 5)
s2.add((v21 + v21 + v20 + v20) - v22 + v23 * 3.00000000 == 10)
s2.add(v20 * -2.00000000 - v21 + v22 + v23 == 3)
s2.add(v21 * 3 + v20 + v20 + v22 * 4.00000000 + v23 + v23 == 11)
solve(s2)

# [v2 = 6, v0 = 8, v3 = 18, v1 = -7]
# key = 387e3669


### i = 3
v30 = v0 / 10
v31 = v1 / 10
v32 = v2 / 10
v33 = v3 / 10
s3.add((v31 + v31 + v30) - v32 + v33 == 0)
s3.add((v30 + v30) - v31 * 3.00000000 + v32 * 3.00000000 == 3)
s3.add(v30 * -4.00000000 + v31 + v32 * 3.00000000 + v33 + v33 == -1)
s3.add(v30 + v31 + v32 + v33 == 2)
solve(s3)

# v2 = 16, v0 = 9, v3 = -17, v1 = 12
# key = 39636740
