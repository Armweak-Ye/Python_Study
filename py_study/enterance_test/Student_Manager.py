Students = [{"name":"SIYI",
             "age":"19",
             "location":"China",
             "id": '0',
             "chinese":"150",
             "math":"150",
             "english":"150",
            }]
while True:
    id = 1
    print('添加学生请输入1，查看学生请输入2，退出程序请按3')
    a = input('请输入数字编号：')
    class Student_Manager:
        def add_students(self):
            name = input('请输入学生姓名：')
            if name in Students:
                print("学生已存在")
            age = input("请输入学生年龄")
            location = input('请输入学生住址')
            chinese = input("请输入其语文成绩：")
            math = input("请输入其数学成绩：")
            english = input("请输入其英语成绩")
            Students.append({
             "name":name,
             "age":age,
             "location":location,
             "id": id,
             "chinese":chinese,
             "math":math,
             "english":english,
            })
        id = id + 1
        def see(self):
            if len(Students) == 0:
                print("系统中还没有学生，请去添加")
            for student in Students:
                print(student)
    op = Student_Manager()
    if a == '1':
        op.add_students()
    elif a == '2':
        op.see()
    elif a == '3':
        exit()
    else:
        print("请输入1或2")