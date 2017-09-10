#-*-coding：utf-8-*-
#author：PeterGu
#e-mail：gucaca@yeah.net

#1,2,3,4，生成所有可能的不重复位数三位数：

def print_num(list):
	num = 0
	for i in list:
		for j in list:
			for k in list:
				if (i!= j) and (i != k) and (j != k):
					print('%d%d%d'%(i,j,k))
					num = num + 1
	print (u'一共有%d个三位数' % num)



if __name__ == '__main__':
	list1 = [1,2,3,4,5,6,7]
	print_num(list1)