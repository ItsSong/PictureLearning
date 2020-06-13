#!/usr/bin/env python
#-*- coding = utf-8 -*-
# 自动轨迹绘制基础
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

#读取数据
datas = []  #建立一个空列表
f = open("data.txt")
#遍历文件中数据
for line in f:
    line = line.replace("\n","")   #将换行符换成空字符串，并赋值给line
    datas.append(list(map(eval, line.split(","))))
f.close()

#自动绘制
for i in range(len(datas)):
    t.pencolor(datas[i][3],datas[i][4],datas[i][5])
    t.fd(datas[i][0])
    if datas[i][1]:
        t.right(datas[i][2])
    else:
        t.left(datas[i][2])