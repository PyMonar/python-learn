# Learn Python 
# 1. Python basic
# By Monar

# 输入与输出

# 输入
print "Hello World"

# 遇到','会显示一个空格
print "My name is", "Monar"
print "100 + 200 =", 100 + 200

# 输出
# name = raw_input("Hey, please input your name:")
name = 'Sandy'
print "The name you input is", name

############################################
# Python 基础
############################################

# 1. 数据类型与变量

# 整数 1, 100, 0, -8000 或者十六进制0xFF00
# 浮点数 1.23 3.14 -9.01 1.23e9 1.2e-5
# 字符串 "I'm OK'"  r"\\\\\\"(不转义)
# '''Some thing''' 表示多行字符串
print r'\\\\\\'

print '''line1
line2
line3'''

print r'''\t\t
\\\\'''
# 布尔值 True False
# 布尔运算 or and not
# 空值 None

# 变量 大小英文字母和数字和_组成
# 变量可以反复赋值，并且可以存储任意类型的数据类型
# 常量 Python中用大写来表示常量

# 2. 字符串和编码

# ord() 将字符转化为ASCII码
print ord('A')
# chr() 将ASCII码转化为字符
print chr(66)

# u"..." 增加Unicode支持
# .encode('utf-8') 转化为UTF-8
print u"\u4e2d"
print '中文'
# len() 显示字符串长度
print len("ABCDEFG")

# 格式化输出字符串
# %d 整数
# %s 字符串
# %f 浮点数
# %x 十六进制

print "%s have %d child." % ('You', 3)
print "%2d-%03d" % (3, 1)
print "%.2f" % 3.14159

# % 可以用%来转义
print "%d%%" % 7

# 3. list和tuple

# list 列表
# list 可以存储不同类型的值
# list 可以嵌套
listInit = list("123") # listInit = ['1', '2', '3']
classmates = ['monar', 'sandy', 'bob']
print "Class has %d person." % len(classmates)
print "%s is the No.1" % classmates[0]
print "%s is the last one." % classmates[-1]

classmates.append('tracy')
print "We have a new classmate: %s" % classmates[-1]
classmates.insert(1, 'jack')
print "%s has the second place." % classmates[1]
print "We delete a classmates", classmates.pop() # pop(index) 删除指定位置的元素并返回

# tuple 元祖
# 类似于list，但是一经初始化就不可修改，安全
language = ('java', 'python', 'js')
# 定义一个只有一个元素的元祖，可以使用：t = (1, ),如果不加逗号，则返回数字1

# 4. 条件判断与循环

# 条件判断
age = 20
if age > 18:
    print "I'm a adult"
elif age < 10:
    print "I'm a child"
else:
    print "I'm nothing"

# if x: do something 
# x 为非零数值、非空字符串、非空列表等时返回True，其余返回False

# 循环

# for
for name in classmates:
    print "This is", name

# range(i) 生成一个列表 [0, i)
sum = 0
for x in range(101):
    sum += x
print "Sum from 1 to 100 is:", sum

# while
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print "Odd sum from 1 to 99 is %d" % sum

# int(str) 转换字符串为整数

# 5. dist与set

# dist 字典
# dic.keys() dic.values() dic.items()
# dic.clear()
# del dic[key]

grade_book = {'math': 99, 'chinese': 92, 'english': 89}
print "My math score is %d" % grade_book['math'] # or grade_book.get('math')
print "I get a art score: 100"
grade_book['art'] = 100
print "Is art in my grade_book? Yes, it is", 'art' in grade_book 
print "I lost my english score"
grade_book.pop('english')

for class_name in grade_book:
    print class_name, "score is", grade_book[class_name]

# set 集合
# 一组key的集合，互不重复

s1 = set([1, 2, 3, 4, 4])
s1.add(5)
s1.remove(3)
print "The set is", s1

s2 = set([2, 4, 6])
print "s1 & s2 is", (s1 & s2)
print "s1 | s2 is", (s1 | s2)