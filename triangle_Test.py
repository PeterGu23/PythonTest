#-*- coding:utf-8 -*-
#author:PeterGu
#email:gucaca@yeah.net


#目标：建立一个生成器，每此生成一个杨辉三角的一行（以列表形式）
#         1
#       1   1
#     1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1'''

def triangles(max):
	yield [1]
	n,l,g = 2,[1,1],[1,1]
	while n <= max:
		yield g
		q = l.copy()
		for i in range(n-1):
			q.insert(i+1,g[i]+g[i+1])
		g = q
		n = n + 1

for i in triangles(10):
	print (i)