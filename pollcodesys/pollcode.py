# -*- coding: utf-8 -*- 
"""
项目: ProjectCases
作者: 张强
创建时间: 2019-12-30 15:42
IDE: PyCharm
介绍:
"""

import os, time, string, random, tkinter, qrcode
from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from string import digits

root = tkinter.Tk(digits)  # tkinter模块为python的标准图形界面接口。建立根窗口
# 初始化数据
number = '1234567890'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&()_+"
i = 0
randstr = []
fourth = []
fifth = []
randfir = ''
randsec = ''
randthr = ''
str_one = ''
strone = ''
strtwo = ''
nextcard = ''
userput = ''
nres_letter = ''


def mkdir(path):  # 创建文件夹函数
    isexists = os.path.exists(path)  # 判断文件夹路径是否存在
    if not isexists:  # 如果文件夹路径不存在
        os.mkdir(path)  # 创建要创建的文件夹


def openfile(filename):  # 读取文件内容函数
    f = open(filename)  # 打开指定文件
    fllist = f.read()  # 读取文件内容
    f.close()  # 关闭文件
    return fllist  # 返回读取的文件内容


def inputbox(showstr, showorder, length):
    instr = input(showstr)  # 使用input函数要求用户输入信息，showstr为输入提示文字
    if len(instr) != 0:  # 输入数据的长度不为零
        # 分成三种验证方式，1：数字，不限位数；2：字符；3：数字且有位数要求
        if showorder == 1:  # 验证方式1，数字格式，不限位数，大于零的整数
            if str.isdigit(instr):  # 验证是否为数字
                if instr == 0:  # 验证数字是否为0，如果是要求重新输入，返回值为“0”
                    print("\033[1;31;40m 输入为零，请重新输入！！\033[0m")  # 要求重新输入
                    return "0"  # 函数返回值为“0”
                else:  # 如果输入正确，返回输入的数据
                    return instr  # 将输入的数据传给函数返回值
            else:  # 如果输入的不是数字，要求用户重新输入，函数返回值为“0”
                print("\033[1;31;40m输入非法，请重新输入!!、033[0m")  # 要求重新输入
                return "0"  # 函数返回值为“0”
        if showorder == 2:  # 验证方式2，要求字母格式且是指定字母
            if str.isalpha(instr):
                if len(instr) != length:
                    print("\033[1;31;40m必须输入" + str(length) + "个字母，请重新输入！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入!!、033[0m")
                return "0"
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print("\033[1;31;40m必须输入" + str(length) + "个数字，请重新输入！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入为空，请重新输入！\033[0m")
                return "0"


def wfile(sstr, sfile, typeis, smsg):
    def wfile(sstr, sfile, typeis, smsg, datapath):
        mkdir(datapath)
        datafile = datapath + '\\' + sfile
        file = open(datafile, 'w')
        wrlist = sstr
        pdata = ""
        wdata = ""
        for i in range(len(wrlist)):
            wdata = str(wrlist[i].replace('[', '')).replace(']', '')
            wdata = wdata.replace(''''','').replace(''''', '')
            file.write(str(wdata))
            pdata = pdata + wdata

        file.close()
        print("\033[1;31m" + pdata + "\033[0m")
        if typeis != "no":
            tkinter.messagebox.showinfo("提示", smsg + str(len(randstr)) + '\n防伪码文件存放位置：' + datafile)
            root.withdraw()


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print("\033[1;31;40m   输入非法，请重新输入！！\033[0m")
            return 0
        else:
            return insel
    else:
        print("\033[1;31;40m    输入非法，请重新输入！！\033[0m")
        return 0


def scode1(schoice):
    # 调用inputbox函数对输入数据进行非空、输入合法性判断
    incount = inputbox("\033[1;32m       请输入您要生成防伪码的数量:\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m     请输入您要生成防伪码的数量：\33[0m", 1, 0)
    randstr.clear()  # 清空保存批量防伪码信息的变量randstr
    for j in range(int(incount)):
        randfir = ''
        for i in range(6):  # 循环生成单条防伪码
            randfir = randfir + random.choice(number)  # 产生数字随机因子
        randfir = randfir + "\n"  # 在单条防伪码后面添加转义换行符\n,使验证码单条列显示
        randstr.append(randfir)  # 将单条防伪码添加到保存批量验证码的变量randstr
    # 调用函数wfile(),实现生成的防伪码屏幕输出和文件输出
    wfile(randstr, "scode" + str(schoice) + ".txt", "已生成6位防伪码共计：", "codepath")


def scode2(schoice):
    ordstart = inputbox("\033[1;32m    请输入系列产品的数字起始号(3位)：\33[0m", 3, 3)
    # 如果输入的系列产品起始号不是三位数，则要求重新输入
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m   请输入系列产品的数字起始号(3位):\33[0m", 3, 3)
    ordcount = inputbox("\033[1;32m   请输入系列产品系列的数量:", 1, 0)
    # 如果输入的产品系列数量小于1或大于9999，则要求重新输入
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount == inputbox("\033[1;32m   请输入产品系列的数量：", 1, 0)
    incount = inputbox("\033[1;32m     请输入要生成的每个系列产品的防伪码数量：\33[0m", 1, 0)
    while int(incount) == 0:  # 如果输入为字母或数字0，则要求重新输入
        incount = inputbox("\033[1;32m    请输入要生成的防伪码数量：\33[0m", 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            # 将生成的单条防伪码添加到防伪码列表
            randstr.append(str(int(ordstart) + m) + randfir + "\n")
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成9位系列产品防伪码共计:", "codepath")


# 生成25位混合产品序列号函数，参数schoice设置输出的文件名称
def scode3(schoice):
    # 输入要生成 的防伪码数量
    incount = inputbox("\033[1;32m     请输入要生成的25位混合产品序列号数量:\33[0m", 1, 0)
    while int(incount) == 0:  # 如果输入非法(符号、字母或者数字0都认为是非法输入),重新输入
        incount = inputbox("\033[1;32m     请输入要生成的25位混合产品序列号数量:\33[0m", 1, 0)
    randstr.clear()  # 情况保存批量防伪码信息的变量randstr
    for j in range(int(incount)):  # 按输入数量生成防伪码
        strone = ''

        for i in range(25):
            # 每次产生一个随机因子，也就是每次产生单条防伪码的一位
            strone = strone + random.choice(letter)
        # 将正常的防伪码每隔5位添加横线"
        strtwo = strone[:5] + "-" + strone[5:10] + "-" + strone[10:15] + "-" + strone[15:20] + "-" + strone[
                                                                                                     20:25] + "\n"
        randstr.append(strtwo)  # 添加防伪码到防伪码列表
        # 调用函数wfile(),实现生成的防伪码在屏幕输出和文件输出
        wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成25混合防伪序列码共计：", "codepath")


def scode4(choice):
    pass


def scode5(choice):
    pass


def scode6(choice):
    pass


def scode7(choice):
    pass


def scode8(choice):
    pass


def scode9(choice):
    pass


def mainmenu():
    print("""\033[1;35m
    *******************************************************************
                    企业编码生成系统
    *******************************************************************
        1.生成6位数字防伪编码(213563型)
        2.生成9位系列产品数字防伪编码(879-335439型)
        3.生成25位混合产品序列号(B2R12-N7TE8-9IET2-FE350-DW2K4型)
        4.生成含数据分析功能的防伪编码(5A61M0583D2)
        5.智能批量生成带数据分析功能的防伪码
        6.后续补加生成防伪码(5A61M0583D2)
        7.EAN-13条形码批量生成
        8.二维码批量输出
        9.企业粉丝防伪码抽奖
        0.退出系统
    ====================================================================
        说明：通过数字键选择
    =========================================================== ========
    \033[0m""")


# 通过循环控制用户对程序功能的选择
while i < 9:
    # 调用程序主界面菜单
    mainmenu()
    # 键盘输入需要操作的选项
    choice = input("\033[1;32m   请输入您要操作的菜单选项:\33[0m")
    if len(choice) != 0:  # 输入如果不为空
        choice == input_validation(choice)  # 验证输入是否为数字
        if choice == 1:
            scode1(str(choice))  # 如果输入大于零的整数，调用scode1()函数生成防伪码
        # 选择菜单2，调用scode2()函数生成9位系统产品数字防伪编码
        if choice == 2:
            scode2(choice)
        # 选择菜单3，调用scode3()函数生成25位混合产品序列号
        if choice == 3:
            scode3(choice)
        # 选择菜单4，调用scode4()函数生成含数据分析功能的防伪编码
        if choice == 4:
            scode4(choice)
        # 选择菜单5，调用scode5()函数智能批量生成带数据分析功能的防伪码
        if choice == 5:
            scode5(choice)
        # 选择菜单6，调用scode6()函数后续补加生成防伪码
        if choice == 6:
            scode6(choice)
        # 选择菜单7，调用scode7()函数批量生成条形码
        if choice == 7:
            scode7(choice)
        # 选择菜单8，调用scode8()函数批量生成二维码
        if choice == 8:
            scode8(choice)
        # 选择菜单9，调用scode9()函数实现企业粉丝抽奖
        if choice == 9:
            scode9(choice)
        # 选择菜单0，退出系统
        if choice == 0:
            i = 0
            print("正在退出系统！")
    else:
        print("\033[1:31:40m 输入非法，请重新输入！！\033[0m")
        time.sleep(2)
