def almash(a,b):
	suz1=a[:2]+b[2:] # a[:2] bu boshidan 3-belgisini + b[2:] bu 3-belgidan oxirigacha
	suz2=b[:2]+a[2:] # b[:2] bu boshidan 3-belgisini + a[2:] bu 3-belgidan oxirigacha
	return suz1+' '+suz2

print(almash('rubekistan','uzssiya'))
