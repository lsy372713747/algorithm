# coding:utf-8
'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：
在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
的结果满足如下条件，即是结果。
循环计算即可，判断成立即可输出。首先要判断是否为正整数。引入math模块算平方根
'''

#第一种解法 判断x，y开方同时为整数即可
import math
from math import sqrt
print '解法一'
for i in range(100000):
    if(math.sqrt(i+100)-int(math.sqrt(i+100))==0):
        x = int(math.sqrt(i + 100)) # 开方求x x为浮点数
        if (math.sqrt(i + 268) - int(math.sqrt(i + 268)) == 0):
            y = int(math.sqrt(i + 268))  # 开方求x x为浮点数
            print x,y
            print '该数为%d' %i

#第二种 直接求x*x-y*y=168
print '解法二'
for i in range(10000):
    for j in range(1000):
        if(i*i-j*j==168):
            print i,j
            print '该数为%d' %(i*i-268)

#第三种 标准解法
print '解法三'
for i in range(100000):
    if(math.sqrt(i+100)-int(math.sqrt(i+100))==0):
        x = int(math.sqrt(i + 100)) # 开方求x x为浮点数
        if (math.sqrt(i + 268) - int(math.sqrt(i + 268)) == 0):
            y = int(math.sqrt(i + 268))  # 开方求x x为浮点数
            if(x*x==i+100 and y*y==i+268):
                print x, y
                print '该数为%d' % i

#第四种 
i=1
while 1:
	a, b = i + 100, i + 268
	x, y = int(sqrt(a)), int(sqrt(b))
	if x**2==a and y**2==i+268:
  		print "%ld" % i
		i+=1