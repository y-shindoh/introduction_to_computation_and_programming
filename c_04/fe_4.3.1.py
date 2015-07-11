#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§4.3.1の練習問題

def fib(n):
    """Assumes n an int >= 0
       Returns Fibonacci of n"""
    if n == 2:
        print '-'	# 3回呼ばれる
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = fib(5)
print 'fib of 5 =', n
