a=input('')
# d=a.dict([])
# a1=next(s)
# a2=next(s)
# a3=next(s)
# print(a,d)
s=a.count('/')
if s>0:
	# print(s)
	# son=a.index("/")
	s=a.replace('/',' ')
	d=s.split()
	son2=d[1]
	son3=d[0]
	natija=int(son3)/int(son2)
	print(natija)
s=a.count('*')
if s>0:
	# print(s)
	# son=a.index("/")
	s=a.replace('*',' ')
	d=s.split()
	son2=d[1]
	son3=d[0]
	natija=int(son3)*int(son2)
	print(natija)
s=a.count('+')
if s>0:
	# print(s)
	# son=a.index("/")
	s=a.replace('+',' ')
	d=s.split()
	son2=d[1]
	son3=d[0]
	natija=int(son3)+int(son2)
	print(natija)
s=a.count('-')
if s>0:
	# print(s)
	# son=a.index("/")
	s=a.replace('-',' ')
	d=s.split()
	son2=d[1]
	son3=d[0]
	natija=int(son3)-int(son2)
	print(natija)

# sinov=[a]
# sinov.insert(1, "S  ")
# print(sinov)