def suz_yasovchi(a):
    if len(a)>2:
        a1=a[-3:]
        if a1=="ing":
            a+="ly"
        else:
            a+="ing"
    else:
        print("Iltimos 2 ta belgida ko'proq bo'lsin")
    return a
print(suz_yasovchi("ab"))
print(suz_yasovchi("abs"))
print(suz_yasovchi("string"))
