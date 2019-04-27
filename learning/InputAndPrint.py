

'''
 python的标准输入和输出
'''

# str.format() 格式化输出
print('{0} <> {1}'.format('zengsk', 'hhu university!'))
print('{name} <> {city}'.format(name='zengsk', city='nanjing jiangsu'))

import math
print('PI 的值为{0:.3f}'.format(math.pi))  # 保留三位有效数字
print('PI 的值为{0:3d}'.format(20))  # 后传入一个整数, 设置该域的宽度

# % 操作符字符串格式化(旧式方式)
print('PI 的值为 %5.3f' % math.pi)  # 保留三位有效数字

print('+--------------------------+')

# 标准输入

# input() 函数：从标准输入读入一行文本，默认的标准输入是键盘
str = input('please input:')
print('str = ', str)


# sys.stdin 标准输入
import sys

# strip('\n')表示以\n分隔，否则输出是'字符串+\n'的形式
line = sys.stdin.readline().strip('\n')
print('line:', line)

# 若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list.
linelist = sys.stdin.readline().strip()
linenum = list(map(int, linelist.split())) #强制转换成int等类型，可以调用map()函数。
print(linenum)



