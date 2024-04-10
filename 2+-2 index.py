def fname(a):
    if len(a)>1: # Agar a ni belgisi 1 dan katta bo'lsa
        return a[0:2]+a[-2:] # a[0:2]+a[-2:] consolga chiqar
    else:
        return " " # bo'sh joyni consolga chiqar.
print(fname("python")) # funksiyani ishlatib ko'beryapmiz
print(fname("u")) # funksiyani ishlatib ko'beryapmiz
