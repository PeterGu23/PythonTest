#-*-coding：utf-8 -*-
#author：PeterGu
#email：744073923@qq.com

#目标：将列表中的名字改为首字母大写，其他字母小写的标准格式

def  normalize(name):
	list1 = ''
	for i in range(len(name)):
		if i == 0:
			list1 = name[i].upper()
		else:
			list1 = list1 + name[i].lower()
	return list1

if __name__ == '__main__':
	L1 = ['adam', 'LISA', 'barT']
	L2 = list(map(normalize, L1))
	print(L2) #期待输出['Adam', 'Lisa', 'Bart']