print("Oylar ro`yxati: Yanvar, Fevral, Mart, Aprel,May, Iyun, Iyul, Avgust, Sentabr, Oktabr, Noyabr,Dekabr")
month_name = input("Oy nomini kiriting: ")
if month_name == "Fevral":
    print("Oyda 28/29 kun bor")
elif month_name in ("Aprel", "Iyun", "Sentabr","Noyabr"):
    print("Oyda 30 kun bor")
elif month_name in ("Yanvar", "Mart", "May","Iyul", "Avgust", "Oktabr", "Dekabr"):
    print("Oyda 31 kun bor")
else:
    print("Oy nomi xato")
