#-*-coding:utf-8 -*-
#author:PeterGu
#e-mail:gucaca@yeah.net

#本程序试图通过分析输入的身高与体重计算BMI，
#并根据BMI的值判断肥胖程度。

import time

#计算BMI值得函数
def bmiCompu(height,weight):
	return weight/(height*height)

#输入身高与体重，并计算BMI后打印
yourheightstr = input('Please input your height(in m):')
yourheight = float(yourheightstr)
yourweightstr = input('Please input your weight(in kg):')
yourweight = float(yourweightstr)
yourBMI = bmiCompu(yourheight,yourweight)
print('your BMI:%.2f' % yourBMI)

time.sleep(1)
print('Please waiting!')

time.sleep(2)

if yourBMI < 18.5:
	print(u'您的体重过轻!')
elif yourBMI <25:
	print(u'您的体重正常!')
elif yourBMI < 28:
	print(u'您的体重过重!')
elif yourBMI < 32:
	print(u'您的体重肥胖！')
else:
	print(u'您的体重严重肥胖！！！！')
