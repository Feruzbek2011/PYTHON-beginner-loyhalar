def mediana():
    a=float(input())
    b=float(input())
    c=float(input())

    if b<a<c or c<a<b:
        print("mediana: ",a)
    elif a<b<c or c<b<a:
        print("mediana: ",b)
    else:
        print("mediana: ",c)
mediana()
