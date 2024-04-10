import turtle as tur
tur.speed(5)
tur.penup()
tur.goto(150,-75)
tur.pendown()

tur.bgcolor('#0270d9')
tur.color('white')
tur.width(23)

tur.left(90)
for i in range(4):
	tur.forward(150)
	tur.circle(70,90)

tur.penup()
tur.goto(80,0)
tur.pendown()
tur.circle(70)
tur.penup()
tur.goto(90,90)
tur.pendown()
tur.circle(7,360)

tur.done()