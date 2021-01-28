#PythonDraw.py
'''import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("red")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#蟒蛇
'''
import turtle as t
t.setup(850,350,200,200)
t.penup()
t.fd(-350)
t.pendown()
t.pensize(25)
t.pencolor("green")
t.seth(-40)
for i in range(5):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,40)
t.fd(100)
t.circle(30,180)
t.fd(300)
t.done()
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#正方形
'''import turtle as t
t.setup(600,600,100,100)
t.penup()
t.fd(-200)
t.left(90)
t.fd(200)
t.right(90)
t.pendown()
t.pensize(10)
t.pencolor("black")
for i in range(4):
    t.fd(400)
    t.right(90)
t.done()
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#六边形
'''import turtle as t
t.setup(600,600,50,50)
t.penup()
t.fd(-125)
t.seth(90)
t.fd(250)
t.seth(0)
t.pendown()
t.pensize(10)
t.pencolor("black")
for i in range(6):
    t.fd(250)
    t.right(60)
t.done()
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#叠边形
'''import turtle as t
t.setup(600,600,50,50)
t.penup()
t.fd(-100)
t.seth(90)
t.fd(100)
t.seth(45)
t.pendown()
t.pensize(10)
t.pencolor("black")
for i in range(5):
     t.fd(200)
     t.right(72)
t.penup()
t.seth(90)
t.fd(200/2)
t.seth(0)
t.fd(200/3)
t.pendown()
for i in range(5):
    t.fd(200)
    t.right(72)
t.done()
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#风轮
import turtle 
turtle.setup(600,600,50,50)
turtle.pensize(10)
for i in range(4):
    if i == 0:
        turtle.pencolor("purple")
    elif i == 1:
        turtle.pencolor("red")
    elif i == 2:
    	turtle.pencolor("green")
    else:
    	turtle.pencolor("yellow")
    turtle.fd(200)
    turtle.right(90)
    turtle.circle(-200,45)
    turtle.goto(0,0)
    turtle.seth((i+1)*90)
turtle.done()
