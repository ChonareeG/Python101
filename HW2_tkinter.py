from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #mainscreen
GUI.title('โปรแกรมทายนิสัยจากสถานที่เที่ยว') #programname
GUI.geometry('500x400') #size

L1 = Label(GUI,text='สถานที่เที่ยวที่ชอบ',font=('Angsana New',30),fg='white')
L1.place(x=100,y=50)
######################
def Button2():
    text = 'รักอิสระ ขี้เหงา ตรงไปตรงมา'
    messagebox.showinfo('ทะเล',text)

FB1 = Frame(GUI) #board
FB1.place(x=150,y=100)
B2 = ttk.Button(FB1,text='ทะเล',command=Button2)
B2.pack(ipadx=10,ipady=10)
######################
def Button3():
    text = 'อดทน อ่อนโยน มีจิตใจอ่อนไหว'
    messagebox.showinfo('ภูเขา',text)

FB2 = Frame(GUI) #board
FB2.place(x=150,y=180)
B3 = ttk.Button(FB1,text='ภูเขา',command=Button3)
B3.pack(ipadx=10,ipady=10)
######################
def Button4():
    text = 'สายบุญ ชอบความสงบ ปนขอเลขเด็ด'
    messagebox.showinfo('วัด',text)

FB3 = Frame(GUI) #board
FB3.place(x=150,y=240)
B4 = ttk.Button(FB1,text='วัด',command=Button4)
B4.pack(ipadx=10,ipady=10)

GUI.mainloop()
