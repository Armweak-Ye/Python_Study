class Person:
    name = "SIYI" #类属性
    __age = 19 #隐藏属性，不能在类的外部访问
    __weight = "65kg"
    _sex = "male"
    def introduce(self):#在实例方法里面访问类属性和隐藏属性
        print(f"My name is {Person.name},age is {Person.__age} and weight is {Person.__weight}")
        Person.__play(self)#在实例方法中调用私有方法，这种格式不推荐，太繁琐
        self.__play() #推荐使用，更简便
    def __play(self):
        print("Battlefield1 hao wan")
pe1 = Person()
print(pe1.name)
print(pe1._Person__age)
#隐藏属性实际上是python自动将名字修改为_类名__属性名  如_Person__age#不规范，不推荐
pe1.introduce()
print(pe1._sex)
#print(Pe.__weight)  #访问不到__weight
print()
class Human:
    height = "168cm"
    age = 19
    weight = "65kg"
    def _introduce(self):
        print(f"A {Human.height} and {Human.age} years"
        f"old Human`s weight is {Human.weight}.")
    def left(self):
        MoneyF = 100
        MoneyF += 50*2**3
        print(f"I have {MoneyF}$")
class Boy(Human):
    pass  #占位符，代码类下面不写任何东西，会自动跳过，不会报错
boy1 = Boy()
boy1._introduce()
boy1.left()
class Girl(Human):
    def left(self):
        print("I don`t make money")
#子代重写父代方法时优先调用自己的
        super().left()
#super在python中是一个特殊的类，super()是使用super类创建出来的对象，可以调用父类的方法
#推荐使用super().方法名()
girl1 = Girl()
girl1._introduce()
girl1.left()

#多继承语法
#class 子类名(父类名1,父类名2)：
#子类可以同时使用两个父类的方法
#假若父类拥有同名的方法，则调用前面的那个