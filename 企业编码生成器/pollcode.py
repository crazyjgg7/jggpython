import os
import random
import string
import tkinter


def mkdir():     #创建目录
    isexists=os.path.exists(path)
    if not isexists:
        os.mkdir(path)
def openfile():   #打开文件读取内容
    with open(filename,'r',encoding="utf-8") as rfile:
        filelist=rfile.readlines()
        return filelist

def inputbox(showstr,showorder,length):
    instr=input(showstr)#用input函数提示客户输入信息，showstr为提示文字
    if len(instr) !=0:#输入长度不为空
        if showorder==1:#验证方式为1，要求数字格式，不限位数，大于0整数
            if str.isdigit(instr):   #str.isdigit检验字符串是否为整数
                if instr==0:
                    print("输入的整数是0，请重新输入")
                    return "0"
                else:
                    return instr
            else:
                print("输入非法请重新输入")
                return "0"
        elif showorder==2:  #验证方式为2，需要字母格式
            if str.isalpha(instr):
                if len(instr)!=length:
                    print("必须输入"+str(length)+"个字母，请重新输入")
                    return "0"
                else:
                    return instr
            else:
                print("输入不是字母非法，请重新输入")
                return "0"
        elif showorder==3: #验证方式为3，要求数字格式并且输入位数有要求
            if str.isdigit(instr):#确定是否输入的为整数类型
                if len(instr)!=length:
                    print("必须输入"+str(length)+"个数字，请重新输入")
                    return "0"
                else:
                    return instr
            else:
                print("输入的不是整数类型，请重新输入")
                return "0"
    else:
        print("\033[1;31;40m输入为空，请重新输入！！\033[0m")

def wfile(sstr,sfile,smsg,datapath):
    '''
    sstr是生成得防伪码   sfile是保存防伪码的文件名   smsg是提示框弹出的消息   datapath是保存防伪码的路径
    '''
    def wfile(sstr,sfile,typeis,smsg,datapath):
    mkdir(datapath)#调用函数创建文件夹
    datafile=datapath+"\\"+sfile#设置保存防伪码的文件 
    file=open(datafile,'w')#打开保存防伪码的文件，如果文件不存在就创建
    wrlist=sstr   #把防伪码信息赋值给 wrlist   
    
