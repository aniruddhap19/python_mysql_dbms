import student_display
import book_fun
from tkinter import *    
def tlayer():
    def stm():
        root.destroy()
        stud_menu()
    def btm():
        root.destroy()
        book_menu()
    def ex():
        root.destroy()
    root=Tk()
    root.title("libary program")
    root.geometry("200x200")
    x=LabelFrame(root, text="main menu")
    x.pack(fill="both", expand="yes")
    sbtn=Button(x, text="1. student",height=3,width=10,command=stm)
    sbtn.pack()
    bbtin=Button(x,text="2. book",height=3,width=10,command=btm)
    bbtin.pack()
    xit=Button(x,text="3. Exit",height=3,width=10,command=ex)
    xit.pack()                
    root.mainloop()
def stud_menu():
    def back():
        root.destroy()
        tlayer()
    root=Tk()
    root.title("libary program")
    root.geometry("300x300")
    x=LabelFrame(root,text="student menu")
    x.pack(fill="both", expand="yes")
    abtn=Button(x, text="1.Add Details",height=3,width=7,command=student_display.ad1)
    abtn.pack()
    dbtn=Button(x, text="2.Display",height=3,width=7,command=student_display.stud_dis)
    dbtn.pack()
    debtn=Button(x, text="3.Delete",height=3,width=7,command=student_display.sdel)
    debtn.pack()
    sbtn=Button(x, text="4.Search",height=3,width=7,command=student_display.ssea)
    sbtn.pack()
    bbtn=Button(x, text="5.Back",height=3,width=7,command=back)
    bbtn.pack()
    root.mainloop()
def book_menu():
    def backb():
        root.destroy()
        tlayer()
    root=Tk()
    root.title("libary program")
    root.geometry("400x400")
    x=LabelFrame(root,text="book menu")
    x.pack(fill="both", expand="yes")
    abtn=Button(x, text="1.Add Details",height=3,width=10,command=book_fun.bk_add)
    abtn.pack()
    dbtn=Button(x, text="2.Display",height=3,width=10,command=book_fun.book_dis)
    dbtn.pack()
    debtn=Button(x, text="3.Delete",height=3,width=10,command=book_fun.bdel)
    debtn.pack()
    sbtn=Button(x, text="4.Search",height=3,width=10,command=book_menu2)
    sbtn.pack()
    bbtn=Button(x, text="5.Book Issue",height=3,width=10,command=book_fun.issue)
    bbtn.pack()
    brbtn=Button(x, text="5.Book Return",height=3,width=10,command=book_fun.return1)
    brbtn.pack()
    babtn=Button(x, text="5.Back",height=3,width=10,command=backb)
    babtn.pack()
    root.mainloop()

z=0
def book_menu2():
    def b_id():
        global z
        z=1
        book_fun.se(z)
    def b_n():
        global z
        z=2
        book_fun.se(z)
    def b_a():
        global z
        z=3
        book_fun.se(z)
    def b_t():
        global z
        z=4
        book_fun.se(z)
    def back2():
        root.destroy()
    root=Tk()
    root.title("libary program")
    root.geometry("300x300")
    x=LabelFrame(root,text="book search menu")
    x.pack(fill="both", expand="yes")
    abtn=Button(x, text="1.By ID",height=3,width=7,command=b_id)
    abtn.pack()
    dbtn=Button(x, text="2.By Name",height=3,width=7,command=b_n)
    dbtn.pack()
    debtn=Button(x, text="3.Author",height=3,width=7,command=b_a)
    debtn.pack()
    sbtn=Button(x, text="4.type",height=3,width=7,command=b_t)
    sbtn.pack()
    bbtn=Button(x, text="5.Back",height=3,width=7,command=back2)
    bbtn.pack()
    root.mainloop()
    

if __name__=="__main__":   
    tlayer()
