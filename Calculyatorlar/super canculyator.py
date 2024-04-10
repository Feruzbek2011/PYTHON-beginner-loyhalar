from tkinter import *
from tkinter.font import *
oyna=Tk()
oyna.title("Kalkulyator")
oyna.geometry("280x350")
oyna.configure(bg="dodger blue")
myfont=Font(size=15)
n=Entry(oyna, width=21, font=myfont)
n.grid(row=0, column=0)
n.place(x=20, y=20)
k=0
l=0
s=""
def t1():
	return n.insert(END,"1")
def t2():
	return n.insert(END,"2")
def t3():
	return n.insert(END,"3")
def t4():
	return n.insert(END,"4")
def t5():
	return n.insert(END,"5")
def t6():
	return n.insert(END,"6")
def t7():
	return n.insert(END,"7")
def t8():
	return n.insert(END,"8")
def t9():
	return n.insert(END,"9")
def t0():
	return n.insert(END,"0")
def tp():
	global s,k
	k=int(n.get())
	n.delete(0,END)
	s="+"
	return
def tm():
	global s,k
	k=int(n.get())
	n.delete(0,END)
	s="-"
	return
def tk():
	global s,k
	k=int(n.get())
	n.delete(0,END)
	s="*"
	return
def tb():
	global s,k
	k=int(n.get())
	n.delete(0,END)
	s="/"
	return
def tc():
	return n.delete(0,END)
def nat():
	global s,k,l
	if s=="+":
		l=int(n.get())
		n.delete(0,END)
		n.insert(END,str(k+l))
	if s=="-":
		l=int(n.get())
		n.delete(0,END)
		n.insert(END,str(k-l))
	if s=="*":
		l=int(n.get())
		n.delete(0,END)
		n.insert(END,str(k*l))
	if s=="/":
		l=int(n.get())
		n.delete(0,END)
		n.insert(END,str(k/l))
	return
Button(oyna, text="1", width=4, font=myfont, bg="spring green",
command=t1).place(x=20, y=80)
Button(oyna, text="2", width=4, font=myfont, bg="spring green",
command=t2).place(x=80, y=80)
Button(oyna, text="3", width=4, font=myfont, bg="spring green",
command=t3).place(x=140, y=80)
Button(oyna, text="4", width=4, font=myfont, bg="spring green",
command=t4).place(x=200, y=80)
Button(oyna, text="5", width=4, font=myfont, bg="spring green",
command=t5).place(x=20, y=130)
Button(oyna, text="6", width=4, font=myfont, bg="spring green",
command=t6).place(x=80, y=130)
Button(oyna, text="7", width=4, font=myfont, bg="spring green",
command=t7).place(x=140, y=130)
Button(oyna, text="8", width=4, font=myfont, bg="spring green",
command=t8).place(x=200, y=130)
Button(oyna, text="9", width=4, font=myfont, bg="spring green",
command=t9).place(x=20, y=180)
Button(oyna, text="0", width=4, font=myfont, bg="spring green",
command=t0).place(x=80, y=180)
Button(oyna, text="+", width=4, font=myfont, bg="orange",
command=tp).place(x=140, y=180)
Button(oyna, text="-", width=4, font=myfont, bg="orange",
command=tm).place(x=200, y=180)
Button(oyna, text="*", width=4, font=myfont, bg="orange",
command=tk).place(x=20, y=230)
Button(oyna, text="/", width=4, font=myfont, bg="orange",
command=tb).place(x=80, y=230)
Button(oyna, text="C", width=4, font=myfont, bg="coral",
command=tc).place(x=140, y=230)
Button(oyna, text="=", width=4, font=myfont, bg="coral",
command=nat).place(x=200, y=230)
oyna.mainloop()