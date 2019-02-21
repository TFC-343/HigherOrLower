from tkinter import *
import random




global y
y = random.randint(0,100)

global lb1
global root




def pressed():
    global z
    x = ent1.get()
    x = int(x)
    if z <= 1:
        ent1.destroy()
        lb2.destroy()
        lb1.config(text = "you lose",bg = "#ff0000")
        root.configure(background="#ff0000")
        btn1.config(text = "Quit",command = quit,bg = "#ff0000",fg = "#000000")


    
    elif x < y:
        lb1.config(text = "higher")
        z = z - 1
        lb2.config(text = "you have "+str(z)+" gueses left")
        ent1.delete(0, END)
    elif x > y:
        lb1.config(text = "lower")
        z = z - 1
        lb2.config(text = "you have "+str(z)+" gueses left")
        ent1.delete(0, END)
    else:
        ent1.destroy()
        lb2.destroy()
        lb1.config(text = "you win!!!",bg = "#00ff00")
        root.configure(background="#00ff00")
        btn1.config(text = "Quit",command = quit,bg = "#00ff00")

    #ent1.delete(0, END)






global z


z = 10

root = Tk()

root.configure(background="#00ffff")
root.geometry()

lb2 = Label(root,text = "you have "+str(z)+" gueses left",bg = "#00ffff")
lb2.pack()


ent1 = Entry(root)
ent1.pack(pady = 20, padx = 10)


lb1 = Label(root,text = "please enter your guess\nbetween 1 and 100",bg = "#00ffff")
lb1.pack()


btn1 = Button(root, text = "Submit",command = pressed,bg = "#0000ff",fg = "White")
btn1.pack(pady = 10)

mainloop()
