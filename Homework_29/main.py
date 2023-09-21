from tkinter import *

# #practice_1
# root = Tk()
# root.title('Welcome')
# colors = {
#     "red": "#ff0000",
#     "orange": "#ff7d00",
#     "yellow": "#ffff00",
#     "green": "#00ff00",
#     "lightblue": "#007dff",
#     "blue": "#0000ff",
#     "purple": "#7d00ff"
# }
# def insert_color(color_name):
#     color_code = colors[color_name]
#     e.delete(0, END)
#     e.insert(0, color_code)
#     l.config(text=color_name)
#
# l = Label(width=18)
# e = Entry(width=18)
# l.pack(pady=10)
# e.pack()
# class RBClr:
#     def __init__(self, color_name):
#         Button(frame, width=3,
#                bg=colors[color_name],
#                command=lambda i=color_name:insert_color(i)).pack(side=LEFT, pady=10, padx=1)
#
# frame = Frame(root)
# frame.pack(side=TOP)
# RBClr('red')
# RBClr('orange')
# RBClr('yellow')
# RBClr('green')
# RBClr('lightblue')
# RBClr('blue')
# RBClr('purple')
#root.mainloop()

# #practice_2
# root = Tk()
# root.title('Welcome')
#
# frame = Frame(root)
# frame.pack(side=LEFT)
#
# numbers = {
#     "Вася" : "+7 702 777 77 77",
#     "Петя" : "+7 702 888 88 88",
#     "Маша" : "+7 702 999 99 99"
# }
#
# def insert_number(name):
#     number_code = numbers[name]
#     e.delete(0, END)
#     e.insert(0, number_code)
#
# class PrintNumbers:
#     def __init__(self, name):
#         Radiobutton(frame, width=10, height=2, text=name, indicatoron=0,
#                command=lambda i=name:insert_number(i)).pack(side=TOP)
#
# e = Entry()
# e.pack(side=RIGHT, ipady=53)
#
# PrintNumbers('Вася')
# PrintNumbers('Петя')
# PrintNumbers('Маша')
#
# root.mainloop()