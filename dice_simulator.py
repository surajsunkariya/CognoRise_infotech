from tkinter import *
import random
from tkinter.messagebox import *

root=Tk()
root.geometry("520x365")
root.configure(bg="#543310")
root.title("Dice Roller")

def roll_dice():
    if a.get()=="":
        showerror(
            title="warning",message="Please enter the NUMBER of ROLLS!!"
        )
    else:
        lis=[]
        while True:
            dice_sides=6
            num_rolls=int(a.get())
            if num_rolls<=0:
                showerror(
                    title="warning",message="please enter valid number for the rolls!!"
                )
            else:
                for i in range(1, num_rolls + 1):
                    roll_result = random.randint(1, dice_sides)
                    lis.append(f"Roll {i}: {roll_result}")     
            break
        showinfo(
                title="Thanks for rolling!!",message=lis
            )
        more=askyesno(
            title="THANKS",message="Do you want to roll again?"
        )

        if more:
            a.set("")
        else:
            root.destroy()
    


frm=Frame(root,width=500,height=350,bg="#74512D")
frm.pack()

head=Label(frm,text="DICE ROLLER 🎲",height=2,bg="#74512D",font="arial 20 bold",fg="white")
head.place(x=120,y=5)

l1=Label(frm,text="Enter the number of rolls: ",font="Georgia 13 bold",bg="#74512D",fg="white")
l1.place(x=20,y=170)

a=StringVar()
e1=Entry(frm,textvariable=a,font="cambria 15 bold",width=14,bg="#AF8F6F",relief=RAISED)
e1.place(x=300,y=170)

but=Button(frm,text="ROLL THE DICE!!",font="Georgia 15 bold",bg="#543310",fg="white",command=roll_dice,borderwidth=5)
but.place(x=140,y=245)
root.mainloop()