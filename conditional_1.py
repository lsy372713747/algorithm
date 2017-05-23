#coding: utf-8

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。if else 判断
'''
# moon = int(raw_input("请输入月利润:\n"))
def moons(moon):
	bonus1 = 100000*0.1
	bonus2 = bonus1+100000*0.75
	bonus4 = bonus2+200000*0.5
	bonus6 = bonus4+200000*0.3
	bonus10 = bonus6+400000*0.15

	if moon<=100000:
	 	bonus=moon*0.1
	elif moon<=200000:
		bonus=bonus1+(moon-100000)*0.075
	elif moon<=400000:
		bonus=bonus2+(moon-200000)*0.05
	elif moon<=600000:
		bonus=bonus4+(moon-400000)*0.03
	elif moon<=1000000:
		bonus=bonus6+(moon-600000)*0.015
	else:
		bonus=bonus10+(moon-1000000)*0.01
	return "月利润 %d 提成为：%d" % (moon, bonus)
print moons(120000)
'''
月利润 120000 提成为：11500
'''


