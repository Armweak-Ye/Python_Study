name =  'SIYI'
def fun1():
    print(name)
    print("%s" %name,'正在学习Python')
    def fun2():
        global age
        age = 19
        print(f'{name}今年{age}岁')
    fun2()
fun1()
yours = int(input('你今年几岁:'))
if yours > age:
    print('你和%s一样大' %name)
elif yours == age:
    print(f'你和{name}一样大')
else:
    print(f'你比{name}小，嘻嘻')