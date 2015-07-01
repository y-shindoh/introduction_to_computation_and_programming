#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.3の例題2

x = -0.1

x = float(x)
e = 0.001
n = 0

l = min(-1.0, x)
h = max(1.0, x)
if x < 0:
    h = 0.0
else:
    l = 0.0

r = (l + h) / 2.0

while abs(r ** 3 - x) > e:
    print '[' + str(n) + ']', 'low =', str(l) + ', high =', str(h) + ', ans =', str(r)
    n += 1
    if r ** 3 < x:
        l = r
    else:
        h = r
    r = (l + h) / 2.0

print r, 'is close to cube root of', x
