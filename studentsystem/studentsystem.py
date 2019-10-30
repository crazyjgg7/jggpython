import os
import re

def main():
    ctrl = True    #标记用
    while(ctrl):
        menu()
        option=input("请选择序号：")
        option_str=re.sub("\D","",option)
        if option_str in['0','1','2','3','4','5','6','7']:
            option_int=int(option_str)
            if option_int == 0:
                print('您已退出学生信息管理系统！')
                ctrl=False
            elif option_int == 1:
                insert()    #录入学生成绩
            elif option_int == 2:
                search()    #查询学生成绩
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
def menu():
    #输出菜单
    print('''
    -------------------------------------
    |                                   |
    |  ===========功能菜单===========    |
    |   1.录入学生信息                   |
    |   2.查询学生信息                   |
    |   3.删除学生信息                   |
    |   4.修改学生信息                   |
    |   5.排序学生信息                   |
    |   6.统计学生总数                   |
    |   7.显示学生信息                   |
    |   0.退出系统                       |
    |                                   |
    |  ===============================  |
    |  说明：通过数字或者方向键选择菜单    | 
    |                                   |   
    -------------------------------------
    ''')
def save(student):
    filename="students.txt"
    try:
        students_txt=open(filename,"a")
    except Exception as e:
        students_txt=open(filename,"w")
    for info in student:
        students_txt.write(str(info)+"\n")
    students_txt.close()
def insert():
    stdentList=[]
    mark =True
    while mark:
        id =input("请输入ID（如1001）")
        if not id:   #ID为空，跳出循环
            break
        name = input("请输入名字：")
        if not name:  #名字为空，跳出循环
            break
        try:
            english=int(input("请输入英语成绩："))
            python=int(input("请输入python成绩："))
            c=int(input("请输入C语言成绩"))
        except:
            print("输入无效，不是整数，请重新录入信息")
            continue
        stdent={"id":id,"name":name,"english":english,"python":python,"c":c}
        stdentList.append(stdent)
        inputMark=input("是否继续添加？（y/n）")
        if inputMark=="y":
            mark=True
        else:
            inputMark=False

        save(stdentList)
        break
    print("学生信息录入完毕")
def delete():
    mark=True
    filename="students.txt"
    while mark:
        studentID=input("请输入要删除的学生ID：")
        if studentID is not "":
            if os.path.exists(filename):
                with open(filename,"r")as rfile:
                    studen_old=rfile.readlines()
            else:
                student_old=[]
            ifdel=False
            if student_old:
                with open(filename,'w') as wfile:
                    d={}
                    for list in student_old:
                        d=dict(eval(list))
                        if d['id']!=studnetID:
                            wfile.write(str(d)+"\n")
                        else:
                            ifdel=True
                if ifdel:
                    print("ID为 %s 的学生信息已经被删除" % studentID) 
                else:
                    print("没有找到ID为 %s 的学生信息" % studentID)
            else:
                print("无学生信息")
                break
            show()
            inputMark=input("是否继续删除？ (y/n):")
            if inputMark =="y":
                mark=True
            else:
                mark=False
                break                                
def modify():
    filename="students.txt"
    show()
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            studentID=rfile.readlines()
    else:
        return
    studentID=input("请输入要修改的学生ID：")
    with open(filename,'w') as wfile:
        for student in student_old:
            d=dict(eval(student))
            if d["id"]==studentID:
                print("找到这名学生，可以修改它的信息")
                while True:
                    try: 
                        d["name"]=input("请输入姓名：")
                        d["english"]=int(input("请输入英语成绩："))
                        d["python"]=int(input("请输入python成绩"))
                        d["c"]=int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入")
                    else:
                        break
                student=str(d)
                wfile.write(student+"\n")
                print("修改成功！")
            else:
                wfile.write(student)
    mark=input("是否继续修改其他学生信息(y/n):")
    if mark=="y":
        modify()
    else:
        return       
def search():
    mark=True
    student_query=[]
    filename="students.txt"
    while mark:
        id=""
        name=""
        if os.path.exists(filename)
            mode=input("按ID查输入1；按姓名查输入2：")
            if mode=="1":
                id=input("请输入学生ID:")
            elif mode=="2":
                name=input("请输入学生姓名:")
            else:
                print("您输入有误，请重新输入！")
                search()
            while open(filename,'r')as file:
                student=file.readlines()
                for list in student:
                    d=dict(eval(list))
                    if id is not "":
                        if d['id']==id:
                            student_query.append(d)
                    elif name is not "":
                        if d['name']==name:
                            student_query.append(d)
                show_student(student_query)     #调用show_student函数
                student_query.clear()
                inputMark=input("是否继续查询？(y/n)")
                if inputMark =="y":
                    mark=True
                else:
                    mark=False
        else:
            print("暂未保存数据信息")
            return                       
def show_student(studentList):
    if not studentList:
        print("无数据")
        return

         

                                                   

if __name__=="__main__":
    main()
