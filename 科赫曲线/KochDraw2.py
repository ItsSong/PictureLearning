#!/usr/bin/env python
#-*- coding = utf-8 -*-
#绘制科赫雪花
import turtle
def koch(size,n):   #曲线的长度；绘制的阶数n
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:   #线的角度
            turtle.left(angle)
            koch(size/3, n-1)

def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3    #3阶科赫雪花
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
    turtle.done()    #需要自己关闭运行窗口界面，若无此行代码则程序运行完自动关闭窗口

main()