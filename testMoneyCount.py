# coding:utf-8
'''
100块换成 1，2，5，10块零钱 一共有多少种算法
'''

'''
这种方法按思维逻辑实现
总数为： 2152
'''
x = 0
for x_1 in range(0, 100):
	for x_2 in range(0, 50):
		for x_5 in range(0, 20):
			for x_10 in range(0, 10):
				if x_1 + 2 * x_2 + 5 * x_5 + 10 * x_10 == 100:
					x += 1
print "总数为：%d\n"%x

'''
这种方法网上看到的
总数为： 2156
'''
def change(amount, loose):
    dp = [0]*(amount+1)
    dp[0] = 1
    for l in loose:
        for i in range(l, amount+1):
            dp[i] += dp[i - l]
    return dp[amount]
print(change(100, [1,2,5,10]))
