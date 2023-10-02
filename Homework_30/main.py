from tkinter import *
root = Tk()
root.title('Project')

lstElements = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

lbox1 = Listbox(selectmode=EXTENDED, width=25, height=15)
lbox2 = Listbox(selectmode=EXTENDED, width=25, height=15)

for i in lstElements:
    lbox1.insert(END, i)


def right():
    select = list(lbox1.curselection())
    for i in select:
        lbox2.insert(END, lbox1.get(i))
    select.reverse()
    for i in select:
        lbox1.delete(i)

def left():
    select = list(lbox2.curselection())
    for i in select:
        lbox1.insert(END, lbox2.get(i))
    select.reverse()
    for i in select:
        lbox2.delete(i)

lbox1.pack(side=LEFT)
f = Frame()
f.pack(side=LEFT)
Button(f, text='>>>', command=right).pack()
Button(f, text='<<<', command=left).pack()
lbox2.pack(side=RIGHT)

root.mainloop()