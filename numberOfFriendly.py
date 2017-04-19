# coding: utf-8
"""
220 的全部约数（除掉本身）1 2 4 5 10 11 20 22 44 55 110  相加是 284
284 的全部约数（除掉本身）1 2 4 71 142 相加是 220
另外一个正整数全部约数之和还等于自身， 这个数被称为自私数 例如： 6
请写一个函数，传入一个参数max_num，将小于max_num的全部友好数对打印在屏幕上
"""

def youhao(max_num):
	shu_list = []
	for shu in range(1, max_num):
		result=[a for a in range(1,shu+1) if shu%a==0]
		sums = sum(result[:-1])
		d = {}
		d[shu] = sums
		shu_list.append(d)
	for x in shu_list:
		for y in shu_list:
			if x.keys()[0] == y.values()[0] and x.values()[0] == y.keys()[0] and x.keys()[0] != y.keys()[0]:
				print "数字%d和%d是一对友好数"%(x.keys()[0], y.keys()[0])
youhao(10000)