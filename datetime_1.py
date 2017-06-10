#coding: utf-8

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
情况，闰年且输入月份大于3时需考虑多加一天
'''

import datetime
t=datetime.date(input("Year:"),input("Month:"),input("Day:"))
n=datetime.date(datetime.date.today().year,1,1)
print (t-n).days+1

year,month,day=input("Year:"),input("Month:"),input("Day:")
d={1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
if not d.has_key(month):
	print "data error"
  	exit()
sum=d[month]
sum+=day
if year%400==0 or (year%4==0 and year%100!=0):
  	leap=1
else:
  	leap=0
if leap==1 and month>2:
  	sum+=1
print "It is the %dth day." % sum