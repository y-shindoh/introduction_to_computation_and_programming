#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.1の練習問題

x = raw_input('Enter an integer: ')

x = int(x)
y = int(abs(x));


for r in range(y + 1):
    if r ** 3 >= y:
        break

if r ** 3 == y:
    if x < 0:
        r *= -1
    print 'Cube root of', x, ':', r
else:
    print x, 'is not a perfect cube.'
