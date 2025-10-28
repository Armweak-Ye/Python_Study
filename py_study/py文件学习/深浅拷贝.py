li = [1,2,3,4,5]
li2 = li
print(li)
print(li2)
print(id(li))#查看内存位置
print(id(li2))
li.append(9)
print(li)
print(li2)
print(id(li))
print(id(li2))
#赋值二者值共享

import copy
li3 = [1,2,3,4,5,[6,7,8]]
li4 = copy.copy(li3)#浅拷贝
print(li3)
print(li4)
print(id(li3))#内存地址不同说明不是同一个对象
print(id(li4))
li3.append(8)
print(li3) #[1, 2, 3, 4, 5,[6,7,8],8]
print(li4) #[1, 2, 3, 4, 5,[6,7,8]]
print(id(li3))
print(id(li4))

print(li[5])
li3[5].append(9)
print(li3)
print(li4)
print(id(li3[5]))
print(id(li4[5]))#二者嵌套列表的内存地址是一样的

#深拷贝
li5 = [1,2,3,4,5,[6,7,8]]
import copy
li6 = copy.deepcopy(li5)
print(id(li5[5]))
print(id(li6[5]))#深拷贝后，二者嵌套列表内存地址不一样了

# 不可变对象
n = 10
print(n,id(n))
n = 15
print(n,id(n))
n = 20
print(n,id(n))
#每次n的内存地址都变，是一个新的变量
#前面的深浅拷贝只针对可变对象，不可变对象没有这一个说法
'''可变对象；
list
dict
set

不可变对象：
int，bool，float，complex（复数）
str
tuple（不可增加，删减与修改，只能查询）
'''