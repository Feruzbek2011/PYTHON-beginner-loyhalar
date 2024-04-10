year = int(input("Tug`ilgan yilingizni kiriting: "))
if (year - 2000) % 12 == 0:
    sign = 'Baliq'
elif (year - 2000) % 12 == 1:
    sign = 'Ilon'
elif (year - 2000) % 12 == 2:
    sign = 'Ot'
elif (year - 2000) % 12 == 3:
    sign = 'Qo`y'
elif (year - 2000) % 12 == 4:
    sign = 'Maymun'
elif (year - 2000) % 12 == 5:
    sign = 'Tovuq'
elif (year - 2000) % 12 == 6:
    sign = 'It'
elif (year - 2000) % 12 == 7:
    sign = 'To`ng`iz'
elif (year - 2000) % 12 == 8:
    sign = 'Sichqon'
elif (year - 2000) % 12 == 9:
    sign = 'Sigir'
elif (year - 2000) % 12 == 10:
    sign = 'Yo`lbars'
else:
    sign = 'Quyon'
print("Sizning muchalingiz :",sign)
