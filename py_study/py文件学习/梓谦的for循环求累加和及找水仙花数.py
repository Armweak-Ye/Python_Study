print("-------寻找规定三位数中的水仙花数-------")
'''
例：153=5*5*5+3*3*3+1*1*1
即该数每一位的位数次幂的和等于该数的为水仙花数
'''
a=eval(input("请输入所需三位数范围的最小数："))
b=eval(input("请输入所需三位数范围的最大数："))
for i in range(a,b+1):
    sd=i%10
    tens=i//10%10
    hundreds=i//100
    if i==sd**3+tens**3+hundreds**3:
        print(i,'是该范围的水仙花数')
print("------求连续整数的和------")
c=eval(input('请输入一串连续整数中的最小数：'))
d=eval(input('请输入一串连续整数中的最大数：'))
s=0
for i in range(c,d+1):
    s+=i
else:#else语句当for循环正常结束后输出，此循环中可有可无
    print('这一串整数和为：',s)