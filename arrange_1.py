# coding: utf-8
'''
题目： 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。
'''
def arrange(loose):
	i = 0
	for b1 in loose:
		for b2 in loose:
			for b3 in loose:
				if b1!=b2 and b2!=b3 and b1!=b3:
					i += 1
					print("%d. %d%d%d" % (i, b1, b2, b3))
arrange([1,2,3,4])