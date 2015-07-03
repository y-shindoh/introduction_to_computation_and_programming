#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§4.1の例題

x = 123456789
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (low + high) / 2.0

while abs(ans ** 2 - x) >= epsilon:
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2.0

print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x
