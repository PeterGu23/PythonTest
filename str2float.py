#-*-coding：utf-8 -*-
#author：PeterGu
#email：744073923@qq.com

#目标:str2float函数，把字符串‘123.456’转换为123.456。

from functools import reduce
from str2int_test import char2int #将每一个字符转换为数字
from str2int_test import list2int #将数字转为整数

def s2float(x,y):# 用来将小数部分倒过来后得到小数部分
	return x*0.1 + y

def str2float(s):
	index = [i for i, num in enumerate(s) if num =='.'] #找到字符串中小数点的位置
	num_part_list = list(map(char2int,s[:index[0]])) #将小数点前面的数字转换为数字list
	num_part_value = reduce(list2int,num_part_list)#将数字list转换为整数部分值
	float_part_list =list(map(char2int, s[index[0]+1:]))#将小数点后的数字转换为list
	float_part_list.reverse()#将小数分布lits倒过来
	float_part_value = 0.1 * reduce(s2float,float_part_list)#求得小数部分值
	return num_part_value + float_part_value #相加得到浮点数值

if __name__ == '__main__':
	str1 = '12345.6789'
	str2 = '11111.1111'
	float1 = str2float(str1)
	float2 = str2float(str2)
	print (float1 + float2)