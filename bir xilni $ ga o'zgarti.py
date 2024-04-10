def belgi_uzgar(str1):
	belgi = str1[0]
	str1 = str1.replace(belgi, '$') # bir xillarini $ ga amashtirish
	str1 = belgi + str1[1:] # belgi+ str1ni[1:] yani 0 emas 1-sidan oxirigacha
	return str1
print(belgi_uzgar('restart'))