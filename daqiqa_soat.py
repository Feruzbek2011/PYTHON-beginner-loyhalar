def sekund():
	a=int(input('sekund kiriting: '))
	k=a//(3600*24)
	a -= (k*3600*24)
	s=a//3600
	a-=(s*3600)
	d=a//60
	a-=(d*60)
	print(f'{k}:{s}:{d}:{a}')
sekund()