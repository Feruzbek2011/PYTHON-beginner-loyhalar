# Python dasturini yozing.
# Dastur kodi
# Dastur
# natijasi
from datetime import date
print("Oy va sanani kiriting \n(bitta bo'sh joy bilan ajratilgan):")
oy, sana = map(int, input().split())
hafta={
1:'Dushanba',2:'Seshanba',3:'Chorshanba',4:'Payshanba',5:'Juma',
6:'Shanba',7:'Yakshanba'
}
kun = date.isoweekday(date(2023, oy, sana))
print("Hafta kuni: ",hafta[kun])