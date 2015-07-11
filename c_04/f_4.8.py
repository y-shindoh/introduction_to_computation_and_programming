#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§4.3.2の例題

def isPalindrome(s):
    """Assume s is a str
       Returns True if the letters in s from a palindrome;
          False otherwise. Non-letters and capitalization are ignored."""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


input = 'aAbBcBBaA'

print 'Is string "', input, '" a palindrome?'
print '=>', isPalindrome(input)
