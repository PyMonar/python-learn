# Learn Python 
# 6. OOP
# By Monar

############################################
# 面向对象
############################################

# 类定义

class Student(object):
    # self 表示创建的实例本身，类似于this，永远是第一个参数
    # 如果实例变量为双下划綫表示的话则表示私有变量
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def __str__(self):
        return 'My name is ' + self.__name
    # def __iter__(self):
    #     pass
    # 用于迭代用
    def printScore(self):
        print "%s has scored %d points." % (self.__name, self.__score)
    
    def getGrade(self):
        if self.__score >= 90 :
            return 'A'
        elif self.__score < 90 and self.__score >= 80:
            return 'B'
        else:
            return 'C'

bart = Student('bart', 90)

bart.printScore()

print "Bart has got a", bart.getGrade()

print bart


# 继承

class Animal(object):
    def run(self):
        print "Animal can run"

class Dog(Animal):
    # 多态，子类复写了父类的方法
    def run(self):
        print "Dog can run"
    def eat(self):
        print "Dog can eat"

class Cat(Animal):
    def run(self):
        print "Cat can run"

cat = Cat()
cat.run()

dog = Dog()
dog.run()
dog.eat()

print "Dog is Animal?", isinstance(dog, Animal)

# 判断类型
# type() 
# isinstance(o, (type1, type2))
# dir() 返回所有属性和方法
# getattr() setattr() hasattr()


# __slots__ = ('name', 'age') 用于限制类的定义属性

# @property 装饰器用来将方法转化为属性调用

# Python 支持多重继承

# __str__ 字符串输出
# __iter__ 迭代器 配合next()
# __getitem__ 下标访问

# continue...

