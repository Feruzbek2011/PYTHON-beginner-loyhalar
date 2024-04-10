day = int(input("Tug`ilgan kuningizni kiriting: "))
month = input("Tug`ilgan oyingizni kiriting (mart, iyul va hk.): ")
if month == 'dekabr':
    astro_sign = 'o`qotar' if (day < 22) else 'tog` echkisi'
elif month == 'yanvar':
    astro_sign = 'tog` echkisi' if (day < 20) else 'qovg`a'
elif month == 'fevral':
    astro_sign = 'qovg`a' if (day < 19) else 'baliq'
elif month == 'mart':
    astro_sign = 'baliq' if (day < 21) else 'qo`y'
elif month == 'aprel':
    astro_sign = 'qo`y' if (day < 20) else 'buzoq'
elif month == 'may':
    astro_sign = 'buzoq' if (day < 21) else 'egizaklar'
elif month == 'iyun':
    astro_sign = 'egizaklar' if (day < 21) else 'qisqichbaqa'
elif month == 'iyul':
    astro_sign = 'qisqichbaqa' if (day < 23) else 'arslon'
elif month == 'avgust':
    astro_sign = 'arslon' if (day < 23) else 'parizod'
elif month == 'sentabr':
    astro_sign = 'parizod' if (day < 23) else 'tarozi'
elif month == 'oktabr':
    astro_sign = 'tarozi' if (day < 23) else 'chayon'
elif month == 'noyabr':
    astro_sign = 'chayon' if (day < 22) else 'o`qotar'
print("Burjni aniqlash :",astro_sign)
