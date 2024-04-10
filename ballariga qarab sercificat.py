from sklearn import tree

a = tree.DecisionTreeClassifier()
a1=int(input("1-ni kiriting: "))
a2=int(input("2-ni kiriting: "))
a3=int(input("3-ni kiriting: "))
a4=int(input("4-ni kiriting: "))
an=(a1+a2+a3+a4)/4



x=[
[51],[52],[60],[61],[0],[-1],[100],[101]
]
y=[
"B1","B2","B2","C1","B1","Kechirasiz bunday bo'lmaydi!","C1","Kechirasiz bunday bo'lmaydi!"
]
b=a.fit(x,y)

n=b.predict([[an]])
print(n)