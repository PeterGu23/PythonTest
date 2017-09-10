#-*-coding：utf-8-*-
#author：PeterGu
#emai：gucaca@yeah.net

#递归练习：汉诺塔
#move(n,a,b,c);其中n表示第一个柱子的盘子数量，打印出把所有盘子
#从a移动到c的方法。

def move(n,a,b,c):
	if n == 1:
		print(u'把盘子从',a,u'移动到',c,'!')
	else:
		move(n-1,a,c,b)
		print(u'把盘子从',a,u'移动到',c,'!')
		move(n-1,b,a,c)


move(2,'A','B','C')