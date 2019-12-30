# -*- coding: utf-8 -*- 
"""
项目: ProjectCases
作者: 张强
创建时间: 2019-12-26 08:58
IDE: PyCharm
介绍:学生成绩管理系统
"""
import re
import os

filename = 'student.txt'


def menu():
    # 输出菜单
    print('''
    功能菜单
    1.录入学生成绩
    2.查找学生信息
    3.删除学生信息
    4.修改学生信息
    5.排序
    6.统计学生总人数
    7.显示所有学生信息
    0.退出系统
    ''')


def insert():
    studentList = []
    mark = True
    while mark:
        id = input("请输入ID(如1001)：")
        if not id:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩:"))
            python = int(input("请输入python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，不是整型数值...重新录入信息")
            continue
        student = {"id": id, "name": name, "english": english, "python": python, "c": c}
        studentList.append(student)
        inputMark = input("是否继续输入?(y/n):")
        if inputMark == 'y':
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完毕！")


def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按ID查输入1；按姓名查输入2:")
            if mode == '1':
                id = input("请输入学生ID：")
            elif mode == '2':
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入!")
                search()
            with open(filename, 'r') as rfile:
                student = rfile.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id is not "":
                        if d['id'] == id:
                            student_query.append(d)
                    elif name is not "":
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMrak = input("是否继续查询?(y/n):")
                if inputMrak == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息...")
            return


def show_student(studentList):
    if not studentList:
        print("o@.@o 无数据信息(o@.@o)\n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"),info.get('name'),str(info.get('english')),str(info.get("python")),str(info.get("c")),str(info.get("python") + info.get("english") + info.get("c")).center(12)))


def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生ID:")
        if studentId is not "":
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除..." % studentId)
                    else:
                        print("没有找到ID为 %s的学生信息..." % studentId)
            else:
                print("无学生信息")
                break
            show()
            inputMark = input("是否继续删除？(y/n):")
            if inputMark == 'y':
                mark = True
            else:
                mark = False


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readline()
    else:
        return
    studentid = input("请输入要修改的学生ID:")
    with open(filename, 'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d['id'] == studentid:
                print("找到了这名学生，可以修改他的信息")
                while True:
                    try:
                        d['name'] = input("请输入姓名：")
                        d['english'] = int(input("请输入英语成绩："))
                        d['python'] = int(input("请输入python成绩:"))
                        d['c'] = int(input("请输入c语言成绩:"))
                    except:
                        print("您的茹茹有误，请重新输入")
                    else:
                        break
                student = str(d)
                wfile.write(student + '\n')
                print("修改成功")
            else:
                wfile.write(student)
    mark = input("是否继续修改其他学生的信息？(y/n):")
    if mark == 'y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r') as file:
            student_old = file.readlines()
            student_new =[]
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)
    else:
        return
    ascOrdesc = input("请选择(0 升序;1 降序):")
    if ascOrdesc == '0':
        ascOrdescBool = False
    elif ascOrdesc =='1':
        ascOrdescBool = True
    else:
        print("您的输入有误，请重新输入!")
        sort()
    mode = input("请选择排序方式(1 按英语成绩排序；2 按python成绩排序; 3 按c语言成绩排序;0 按总成绩排序):")
    if mode == '1':
        student_new.sort(key=lambda x:x['english'],reverse=ascOrdescBool)
    elif mode =='2':
        student_new.sort(key=lambda x:x['python'],reverse=ascOrdescBool)
    elif mode =='3':
        student_new.sort(key=lambda x:x['c'],reverse=ascOrdescBool)
    elif mode =='0':
        student_new.sort(key=lambda x:x['english']+x['python']+x['c'],reverse=ascOrdescBool)
    else:
        print("您输入有误，请重新输入！")
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("一共有 %d 名学生!" %len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息")


def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


def save(student):
    try:
        students_txt = open(filename, 'a')
    except Exception as e:
        students_txt = open(filename, 'w')
    for info in student:
        students_txt.write(str(info) + "\n")
    students_txt.close()


def main():
    ctrl = True
    while (ctrl):
        menu()
        option = input("请选择：")  # 选择菜单项
        option_str = re.sub("\D", "", option)  # 提取数字
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出学生信息管理系统！")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()


if __name__ == '__main__':
    main()
