import os,time,string,random.tkinter,qrcode
from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from string import digits
root=tkinter.TK()
number="1234567890"
lettter="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i=0
randstr=[]
fourth=[]
fifth=[]
randfir=""
randsec=""
randthr=""
str_one=""
strone=""
strtwo=""
nextcard=""
userput=""
nres_letter=""


def mkdir(path):     #创建目录
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
    pdata=""  #清空变量padata  pdata存储保存到文本文件的防伪码
    wdata=""  #清空变量wdata wdata保存到文本文件的防伪码 
    for i in range(len(wrlist)):
        wdata=str(wrlist[i].replace('[','')).replace('[','')#去掉字符的中括号
        wdata=wdata.replace(''''','').replace(''''','')
        file.write(sr(wdata))
        pdata=pdata+wdata
    file.close()
    print(pdata)
    if typeis != "no"  #
        tkinter.messagebox.showinfo("提示",smsg+str(len(rendstr))+"\n防伪码存放位置:"+datafile)
        root.withdraw()   #关闭辅助窗口

def mainmenu():

    print("""
    ***************************************************************************
         1.生成6位数字防伪编码（2135563型）
         2.生成9位系列产品数字防伪编码（879-335439型）
         3.生成25位混合产品序列号（B2R12-N7TE8-9IET2-FE350-DW2K4型）
         4.生成含数据分析功能的防伪编码（5A61M0583D2）
         5.智能批量生成带数据分析功能的防伪码
         6.后续补加生成防伪码（5A61M0583D2）
         7.EAN-13条形码批量生成
         8.二维码批量输出
         9.企业粉丝防伪码抽奖
         0.退出系统
    ============================================================================
    说明：通过数字选择菜单
    ============================================================================     

    """)

    while i<9:
        mainmenu()
        if len(choice) !=0:
            choice=input_validation(choice)
            if choice==1:
                scode1(str(choice))
            if choice==2:
                scode2(choice)
            if choice==3:
                scode3(choice)
            if choice==4:
                scode4("",choice)
            if choice==5:
                scode5(choice)
            if choice==6:
                scode6(choice)
            if choice==7:
                scode7(choice)
            if choice==8:
                scode8(choice)
            if choice==9:
                scode9(choice)
            if choice==0:
                i=0
                print("正在退出系统")                  
        else:
            print("输入非法，请重新输入")

def input_validation(insel):
    if str.isdigit(insel):
        if insel==0:
            print("输入非法，请重新输入")
            return 0
        else：
            return insel
    else：
        print("输入非法，请重新输入")
        return 0
def scode1(schoice):#生成6位数字防伪码
    incount=inputbox("输输入你要生成防伪码的数量")
    while int(incount)==0:
        incount=inputbox("请输入你要生成防伪码的数量")
    randstr.clear()
    for j in range(int(incount)):
        randfir=''
        for i in range(6):
            randfir=randfir+random.choice(number) 
        randfir=randfir+"\n"
        randstr.append(randfir)
    wfile(randstr,"scode"+str(schoice)+".txt","","已生成6位防伪码共计：","codepath")  
def scode2(schoice):  #9位系列产品数字防伪编码
    ordstart=inputbox("请输入系统产品的数字起始号")  
    while int(ordstart)==0:
        ordstart=input("请输入系列产品的数字起始号")
    ordcount=inputbox("请输入产品系列的数量")
    while int(ordcount)<1 or int(ordcount)>9999:
        ordcount=inputbox("请输入产品系列的数量")
    incount=inputbox("请输入要生成的每个系列产品的防伪码数量")
    while int(incount)==0:
        incount=inputbox("请输入要生成的防伪码的数量") 
    randstr.clear()
    for m in range(int(ordcount)):
        for j inrange(int(incount)):
            randfir=''
            for i in range(6):
                randfir=randfir+random.choice(number)
            randstr.append(str(int(ordstart)+m)+randfir+"\n")
    wfile(randstr,"scode"+str(schoice)+".txt","","已生成9位系列产品防伪码共计：","codepath")


def scode3(schoice):#25位混合产品序列号数量
    incount=inputbox("请输入要生成的25位混合产品序列号数量")
    while int(incount)==0:
        incount=inputbox("请输入非法(符号、字母或者数字0都认为是非法输入)，重新输入")
    randstr.clear()
    for j in range(int(incount)):
        strone=''
        for i in range(25):
            strone=strone+random.choice(letter) 
        strtwo=strone[:5]+"-"+strone[5:10]+"-"+strone[10:15]+"-"+strone[15:20]+"-"+strone[20:25]+"\n"
        randstr.append(strtwo)
    wfile(randstr,"scode"+str(schoice)+".txt","","已生成25混合防伪序列码共计："，"codepath") 

def scode4(schoice):#数据分析功能的防伪编码
    intype=inputbox("请输入数据分析编号(3位字母)")
    while not str.isalpha(intype) or len(intype)!=3:
        intype=inputbox("请输入数据分析编号(3位字母)")   
    incount=inputbox("输入要生成的带数据分析功能的防伪码数量")
    while int(incount)==0:
        incount=inputbox("请输入要生成的带数据分析功能的防伪码数量")
    ffcode(incount,intype,"",schoice)                                 

                     
def ffcode(scount,typestr,ismessage,schoice):  #调用ffcode()函数将数据分析码随机插入到防伪码，第一个字母一定
    randstr.clear()
    for j in range(int(scount)):
        strpro=typestr[0].upper()#取得三个字母中的第一个字母，并转为大写，区域分析
        strtype=typestr[1].upper()
        strclass=typestr[2].upper()
        randfir=random.sample(number,3)
        randsec=sorted(randfir)
        letterone=""
        for i in range(9):
            letterone=letterone+random.choice(number)
        sim=str(letterone[0:int(randsec[0])])+strpro+str(letterone[int(randsec[0]):int(randsec[1])])+strtype+str(letterone[int(randsec[1]):int(randsec[2])])+strclass+str(letterone[int(randsec[2]):9]+"\n")
        randstr.append(sim)
    wfile(randstr,typestr+"scode"+str(schoice)+".txt",ismessage,"生成含数据分析功能的防伪码共计：","codepath")



    
