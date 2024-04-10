def absd():
	a=int(input()) # a degan input yaratyapmiz
	b=int(input()) # b degan input yaratyapmiz
	s=int(input()) # s degan input yaratyapmiz
	d=int(input()) # d degan input yaratyapmiz
	if 0< a <1000 and 0<b<1000 and 0<s<1000 and 0<d<1000: # Agar hamma inputlar 0 dan katta 1000dan kichik bo'lsa
		n=a**b+s**d # a ni b darajasi + s ni d darajasi
		print(n) # n ni consolga chiqaryapmiz
	else:
		print('0 dan katta 1000 dan kichik son kiriting!') # '0 dan katta 1000 dan kichik son kiriting!' consolga chiqaryapmiz
absd()
