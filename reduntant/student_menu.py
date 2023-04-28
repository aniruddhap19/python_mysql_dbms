import main
import student_display 
from tkinter import *
def stud_menu():
    def back():
        root.destroy()
        main.tlayer()
    def display():
        student_display.stud_dis()
    def std_add():
        student_display.ad1()
    def std_delete():
        student_display.sdel()
        
    root=Tk()
    root.title("libary program")
    root.geometry("300x300")
    x=LabelFrame(root,text="student menu")
    x.pack(fill="both", expand="yes")
    abtn=Button(x, text="1.Add Details",height=3,width=7,command=std_add)
    abtn.pack()
    dbtn=Button(x, text="2.Display",height=3,width=7,command=display)
    dbtn.pack()
    debtn=Button(x, text="3.Delete",height=3,width=7,command=std_delete)
    debtn.pack()
    sbtn=Button(x, text="4.Search",height=3,width=7)
    sbtn.pack()
    bbtn=Button(x, text="5.Back",height=3,width=7,command=back)
    bbtn.pack()
    root.mainloop()
