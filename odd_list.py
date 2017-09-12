#-*- coding:utf-8 -*-
#author:PeterGu23	
#email:gucaca@yeah.net


#目标：生成目标数据内的奇数列表（本例为1000）

#判断一个数是否为奇数
def is_odd(num):
	return (num % 2 != 0)

#生成目标数内的全数列表
def num_list(num):
	ls = []
	for i in range(num+1):
		ls.append(i)
	return ls[1:]


if __name__ == '__main__':
	r = list(filter(is_odd, num_list(1000))) #生成100以内的奇数
	print (r)



