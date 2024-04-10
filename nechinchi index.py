def func(a,b):
       if b in a:
           return a.index(b)
       else:
           return -1
print(func("Uzbekistan", "i"))
print(func("Feruzbek","d"))
