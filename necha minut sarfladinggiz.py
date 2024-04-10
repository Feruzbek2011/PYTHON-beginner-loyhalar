soat1=int(input('soat nechi edi: '))
minut1=int(input('minut nechi edi: '))
secund1=int(input('secund nechi edi: '))
soat2=int(input('soat nechi bo`ldi : '))
minut2=int(input('minut nechi bo`ldi : '))
secund2=int(input('secund nechi bo`ldi: '))
soat=soat2-soat1
minut=minut2-minut1
secund=secund2-secund1
if secund==secund<0:
	a=secund+60
	b=minut-1
else:
	a=secund
	b=minut
if minut==minut<0:
	b=minut+60
	c=soat-1
else:
	c=soat
	b=minut
print('soat:{}'.format(c),'minut:{}'.format(b),'secund:{}'.format(a))
print('{}:'.format(c),'{}:'.format(b),'{}'.format(a))