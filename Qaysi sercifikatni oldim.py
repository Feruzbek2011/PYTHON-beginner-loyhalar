from sklearn import tree

a = tree.DecisionTreeClassifier()
a1=input("kiriting: ")
x=[
[51],[52],[60],[61],[0],[-1],[100],[101]
]
y=[
"B1","B2","B2","C1","B1","Kechirasiz bunday bo'lmaydi!","C1","Kechirasiz bunday bo'lmaydi!"
]
b=a.fit(x,y)

n=b.predict([[a1]])
print(n)