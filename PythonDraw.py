#!/usr/bin/env python
#-*- coding = utf-8 -*-
# -------------------------------画蟒蛇
import turtle as t  #海龟绘图库
t.setup(650,350,200,200)  #turtle绘图窗体的位置和大小（宽度，高度，窗体左上角的坐标）
t.penup()  #抬起画笔，海龟在飞行
t.fd(-250)  #fd表示向前进，负数表示倒退250（注意，并不会画下图形，因为画笔是抬起的）
t.pendown()   #落下画笔，海龟在爬行
t.pensize(25)  #海龟的宽度
t.pencolor("purple")   #海龟的颜色
t.seth(-40)   #改变海龟的行进角度-40度方向，注意不行进只改变方向

for i in range(4):
    t.circle(40,80)  #circle表示以海龟当前位置的左侧某个点为圆心，曲线运行。半径为40，角度为80，绘制弧形
    t.circle(-40,80)

t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40 * 2/3)
t.done()   #程序运行结束后不会自动退出，需手动关闭。若需自动退出，则删掉该行
