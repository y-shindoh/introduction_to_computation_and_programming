#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 「Introduction to Computation and Programming Using Python」の§4.1.2の例題

def printName(firstName, lastName, reverse=False):
    if reverse:
        print lastName + ', ' + firstName
    else:
        print firstName, lastName

printName('Olga', 'Puchajerova')
printName('Olga', 'Puchajerova', True)
printName('Olga', 'Puchajerova', False)
printName('Olga', 'Puchajerova', reverse=False)
printName('Olga', lastName='Puchajerova', reverse=False)
printName(lastName='Puchajerova', firstName='Olga', reverse=False)
