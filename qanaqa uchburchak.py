a=int(input())
b=int(input())
c=int(input())

if a==b==c:
    print("bu teng tomonli uchburchak")
elif a==b or a==c or b==c:
    print("bu teng yonli uchburchak")
else:
    print("Turli tomonli uchburchak")
