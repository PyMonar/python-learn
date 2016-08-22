# Learn Python 
# 4. 函数式编程
# By Monar

############################################
# 函数式编程
############################################

# 高阶函数
# 函数名也是变量，类似js，一个函数接受另一个函数作为参数，则成为高阶函数
def add(x, y, f):
    return f(x) + f(y)

print add(-1, -2, abs)

# map/reduce

def f(x):
    return x * x

print map(f, [1, 2, 3, 4, 5])

def add(a, b):
    return a + b

print reduce(add, [1, 2, 3, 4, 5])

# practice
def op(s):
    #return s[0:1].upper() + s[1:].lower()
    return s.capitalize()

print map(op, ['adam', 'LISA', 'barT'])

def prod(a, b):
    return a * b

print reduce(prod, [2, 3, 4, 5])

# filter
def odd(x):
    return x % 2 == 0

print filter(odd, [1, 2, 3, 4, 5, 6])

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print filter(isPrime, range(2, 101))

# sort
# sorted(list, comp)

# python 支持闭包！
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 3, 4)
print f()

# lambda 函数

# lambda x: x * x
# =>
# def some(x):
#     return x * x

# 装饰器

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def sayHi():
    print "My name is Monar"

sayHi()

# 偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单