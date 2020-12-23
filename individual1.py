# 17. Дано предложение. Определить число вхождений в него некоторого символа.
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    s = input('Введите предложение: ')
    simb = input('Введите искомый символ: ')
    counter = 0
    for i in range (0, len(s)):
        if s[i] == simb:
            counter += 1
    print("Число вхождений символа", simb, ' - ', counter)