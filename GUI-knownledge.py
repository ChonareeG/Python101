from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #mainscreen
GUI.title('โปรแกรมบันทึกข้อมูล') #programname
GUI.geometry('500x400') #size

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='white')
L1.place(x=30,y=20)
######################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #board
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่เท่าไหร่',command=Button2)
B2.pack(ipadx=20,ipady=20)
######################
def Button3():
    text = 'Python101, Math'
    messagebox.showinfo('วิชาที่เรียน 10-20 FEB',text)

FB2 = Frame(GUI) #board
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์่นี้เรียนอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
