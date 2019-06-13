# -*- coding: utf-8 -*-

"""
一、有一个整数 a 求列表b中的两个元素和等于a
"""
b = [1,2,3,4,5,6]
a = 7

for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if b[i] + b[j] == a:
            print("找到 %d-%d"%(b[i], b[j]))
