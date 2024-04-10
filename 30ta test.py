from random import randint
w=0
v=0
for s in range(30):
    a=randint(1,500)
    b=randint(1,500)
    c=int(input('{}+{} ='.format(a, b)))
    e=a+b
    if c == (a+b):
	    v+=1
	    print('to`g`ri')
    else:
	    print('xato',e)
w=30-int(v)
print(v ,'ta to`g`ri')
print(w ,'ta noto`g`ri')