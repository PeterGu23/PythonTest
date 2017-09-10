#-*-coding:utf-8 -*-
#author:PeterGu
#e-mail:744073923@qq.com

#目标：请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0的两个解。
#提示：计算平方根可以调用math.sqrt()函数。

import math

def quadratic(a,b,c):
	if not isinstance((a,b,c),(int,float)):
		raise TypeError('Bad type!')
	delta = b*b- 4*a*c
	if delta < 0:
		print (u'方程无解！')
		return 
	else:
		print(u'方程有两个解，分别为：%s，%s' % ((-b+math.sqrt(delta))/2*a,(-b-math.sqrt(delta))/2*a))
		return (-b+math.sqrt(delta))/2*a,(-b-math.sqrt(delta))/2*a
		


print(quadratic('c',2,3))