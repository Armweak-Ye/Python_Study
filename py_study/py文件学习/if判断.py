age = input ("请输入年龄：")
if age >= '18':
    print("你已经是个成年人啦！")
else:
    print("你还是个未成年喔。")

cash = float(input ("请放入钞票："))
bill = float(input ("请输入消费额："))
# 指定输入的数据类型
if cash >= bill:
    print("找您""{:.2f}""元".format(cash - bill))
else:
    print("您还差""{:.2f}""元".format(bill - cash ))
# bill-cash要括号要不然他以为%.2f要输入cash这个字符串
# 百分号后面要有个点去限定多少位数
# 师兄建议用上面那种输出形式先处理数据到只有两位，然后输出
Ticket = True#布尔型变量
if Ticket == True :
    print("可以进站了")
    Temp = float(input("你腋下体温多少："))
    if 36.5<=Temp<=37.2 :#正常人腋下体温
        print("可以回家了。")
    else:
        print("要被抓过去隔离力")
else:
    print("没买票坐什么车")