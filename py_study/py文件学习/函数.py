def function1(*args): #可变参数，可传入多个值
    print(args)
    print(type(args)) #tuple
function1(1,56,96)
#默认参数必须写在所有参数的后面

def function2(**kwargs):
    print(kwargs)
    print(type(kwargs)) #dict
function2(name='SIYI',age=19,sex='Man')
# 传值时需要以键名=值的形式传值


#嵌套调用
#含义：在一个函数里面调用另一个函数
def function3(a=666):
    print(a)
    function2(name='SIYI',age=19,sex='Man')
function3(a=666)

#嵌套定义
def function4(*args):
    print(args)
    def function5(**kwargs):
        print(kwargs)
    function5(学习的是='Python基础')
function4('现在在学习')
#注意：内层函数不要去调用外层函数，否则会陷入死循环直到到达最大递归深度

