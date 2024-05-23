from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.title("CALCULATOR!!")
root.configure(bg="#0F0F0F")
root.geometry("430x650")
#root.resizable(False,False)

def click(event):
    txt=event.widget.cget("text")
    if txt=="=":
        try:
            if a.get().isdigit():
                val=int(a.get())
            else:
                val=eval(a.get())

            a.set(val)
        except SyntaxError:
            showerror("ERROR","You have used mulpile operators(signs)")
        except ZeroDivisionError:
            showwarning("WARNING!","ANY NUMBER CANNOT DIVISIBLE BY 0")

    elif txt=="AC":
        a.set("")
        e1.update()
    elif txt=="<-":
        de=a.get()
        if de:
            newtxt=de[:-1]
            e1.delete(0,END)
            e1.insert(0,newtxt)
        
    else:
        if txt=="x":
            txt="*"
        elif txt=="÷":
            txt="/"
        else:
            pass
        a.set(a.get()+txt)
        e1.update()

a=StringVar()
e1=Entry(root,font="Georgia 30 bold",justify="right",textvariable=a)
e1.pack(fill=X,side=TOP,padx=10,pady=10)

frm1=Frame(root,bg="#0F0F0F")
frm1.pack(padx=15,pady=15,anchor=E)
b=Button(frm1,text="AC",bg="#31363F",fg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=RIGHT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm1,text="<-",bg="#31363F",fg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

frm2=Frame(root,bg="#0F0F0F")
frm2.pack(padx=15,pady=15)
b=Button(frm2,text="7",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm2,text="8",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm2,text="9",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm2,text="-",bg="#61677A",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

frm3=Frame(root,bg="#0F0F0F")
frm3.pack(padx=15,pady=15)
b=Button(frm3,text="4",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm3,text="5",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm3,text="6",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm3,text="+",bg="#61677A",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

frm4=Frame(root,bg="#0F0F0F")
frm4.pack(padx=15,pady=15)
b=Button(frm4,text="1",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm4,text="2",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm4,text="3",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm4,text="x",bg="#61677A",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

frm5=Frame(root,bg="#0F0F0F")
frm5.pack(padx=15,pady=15)
b=Button(frm5,text="0",bg="#D8D9DA",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm5,text="=",bg="#FF6000",font="Georgia 25 bold",width=7)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b=Button(frm5,text="÷",bg="#61677A",font="Georgia 22 bold",width=3)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

root.mainloop()