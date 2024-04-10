def fname(a,b):
    q=0
    a=set(a)
    b=set(b)
    for value in a:
        if value in b:
            q+=1
            print(f"bir xil xarf {value}")
    if q<1:
        print("bir xillik yo'q")

fname("PHP","Python")
fname("Java","Python")
fname("Feruzbek","Fayozbek")
