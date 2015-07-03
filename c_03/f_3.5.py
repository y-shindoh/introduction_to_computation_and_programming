#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.5の例題

# Newton-Raphson for square root
# Find x such that x ** 2 - 24 is within epsilon of 0

epsilon = 0.01
k = 123456789.0
guess = k / 2.0
c = 1

while abs(guess * guess - k) >= epsilon:
    print '[' + str(c) + ']', guess
    guess = guess - (((guess ** 2) - k) / (2 * guess))
    c += 1

print 'Square root of', k, 'is about', guess
