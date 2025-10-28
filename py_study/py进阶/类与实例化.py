class Washing_Machine:
    weight = 600 #类属性
    def wash(self): #这是方法部分 #self参数是类中的实例方法必须具备的
        print("I can wash clothes")
        print("self:", self) #self表示当前调用该方法的对象
wa = Washing_Machine()#实例化对象
wa.wash()#调用对象
print(wa)
wa2 = Washing_Machine()
wa2.wash()
print(wa2)
'''self代表对象本身，当对象调用实例方法时，
python会自动将对象本身的引用作为参数，传递到实例方法的第一个参数self里面
'''
print()
class Person:
    name = "SIYI"
    def introduce(self):
        print(f"我的名字是{Person.name},年龄:{self.age}")#self.age是实例属性 #self改为pe也行
pe = Person()
pe.age = 19
pe.introduce()
""" 类属性是属于类的，是公共的，大家都可以访问
实例属性是对象的，是私有的，只能由对象名访问，不能由类名访问
"""
class Person:
    def __init__(self,age,sex,name):#__init__通常用来做属性初始化或赋值操作
        self.age = age #以下是实例属性
        self.sex = sex
        self.name = name
    def introduce(self):
        print(f"{self.name}今年{self.age}岁，sex is {self.sex}")
    def play(self):
        print(f"{self.name}在打战地1")
pe = Person(19,"male","SIYI")#实例化时先传参
pe.introduce()
pe.play()
#实例化第二个
pe2 = Person(19,"female","yanjingmei")
pe2.introduce()
pe2.play()