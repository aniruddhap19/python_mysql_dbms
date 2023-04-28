from tkinter import *
def ad1():
    i=0
    n=''
    cl=''
    bo=False
    def back()
        root.destroy()
    def ad():
        global i,n,cl,bo
        i=int(a.get())
        n=b.get()
        cl=c.get()
        bo=True
        root.destroy()
    root=Tk()
    root.title("libary program")
    root.geometry("200x200")
    y=LabelFrame(root, text="enter details")
    y.pack(fill="both", expand="yes")
    txt=Label(y, text="student id")
    txt.pack()
    a=Entry(y, width=10)
    a.pack()
    txt1=Label(y, text="student name")
    txt1.pack()
    b=Entry(y, width=10)
    b.pack()
    txt2=Label(y, text="class")
    txt2.pack()
    c=Entry(y, width=10)
    c.pack()
    d=Button(y, text="done",height=1,width=3,command=ad)
    d.pack()
    e=Button(y, text="back",height=1,width=3,command=back)
    e.pack()
    root.mainloop()
