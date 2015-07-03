#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§3.3の例題2

def isIn(short_string, long_string):
    m = len(long_string)
    n = len(short_string)
    for i in range(m):
        if long_string[i] == short_string[0]:
            flag = True
            for j in range(n):
                if long_string[i+j] != short_string[j]:
                    flag = False
                    break
            if flag:
                return True
    return False

if isIn('test', 'Test test'):
    print 'True'
else:
    print 'False'
