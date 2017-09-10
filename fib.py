#-*-coding:utf-8-*-
#author:PeterGu
#email:744073923@qq.com

#运用生成器生成斐波那契数列


def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield(b)
		a, b = b, a+b
		n = n + 1
	return 'done'


f = fib(8)
print(next(f))


