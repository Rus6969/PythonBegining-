from tkinter import*

window = Tk()
def kg_toPounds():
    poundsResult = int(e1valaue1.get())*2.2

    t1.insert(END,poundsResult)




b1 = Button(window,text="Calculate",command=kg_toPounds)
b1.grid(row=0,column=0)




e1valaue1 = StringVar()
e1=Entry(window,textvariable=e1valaue1)
e1.grid(row=0,column=1)
t1 = Text(window,height=1,width=10)
t1.grid(row=0,column=2)



window.mainloop()