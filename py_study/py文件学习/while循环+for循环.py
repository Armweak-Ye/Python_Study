# 计算1到100的和
i = 1
s = 0
while i<=100 :
    s += i    #要先计算0+1
    i += 1
print("从1到100的和：", s)

a = 1
while a <= 3 :
    print(f"这是第{a}次外循环" )
    b = 1
    while b <= 5 :
        print(f"这是{b}次内循环" )
        b += 1
    a += 1
'''每进行一次外循环，只要内循环条件满足就会一直执行直到条件不满足再
从头进行一次外循环'''

j = 0
for i in range(1,101):
    j += i
print(f"输出结果是：{j}")

c = 1
while c <= 5 :
    print(c)
    if c == 3 :
        print("不想算了，拜拜")
        break #满足c=3时结束循环
    c += 1

d = 1
while d <= 5 :
    print(f"我数到了{d}")
    if d == 3 :
        print("我其实不想数3")
        d += 1
        # continue之前一定要修改计数器，不然会陷入死循环
        continue
    d += 1