#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.3の例題

x = 25
epsilon = 0.01
step = epsilon ** 2
numGuesses = 0
ans = 0.0

while abs(ans ** 2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1

print 'numGuesses =', numGuesses

if abs(ans ** 2 - x) >= epsilon:
    print 'Failed on square root of', x
else:
    print ans, 'is close to square root of', x

