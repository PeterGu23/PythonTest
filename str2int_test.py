#-*-coding：utf-8 -*-
#author：PeterGu
#email：744073923@qq.com

#目标：运用reduce和map写出将str转换为int的函数

from functools import reduce

def char2int(char1):
	char2int_dict = {"0":0,"1":1,"2":2,"3":3,"4":4,
	"5":5,"6":6,"7":7,"8":8,"9":9}
	return char2int_dict[char1]

def list2int(x,y):
	return x*10 + y

def str2int(str1):
	r = reduce(list2int,list(map(char2int,str1)))
	return r

if __name__ == '__main__':
	print (str2int('23456')+str2int('22222'))


