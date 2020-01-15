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


# 生成含数据分析功能更防伪编码函数，参数schoice设置输出的文件名称
def scode4(schoice):
    intype = inputbox("\033[1;32m   请输入数据分析编号(3位字母):\033[0m", 2, 3)
    # 验证输入是否是三个字母，所以要判断输入是否是字母和输入长度是否为3
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox("\033[1;32m   请输入数据分析编号(3位字母):\033[0m", 2, 3)
    incount = inputbox("\033[1;32m    输入要生成的带数据分析功能的防伪码数量：\033[03", 1, 0)
    # 验证输入是否是大于零的整数，方法是判断输入转换为整数值时是否大于零
    while int(incount) == 0:  # 如果转换为整数时位零，则要求重新输入
        incount = inputbox("\033[1;32m   请输入要生成的带数据分析功能更的防伪编码数量：\033[0m", 1, 0)
    ffcode(incount, intype, "", schoice)  # 调用ffcode()函数生成防伪码


# 生成含数据分析功能防伪码函数：参数scount为要生成的防伪码数量；typestr为数据分析字符；
# 参数ismessage在输出完成时是否显示提示信息，为"no"不显示，为其他值显示；参数schoice设置输出的文件名称

def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()  # 清空保存批量防伪码信息的变量randstr
    # 按数量生成含数据分析功能更防伪码
    for j in range(int(scount)):
        strpro = typestr[0].upper()  # 取得三个字母中的第一个字母，并转为大写，区域分析码
        strtype = typestr[1].upper()  # 取得三个字母中的第二个字母，并转为大写，颜色分析码
        strclass = typestr[2].upper()  # 取得三个字母中的第三个字母，并转为大写，版本分析码
        randfir = random.sample(number, 3)  # 随机抽取防伪码中的三个位置，不分先后
        ransec = sorted(randfir)  # 对抽取的位置进行排序并赋值给randsec变量
        letterone = ""  # 情况存储单条防伪码的变量letterone
        for i in range(9):  # 生成9位的数字防伪码
            letterone = letterone + random.choice(number)
        # 将三个字母按randsec变量汇总存储的位置值添加到数字防伪码中，并保存到sim变量中
        sim = str(letterone[0:int(randsec[0])]) + strpro + str(
            letterone[int(randsec[0]):int(ransec[1])]) + strtype + str(
            letterone[int(ransec[1]):int(ransec[2])]) + strclass + str(letterone[int(ransec[2]):9]) + "\n"
        randstr.append(sim)  # 将组合生成的心防伪码添加到randstr变量
        # 调用wfile()函数，实现生成的防伪码屏幕输出和文件输出
        wfile(randstr, typestr + "scode" + str(schoice) + '.txt', ismessage, "生成含数据分析功能的防伪码共计：", "codepath")


def scode5(schoice):
    default_dir = r"codeauto.mri"  # 设置默认打开的文件名
    # 打开文件选择对话框，指定打开的文件名称为"codeauto.aut",扩展名为".mri"可以使用记事本打开和编辑
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file", "*.mri")], title=u"请选择只能批处理文件：",
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)  # 读取从文件选择对话框选中的文件
    # 以换行符为分隔符将读取的信息内容转换为列表
    codelist = codelist.split("\n")
    print(codelist)
    for item in codelist:  # 按读取的信息循环生成防伪码
        codea = item.split(",")[0]  # 信息用","分割，","前面的信息存储防伪码标准信息
        codeb = item.split(",")[1]  # 信息用","分割，","后面的信息存储防伪码生成的数量
        ffcode(codeb, codea, "no", schoice)  # 调用ffcode函数批量生成同一标识信息的防伪码


def scode6(schoice):
    default_dir = r"c:\ABDscode5.txt"  # 设置默认打开的文件名称
    # 按默认的文件名称打开文件选择对话框，用于打开已经存在的防伪码文件
    file_path = tkinter.filedialog.askopenfilename(title=u"请选择已经生成的防伪码文件", initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)  # 读取文件选择对话框选中的文件
    # 以换行符为分隔符将读取的信息内容转换为列表
    codelist = codelist.split("\n")
    codelist.remove("")  # 删除列表中的空行
    strset = codelist[0]  # 读取一行数据，以便获取原验证码的字母标志信息
    # 用maketrans()方法创建删除数字的字符映射转换表
    remove_digits = strset.maketrans("", "", digits)
    # 根据字符映射转换表删除该防伪码中的数字，获取字母标识信息
    res_letter = strset.maketrans(remove_digits)
    nres_letter = list(res_letter)  # 吧信息用列表变量nres_letter存储
    strpro = nres_letter[0]  # 从列表变量中取得第一个字母，即区域分析码
    strtype = nres_letter[1]  # 从列表变量中取得第二个字母，即色彩分析码
    strclass = nres_letter[2]  # 从列表变量中取得第三个字母，即版次分析码
    # 取出信息中的括号和引号
    nres_letter = strpro.replace(''''',").replace(''''', '') + strtype.replace(
        ''''','').replace(''''', '') + strclass.replace(''''','').replace(''''', '')
    card = set(codelist)
    # 利用tkinter的messagebox提示用户之前生成的防伪码数量
    tkinter.messagebox.showinfo("提示", "之前的防伪码共计：" + str(len(card)))
    root.withdraw()  # 关闭提示信息框
    incount = inputbox("请输入补充防伪码正常的数量：", 1, 0)  # 输入新补充生成的防伪码数量
    # 最大值按输入生成数量的2倍生成新防伪码
    # 放置新生成防伪码与原有防伪码重复造成新生成的方面数量不够
    for j in range(int(incount) * 2):
        randfir = random.sample(number, 3)  # 随机产生3位不重复的数字
        randsec = sorted(randfir)  # 对产生的数字排序
        addcount = len(card)  # 记录集合中防伪码的总数量
        strone = ''  # 情况存储单条防伪码的变量strone
        for i in range(9):  # 生成9位的数字防伪码
            strone = strone + random.choice(number)
        # 将三个字母按randsec变量中存储的位置值添加到数字防伪码中，并放到sim变量中
        sim = str(strone[0:int(randsec[0])]) + strpro + str(
            strone[int(randsec[0]):int(randsec[1])]) + strtype + str(
            strone[int(randsec[1]):int(randsec[2])]) + str(strone[int(randsec[2]):9]) \
              + "\n"
        card.add(sim)  # 添加新生成的防伪码到集合
        if len(card) > addcount:
            randstr.append(sim)  # 添加新生成的防伪码到新防伪码列表
        addcount = len(card)  # 记录新生成的防伪码集合的防伪码数量
        if len(randstr) >= int(incount):  # 如果新防伪码数量达到输入的防伪码数量
            print(len(randstr))  # 输出已正常的防伪码的数量
        break
    # 调用wfile()函数，实现生成的防伪码屏幕输出和文件输出
    wfile(randstr, nres_letter + "ncode" + str(choice) + ".txt", nres_letter, "生成后补防伪码共计：", "codeadd")


def scode7(choice):
    mainid = inputbox("\033[1;32m     请输入EN13的国家代码(3位)  :\33[0m", 1, 0)
    while int(mainid) < 1 or len(mainid) != 3:  # 验证输入是否为3位数字
        mainid = inputbox("\033[1;32m    请输入EN13的国家代码(3位) :\33[0m", 1, 0)
    compid = inputbox("\033[1;32m   请输入企业代码(4位)  :\33[0m", 1, 0)  # 输入企业代码
    while int(compid) < 1 or len(compid) != 4:  # 验证输入是否为4位数字
        compid = inputbox('\033[1;32m   请输入要生成的条形码数量：\033[0m', 1, 0)
    incount = inputbox('\033[1;32m   请输入要生成的条形码数量：\33[0m', 1, 0)
    mkdir("barcode")  # 判断保存条形码的文件夹是否存在，不存在，则创建文件夹
    for j in range(int(incount)):  # 批量生成条形码
        strone = ''  # 清空存储单条条形码的变量
        for i in range(5):  # 生成条形码的5位数字
            strone = strone + str(random.choice(number))
        barcode = mainid + compid + strone  # 把国家代码、企业代码和新生成的随机码进行组合
        # 计算条形码的校验位
        evensum = int(barcode[1]) + int(barcode[3]) + int(barcode[5]) + int(barcode[7]) + int(barcode[9]) + int(
            barcode[11])
        oddsum = int(barcode[0]) + int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(
            barcode[10])
        checkbit = int(10 - ((evensum * 3 + oddsum) % 10) % 10)
        barcode = barcode + str(checkbit)  # 组成完整的EAN13条形码的13位数字
        encoder = EAN13Encoder(barcode)  # 调用EAN13Encoder生成条形码
        encoder.save("barcode\\" + barcode + ".png")  # 保存掉行吗信息图片到文件


# 本函数生成固定的12位二维码，读者可以根据实际需要修改成按输入位数进行生成的函数
def scode8(schoice):
    # 输入要生成的二维码数量
    incount = inputbox("\033【1;32m    请输入要生成的12位数字二维码数量:\33[0m", 1, 0)
    while int(incount) == 0:  # 如果输入不是大于0的数字，重新输入
        incount = inputbox("\033[1;32m   请输入要生成的12位数字二维码数量:\33[0m", 1, 0)
    mkdir("qrcode")  # 判断保存二维码的文件夹是否存在，不存在，则创建该文件夹
    for j in range(int(incount)):  # 批量生成二维码数字
        strone = ''  # 清空存储单条二维码的变量
        for i in range(12):  # 生成单条二维码数字
            strone = strone + str(random.choice(number))
        encoder = qrcode.make(strone)
        encoder.save("qrcode\\" + strone & +".png")


def scode9(schoice):
    default_dir = r"lottery.ini"  # 设置默认打开文件为项目路径下的"lottery.ini"
    # 选择包含用户抽奖信息票号的文件，扩展名为".ini"
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Ini file", "*.ini")], title=u"请选择包含抽奖号码的抽奖文件:",
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)  # 调用openfile()函数读取刚打开的抽奖文件
    codelist = codelist.split("\n")  # 通过换行符把抽奖信息分割成抽奖列表
    # 要求用户输入中(抽)奖数量
    incount = inputbox("\033[1;32m    请输入要生成的抽奖数量：\33[0m", 1, 0)
    # 如果输入中(抽)奖数量等于0或超过抽奖数组数量，重新输入
    while int(incount) == 0 or len(codelist) < int(incount):
        incount = inputbox("\033[1;32m     请输入要生成的抽奖数量：\33[0m", 1, 0)
    strone = random.sample(codelist, int(incount))  # 根据输入的中奖数量进行抽奖
    for i in range(int(incount)):  # 循环将抽奖列表的引号和中括号去掉
        # 将抽奖列表的中括号去掉
        wdata = str(strone[i].replace('[', '')).replace(']', '')
        # 将抽奖列表的引号去掉
        wdata = wdata.replace(''''','').replace(''''', '')
        # 输出中奖信息
        print(wdata)


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
        # 选择菜单8,调用scode8()函数批量生成二维码
        if choice == 8:
            scode8(choice)
        # 选择菜单9,调用scode9()函数生成企业粉丝抽奖程序
        if choice == 9:
            scode9(choice)
        # 选择菜单0，退出系统
        if choice == 0:
            i = 0
            print("正在退出系统！")
    else:
        print("\033[1:31:40m 输入非法，请重新输入！！\033[0m")
        time.sleep(2)
