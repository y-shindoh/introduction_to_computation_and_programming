#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.4の練習問題

bits = '10011'
value = 0

for v in bits:
    print v
    value = value * 2 + int(v)

print bits, '->', value
