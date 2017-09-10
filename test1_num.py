#-*- coding:utf-8 -*-
#author:PeterGu
#e-mail:744073923@qq.com

#目标：有四个数字1、2、3、4，能组成多少互不相同的无重复的三位数，并输出。
#分析：建立一个列表，依次取数作为百位数，去掉该百位数后形成新的列表，再在剩余的里面取十位数，依次操作，最后取个位数。
#最终：形成一个函数，不管输入列表中有多个元素，都能判断出有多少个三位数。

def list_num(list1):
	num = 0
	for i in range(len(list1)):
		list2 = list1.copy()
		list2.pop(i)
		for j in range(len(list2)):
			list3 = list2.copy()
			list3.pop(j)
			for k in range(len(list3)):
				print("%d%d%d" %(list1[i],list2[j],list3[k]))
				num = num + 1
	print (u'一个有%d个三位数'% num)			




if __name__ == "__main__":
	list_num([1,2,3,4,5,6,7])



