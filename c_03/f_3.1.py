#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.1の例題

x = raw_input('Enter an integer: ')

x = int(x)
y = int(abs(x));
r = 0

while r ** 3 < y:
    r += 1

if r ** 3 == y:
    if x < 0:
        r *= -1
    print 'Cube root of', x, 'is', r, '.'
else:
    print x, 'is not a perfect cube.'
