b=[] # b degan list yaratyapmiz
for value in range(101): #101 gacha sonlarni birmabir vaule ga qo'y.
    if "2" in str(value): # Agar value da 2 soni bo'lsa
        b.append(value)  # b listga valueni qo'sh
print(b) # b listtini chiqar
