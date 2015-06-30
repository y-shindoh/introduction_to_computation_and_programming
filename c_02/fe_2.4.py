#! /usr/bin/env python
# -*- coding: utf-8; tab-width: 4 -*-
# 「Introduction to Computation and Programming Using Python」の§2.4の練習問題の回答

input = raw_input('Enter integer(s): ')

numberes = input.split()
odd_number = 0

for n in numberes:
    number = int(n)
    if 0 < number % 2:
        if odd_number < number:
            odd_number = number

if 0 < odd_number:
    print 'The largest odd number:', odd_number
else:
    print 'Not found odd number.'
