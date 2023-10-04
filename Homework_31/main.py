from tkinter import *
root = Tk()
root.title('tk')

c = Canvas(width=200, height=200, bg='white')
c.pack()

c.create_rectangle(60, 80, 140, 160, fill='lightblue', outline='lightblue')
c.create_polygon(100, 30, 40, 90, 160, 90, fill='lightblue', outline='lightblue')
c.create_oval(200, 5, 150, 55, fill='orange', outline='orange')
i = 0
while (i<500):
    c.create_arc((i, 140), (i+60, 220),
                 start=-160, extent=-70,
                 style=ARC, outline='green',
                 width=2)
    i += 10

root.mainloop()