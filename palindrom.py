def palindrom():
	a=int(input('palindrom son kiriting: '))
	if str(a) == str(a)[::-1]:
		print(True)
	else:
		print(False)
palindrom()