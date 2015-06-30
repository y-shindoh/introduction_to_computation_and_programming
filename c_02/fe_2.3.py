#! /usr/bin/env python
# -*- coding: utf-8; tab-width: 4 -*-
# 「Introduction to Computation and Programming Using Python」の§2.2の練習問題の回答

x = 1
y = 2
z = 3
a = 0
c = '-'

if x % 2 != 0:
    a = x
    c = 'x'

if y % 2 != 0:
    if a < y:
        a = y
        c = 'y'

if z % 2 != 0:
    if a < z:
        a = z
        c = 'z'

if c != '-':
    print c + ' is the largest odd number.'
else:
    print 'Not found odd numbers.'
