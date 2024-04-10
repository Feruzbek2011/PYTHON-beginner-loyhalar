import turtle
a=0
b=0
turtle.speed(18)
turtle.bgcolor('black')
turtle.pencolor('cyan')
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
while True:
	turtle.forward(a)
	turtle.right(b)
	a+=3
	b+=1
