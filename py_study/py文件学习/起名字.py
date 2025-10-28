name_list = ['Jack','Lisa','Akatonia']
while True:
    name = input("请输入昵称：")
    if name in name_list:
        print(f'昵称{name}已存在')
        print(name_list)
    else:
        print(f'昵称{name}创建成功')
        name_list.append(name)
        break