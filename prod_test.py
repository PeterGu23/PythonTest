#-*-coding：utf-8 -*-
#author：PeterGu
#email：744073923@qq.com

#目标：编写prod( )，接收一个list，并用reduce求积。

from functools import reduce

def prod(x,y):
	return x * y

list1 = [1,4,3,2,1,111,12]
multiply = reduce(prod,list1)
print (multiply)


