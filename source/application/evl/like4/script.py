#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 1:04
# @Author  : Lewic
# @File    : script.py
# @Software: PyCharm
# @context :


from tkinter import *  # _all_ = [a,b]
from tkinter import messagebox


def closeWindow():
    messagebox.showinfo(title="警告", message="不许关闭，好好回答")
    return


# 点击喜欢触发的方法
def Love():
    # Toplevel独立的顶级窗口，和父级标题一样
    love = Toplevel(window)
    love.geometry("300x90+540+360")
    love.title("好巧，我也是")
    label = Label(love, text="好巧，我也是", font=("微软雅黑", 20))
    label.pack()
    # label1 = Label(love,text="加个微信呗",font =("微软雅黑",20))
    # label1.pack()
    # entry = Entry(love,font = ("微软雅黑",15))
    # entry.pack()
    btn = Button(love, text="确定", width=10, height=1, command=close_all)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)


def closelove():
    return


# 关闭所有的窗口   注意，如果父级窗口关了，下面的所有窗口均会关闭
def close_all():
    # destory 销毁
    window.destroy()


# 关闭不喜欢框的X时
def closenolove():
    # messagebox.showinfo("再考虑一下","再考虑一下呗")
    # return
    disLove()


# 点击不喜欢触发的事件
def disLove():
    no_love = Toplevel(window)
    no_love.geometry("300x90+540+360")
    no_love.title("再考虑考虑")
    label = Label(no_love, text="再考虑考虑呗！", font=("微软雅黑", 25))
    label.pack()
    btn = Button(no_love, text="好的", width=10, height=1, command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW", closenolove)


# 创建窗口
window = Tk()  # 类的实例化，创建窗口,window仅仅是个变量

# 窗口标题
window.title("你喜欢我吗？")

# 窗口的大小   运用小写的x来连接
window.geometry("380x400")

# 窗口位置（距离屏幕左上角）      运用+来连接
window.geometry("+500+240")  # geometry意为几何
# 上述可以写成window.geometry("380x200+500+245")，其中+是用来连接的

# 用户关闭窗口触发的事件
window.protocol("WM_DELETE_WINDOW", closeWindow)

# 标签控件，一般第一个参数均是父级窗口         ，这里传参为window           fg设置颜色
label = Label(window, text="Hey,小姐姐", font=("微软雅黑", 15), fg="black")

# 定位  grid（网格式） pack（包的方式） place(用的最少的一种，根据位置)
label.grid(row=0, column=0)  # 默认值为 0  0

label_1 = Label(window, text="喜欢我吗？", font=("微软雅黑", 25))
label_1.grid(row=1, column=1, sticky=E)  # sticky为对齐方式  N上S下W左E右

#  显示图片
photo = PhotoImage(file="heart.png")
imageLable = Label(window, image=photo)
# column 组件所跨越的列数
imageLable.grid(row=2, columnspan=2)  # 跨列操作

# 按钮控件           点击触发command事件
btn = Button(window, text="喜欢", width=15, height=1, command=Love)
btn.grid(row=3, column=0, sticky=W)

btn1 = Button(window, text="不喜欢", command=disLove)
btn1.grid(row=3, column=1, sticky=E)
# 显示窗口 消息循环
window.mainloop()
