#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.1の練習問題

x = raw_input('Enter an integer: ')

x = int(x)
y = int(abs(x));
flag = False

for i in range(6):
    r = 0
    while r ** i < y:
        r += 1
        if i == 0:
            break
    if r ** i == y:
        if x < 0 and i % 2 != 0:
            r *= -1
            print r, '**', i, '=', x
            flag = True
        elif 0 <= x:
            print r, '**', i, '=', x
            flag = True

if not flag:
    print x, 'has no roots.'
