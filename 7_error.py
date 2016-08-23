# Learn Python 
# 7. Exception
# By Monar

############################################
# Exception
############################################

# 异常处理

try:
    print "Try:"
    r = 10 / 0
    print "Result:", r
except ZeroDivisionError, e:
    print "Except:", e
else:
    pass
finally:
    print "Finally"

print "End"

# 自定义异常
# 继承自StandardError
# raise 语句来抛出异常
class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# 调试

# assert 断言，不匹配则抛出错误