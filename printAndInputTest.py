# -*-coding:utf-8 -*-
# author:PeterGu23
# e-mail:744073923@qq.com

#这是一个关于输入输出的练习，为一个进房间的小游戏

import time

#捕获玩家姓名
name = input('Please tell me your name:')
print('Hello',name,',','Welcome to play the Game!')
time.sleep(2)

print('There are two houses in front of you. Please choose one! Left or Right?')

choose = input('r/l:')

#防止非法输入
while choose != 'r' and choose != 'l':
	choose = input('Please choose r or l:')

if choose == 'l':
	print ('Congraculations! There are two beauties in the house, you can do what you want!')
else:
	print ('I am sorry! It is a trip! You die!')

time.sleep(2)

print ('Thank you for play the Game!')

