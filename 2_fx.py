# Learn Python 
# 2. 函数
# By Monar

############################################
# 函数
############################################

# 内置函数
# abs() 取绝对值
# cmp(a, b) a < b: -1, a == b: 0, a > b: 1

# 数据类型转换
# int()
# float()
# str()
# bool()

# 定义函数

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Bad operand type")
    if x >= 0:
        return x
    else:
        return -x

def doNothing():
    pass


print my_abs(-1)
# print my_abs('A')

# 函数可以返回多个值

def move(x, y):
    x += 1
    y += 1
    return x, y # 返回的是一个tuple，只不过括号可以省略

x, y = move(3, 4)
print "(x, y) is (%d, %d)" % (x, y)


# 函数的参数

# 定义默认参数

def my_power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print my_power(5)
print my_power(2, 3)


def enroll(name, gender, age = 6, city = 'Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city = 'Tianjin')

# 注意：默认参数必须指向不可变对象，否则会有问题。

# 可变参数

def calc(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

print "the sum of (1, 2, 3, 4, 5) is", calc(1, 2, 3, 4, 5)

# *加上tuple或者列表可以将其解构成参数列表
nums = [1, 2, 3, 4, 5, 6]
print "the sum of (1, 2, 3, 4, 5, 6) is", calc(*nums)

# 关键字参数

def person(name, age, **kw):
    print "name:", name, ",age:", age, ",other:", kw

person('Monar', 26, city = 'Beijing', job = 'FE')

# 参数组合

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw) # a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}


# 递归

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)

print "5! is", fact(5)



