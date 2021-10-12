from tkinter import*
def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else: 
             value = eval(screen.get()) 

        scvalue.set(value)
        screen.update  
   

    elif text == "C":  
        scvalue.set("") 
        screen.cut()  
    else:
        scvalue.set(scvalue.get() + text)     
window = Tk()
window.geometry("600x500")
window.title("HIMANI CALCULATER")
sachin = Label(text="Himani's calculater")


scvalue = StringVar()
scvalue.set("")
screen = Entry(window,textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X,ipadx=9,pady=10,padx=10)
f = Frame(window,bg="black")


b = Button(f,text="C",font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)

f = Frame(window,bg="black")
b = Button(f,text="9",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="8",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="7",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="-",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
f.pack()


f = Frame(window,bg="black")
b = Button(f,text="4",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="5",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="6",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="*",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
f.pack()


f = Frame(window,bg="black")
b = Button(f,text="1",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="2",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="3",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="/",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
f.pack()


f = Frame(window,bg="black")
b = Button(f,text="C",font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="0",font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="=",font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
b = Button(f,text="+",font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=15)
b.bind("<Button-1>",click)
f.pack()


#width,height
window.minsize(400,200)
#width,height
window.maxsize(1000,800)
sachin = Label(text="Welcome to Himani's calculater")
sachin.pack()
window.mainloop()