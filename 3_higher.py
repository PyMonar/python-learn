# Learn Python 
# 3. 高级特性
# By Monar

############################################
# 高级特性
############################################

# 至简哲学

# 切片
# 列表、元组和字符串都适用
colors = ['blue', 'orange', 'red', 'pink', 'yellow']

print "slice [0, 3) is", colors[0:3]
print "slice [-2, ) is", colors[-2:]

nums = range(20)
print "even range is", nums[:20:2] # 第三个参数是步长

# 如果不设参数会复制整个列表
nums2 = nums[:]
print "nums2 is", nums2

# 迭代
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，如果要同时迭代key和value，可以用for k, v in d.iteritems()

for i, value in enumerate(colors):
    print i, value

for i in range(len(colors)):
    print colors[i]

# 列表生成式

# range(i, j) => [i, j)
# [x * x for x in range(1, 11)]
# [x * x for x in range(1, 11) if x % 2 == 0]
print '[x * x for x in range(1, 11)] is:', [x * x for x in range(1, 11)]
print "[m + n for m in 'ABC' for n in 'XYZ'] is", [m + n for m in 'ABC' for n in 'XYZ']

L = ['Hello', 'World', 18, 'Apple', None]
print [x.lower() if isinstance(x, str) else x for x in L]

# 生成器

# 简单生成器
g = (x * x for x in range(10))
for n in g:
    print n

# 函数生成器，只要在函数中包含yield

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in fib(6):
    print n

