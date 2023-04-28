from tkinter import *
id_del=0
bo1=False
def back():
    root.destroy()
def clk():
    global id_del,bo1
    id_del=int(y.get())
    boi=True
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
