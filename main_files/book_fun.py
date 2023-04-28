
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="root",database="lib")
cur=con.cursor()
from tkinter import *
def bk_add():
    def back():
        root.destroy()
    def val():
        s.set(1)
    def badd():
            st=s.get()
            i=int(a.get())
            n=b.get()
            cl=c.get()
            ty=t.get()
            pr=int(p.get())
            cur.execute(f"insert into books2 values({i},'{n}','{cl}','{ty}',{pr},{st});")
            con.commit()
            root.destroy()
    s=IntVar()
    s.set(0)
    root=Tk()
    root.title("libary program")
    root.geometry("400x450")
    y=LabelFrame(root, text="enter details")
    y.pack(fill="both", expand="yes")
    txt=Label(y, text="book id")
    txt.pack()
    a=Entry(y, width=10)
    a.pack()
    txt1=Label(y, text="book name")
    txt1.pack()
    b=Entry(y, width=10)
    b.pack()
    txt2=Label(y, text="author")
    txt2.pack()
    c=Entry(y, width=10)
    c.pack()
    txt3=Label(y, text="Type")
    txt3.pack()
    t=Entry(y, width=10)
    t.pack()
    txt4=Label(y, text="Price")
    txt4.pack()
    p=Entry(y, width=10)
    p.pack()
    R1 = Radiobutton(y, text="CHECKED IN", variable=s, value=0,)
    R1.pack(anchor = W)
    R2 = Radiobutton(y, text="CHECKED OUT", variable=s, value=1,command=val)
    R2.pack(anchor = W)
    d=Button(y, text="done",height=1,width=3,command=badd)
    d.pack()
    e=Button(y, text="back",height=1,width=3,command=back)
    e.pack()
    root.mainloop()
def bdel():
    def back():
        root.destroy()
    def clk():
        idel=int(y.get())
        cur.execute("delete from books2 where bid={};".format(idel))
        con.commit()
        root.destroy()
    root=Tk()
    root.title("libary program")
    root.geometry("200x200")
    x=LabelFrame(root,text="Enter Id To Be Deleted")
    x.pack(fill="both", expand="yes")
    y=Entry(x, width=10)
    y.pack()
    d=Button(x, text="done",height=1,width=3,command=clk)
    d.pack()
    e=Button(x, text="back",height=1,width=3,command=back)
    e.pack()
    root.mainloop()
def book_dis():
    disp=''
    cur.execute("select * from books2;")
    disp=cur.fetchall()
    def back1():
        root.destroy()
    root=Tk()
    root.geometry("300x300")
    root.title("libary program")
    x=LabelFrame(root, text="Display")
    x.pack(fill="both", expand="yes")
    txt=Label(x, text=disp)
    txt.pack(anchor=CENTER)
    btn=Button(x,height=3,width=7,text="back",command=back1)
    btn.pack(anchor=S)
    root.mainloop()
    
def se(z):
    disp=''
    def back2():
        root.destroy()
    def clk2():
        idel=y.get()
        if z == 1:
            ye="bid"
        elif z == 2:
            ye="bname"
        elif z == 3:
            ye="author"
        else:
            ye="type"
        cur.execute(f"select * from books2 where {ye}={idel};")
        disp=cur.fetchall()
        root=Tk()
        root.geometry("300x300")
        root.title("libary program")
        x=LabelFrame(root, text="Display")
        x.pack(fill="both", expand="yes")
        txt=Label(x, text=disp)
        txt.pack(anchor=CENTER)
        btn=Button(x,height=3,width=7,text="back",command=root.destroy)
        btn.pack(anchor=S)
        root.mainloop()
    root=Tk()
    root.title("libary program")
    root.geometry("200x200")
    x=LabelFrame(root,text="Enter The value")
    x.pack(fill="both", expand="yes")
    y=Entry(x, width=10)
    y.pack()
    txt=Label(x,text=disp).pack()
    d=Button(x, text="done",height=1,width=3,command=clk2)
    d.pack()
    e=Button(x, text="back",height=1,width=3,command=back2)
    e.pack()
    root.mainloop()
def issue():
    def chkstd():
        st=y.get()
        root1.destroy()
        cur.execute(f"select sid from student where sid ={st};")
        dis=cur.fetchall()
        if dis is not None:
            def chkbk():
                bt=y1.get()
                cur.execute(f"select status from books2 where bid={bt};")
                dis2=cur.fetchall()
                for i in dis2:
                    for x in i:
                        if x == 0:
                            cur.execute(f"update books2 set status = 1 where bid = {st};")
                            con.commit()
                            rt=Tk()
                            rt.title("done")
                            rt.geometry('100x100')
                            txt1=Label(rt, text="book taken out").pack()
                            btn=Button(rt, text="back",height=2,width=3,command=rt.destroy).pack()
                            rt.mainloop()
        
                    
            root=Tk()
            root.title("libary program")
            root.geometry("200x200")
            x=LabelFrame(root,text="Enter The Book ID")
            x.pack(fill="both", expand="yes")
            y1=Entry(x, width=10)
            y1.pack()
            d=Button(x, text="done",height=1,width=3,command=chkbk)
            d.pack()
            e=Button(x, text="back",height=1,width=3,command=root.destroy)
            e.pack()
            root.mainloop()
        

    root1=Tk()
    root1.title("libary program")
    root1.geometry("200x200")
    x=LabelFrame(root1,text="Enter The Student ID")
    x.pack(fill="both", expand="yes")
    y=Entry(x, width=10)
    y.pack()
    d=Button(x, text="done",height=1,width=3,command=chkstd)
    d.pack()
    e=Button(x, text="back",height=1,width=3,command=root1.destroy)
    e.pack()
    root1.mainloop()

def return1():
    def chkstd1():
        st=y.get()
        root1.destroy()
        cur.execute(f"select sid from student where sid ={st};")
        dis=cur.fetchall()
        if dis is not None:
            def chkbk1():
                bt=y1.get()
                cur.execute(f"select status from books2 where bid={bt};")
                dis2=cur.fetchall()
                for i in dis2:
                    for x in i:
                        if x == 1:
                            root.destroy()
                            cur.execute(f"update books2 set status = 0 where bid = {st};")
                            con.commit()
                            rt=Tk()
                            rt.title("done")
                            rt.geometry('100x100')
                            txt1=Label(rt, text="book returned").pack()
                            btn=Button(rt, text="back",height=2,width=3,command=rt.destroy).pack()
                            rt.mainloop()
        
                    
        root=Tk()
        root.title("libary program")
        root.geometry("200x200")
        x=LabelFrame(root,text="Enter The Book ID")
        x.pack(fill="both", expand="yes")
        y1=Entry(x, width=10)
        y1.pack()
        d=Button(x, text="done",height=1,width=3,command=chkbk1)
        d.pack()
        e=Button(x, text="back",height=1,width=3,command=root.destroy)
        e.pack()
        root.mainloop()
        

    root1=Tk()
    root1.title("libary program")
    root1.geometry("200x200")
    x=LabelFrame(root1,text="Enter The Student ID")
    x.pack(fill="both", expand="yes")
    y=Entry(x, width=10)
    y.pack()
    d=Button(x, text="done",height=1,width=3,command=chkstd1)
    d.pack()
    e=Button(x, text="back",height=1,width=3,command=root1.destroy)
    e.pack()
    root1.mainloop()

    
