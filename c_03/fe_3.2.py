#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.2の練習問題

s = raw_input('Enter an integer: ')
r = 0.0

for n in s.split(','):
    r += float(n)

print r
