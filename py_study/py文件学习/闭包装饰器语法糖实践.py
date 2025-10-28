def fun1():
    print("hello world")
def fun2(fn):
    def fun3():
        fn()  #相当于fun1
        print("hello beautiful world")
    return fun3
#print(fun2(fun1))
f2 = fun2(fun1)
f2()

@fun2
def fun4():
    print("hello world")
fun4()
#装饰器1
def deco1(fn):
    def inner():
        return "你好"+fn()+"世界"
    return inner
#装饰器2
def deco2(fn):
    def inner():
        return "再见"+fn()+"世界"
    return inner
#被装饰的函数
@deco2 #多个装饰器时先离得最近的先装饰
@deco1
def han():
    return "美丽的"
print(han())
#再见你好美丽的世界世界