#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 8. Дано предложение. Удалить из него все буквы о, стоящие на нечетных местах.

if __name__ == '__main__':
    s = input('Введите предложение: ')
    s_new = ''
    for i in range(0, len(s)):
        if not (s[i] == 'о' and i % 2):
            s_new += s[i]
    print(s_new)
