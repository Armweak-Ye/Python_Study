# 1. 提示拥有的功能
# 2. 增加学生
# 3. 删除学生
# 4. 修改学生
# 5. 查询学生
# 6. 显示所有学生
# 7. 按分数排序
# 8. 退出

student_list = [] # 保存所有学生的信息
cur_id = 0  # 当前学生id

# student_menu 学生菜单
def student_menu():
    print(" 1) 添加学生")
    print(" 2) 查看所有学生")
    print(" 3) 修改指定学生")
    print(" 4) 删除指定学生")
    print(" 5) 按分数排序")
    print(" 6) 退出")
    choice = input("请输入菜单序号：")
    if choice == "1":
        print("添加学生")
        add_stu()
    elif choice == "2":
        print("查看所有学生")
        get_stu()
    elif choice == "3":
        print("修改指定学生")
        change_stu()
    elif choice == "4":
        print("删除指定学生")
        del_stu()
    elif choice == "5":
        print("按分数排序")
        order_by_score()
    elif choice == "6":
        print("退出")
        exit() #退出程序
    else:
        print("输入错误")

def add_stu():
    # 添加学生
    global cur_id  #声明全局变量
    name = input("请输入学生的名字：")
    age = input("请输入学生的年龄：")
    score = int(input("请输入学生的分数："))
    cur_id = cur_id + 1
    student_list.append({
        "id":cur_id,
        "name":name,
        "age":age,
        "score":score
    })
    print("添加成功")


def get_stu():
    # 查看所有学生
    if len(student_list) <= 0:
        print("没有学生~")
        return
    for stu in student_list:
        '''
            多行注释
        '''
        print(f'''学生id:{stu["id"]},
                姓名:{stu["name"]},
                年龄:{stu["age"]},
                分数:{stu["score"]}''')


def change_stu():
    # 修改指定学生
    change_id = input("请输入要修改的学生id:")
    for stu in student_list:
        if stu["id"] == int(change_id):
            name = input("请输入修改后的学生的名字：")
            age = input("请输入修改后的学生的年龄：")
            score = input("请输入修改后的学生的分数：")
            stu["name"] = name
            stu["age"] = age
            stu["score"] = score
            print("修改成功")
        else:
            print("您输入的学生不存在")
            break

def del_stu():
    # 删除指定学生
    del_id = input("请输入要删除的学生id:")
    for stu in student_list:
        if stu["id"] == int(del_id):
            student_list.remove(stu)
            print("删除成功")
            break

def order_by_score():
    # 按分数排序
    def by_score(stu):
        return stu["score"]
    student_list.sort(reverse=False,key=by_score)
    # newStudent_list = sorted(student_list,reverse=False,key=lambda stu:stu["score"])
    print(student_list)

# 主循环 执行所有代码
while True:
    student_menu()
