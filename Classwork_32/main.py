import math
import tkinter as tk
from tkinter import ttk

class Calc:
    def __init__(self, window):
        self.root = window
        self.root.title('Calculator')
        #----------------Entry-----------------#
        self.num_entry = ttk.Entry(self.root, width=20)
        self.num_entry.grid(row=0,column=0,columnspan=4)
        #----------------Default attributes-----------------#
        self.math = ''
        self.f_num = 0
        # ---------------Creat btn------------------#
        self.btn1 = ttk.Button(self.root, text='1', command=lambda: self.btn_click(1))
        self.btn2 = ttk.Button(self.root, text='2', command=lambda: self.btn_click(2))
        self.btn3 = ttk.Button(self.root, text='3', command=lambda: self.btn_click(3))
        self.btn4 = ttk.Button(self.root, text='4', command=lambda: self.btn_click(4))
        self.btn5 = ttk.Button(self.root, text='5', command=lambda: self.btn_click(5))
        self.btn6 = ttk.Button(self.root, text='6', command=lambda: self.btn_click(6))
        self.btn7 = ttk.Button(self.root, text='7', command=lambda: self.btn_click(7))
        self.btn8 = ttk.Button(self.root, text='8', command=lambda: self.btn_click(8))
        self.btn9 = ttk.Button(self.root, text='9', command=lambda: self.btn_click(9))
        self.btn0 = ttk.Button(self.root, text='0', command=lambda: self.btn_click(0))
        self.btn_cl = ttk.Button(self.root, text='C', command=lambda: self.btn_clear())
        self.btn_sum = ttk.Button(self.root, text='+', command=lambda: self.btn_add())
        self.btn_eq = ttk.Button(self.root, text='=', command=lambda: self.btn_equal())
        self.btn_min = ttk.Button(self.root, text='-', command=lambda: self.btn_minus())
        self.btn_mul = ttk.Button(self.root, text='*', command=lambda: self.btn_multiple())
        self.btn_div = ttk.Button(self.root, text='/', command=lambda: self.btn_division())
        self.btn_com = ttk.Button(self.root, text=',', command=lambda: self.btn_comma())
        self.btn_sq = ttk.Button(self.root, text='x²', command=lambda: self.btn_square())
        self.btn_sqRoot = ttk.Button(self.root, text='√', command=lambda: self.btn_squareRoot())
        self.btn_oneDiv = ttk.Button(self.root, text='1/x', command=lambda: self.btn_oneDivided())

        #----------------Grid-----------------#
        self.btn1.grid(row=4,column=0)
        self.btn2.grid(row=4,column=1)
        self.btn3.grid(row=4,column=2)
        self.btn4.grid(row=3,column=0)
        self.btn5.grid(row=3,column=1)
        self.btn6.grid(row=3,column=2)
        self.btn7.grid(row=2,column=0)
        self.btn8.grid(row=2,column=1)
        self.btn9.grid(row=2,column=2)
        self.btn0.grid(row=5,column=1)

        self.btn_oneDiv.grid(row=1,column=0)
        self.btn_sq.grid(row=1,column=1)
        self.btn_sqRoot.grid(row=1,column=2)
        self.btn_div.grid(row=1,column=3)
        self.btn_mul.grid(row=2,column=3)
        self.btn_min.grid(row=3,column=3)
        self.btn_sum.grid(row=4,column=3)
        self.btn_cl.grid(row=5,column=0)
        self.btn_com.grid(row=5,column=2)
        self.btn_eq.grid(row=5,column=3)

    # ---------------Методы------------------#
    def btn_click(self, num):
        current_num = self.num_entry.get()
        self.num_entry.delete(0, tk.END)
        self.num_entry.insert(0, str(current_num) + str(num))
    def btn_clear(self):
        self.num_entry.delete(0, tk.END)
    def btn_add(self):
        first_num = self.num_entry.get()
        self.math = "+"
        self.f_num = float(first_num)
        self.num_entry.delete(0, tk.END)
    def btn_minus(self):
        first_num = self.num_entry.get()
        self.math = "-"
        self.f_num = float(first_num)
        self.num_entry.delete(0, tk.END)
    def btn_multiple(self):
        first_num = self.num_entry.get()
        self.math = "*"
        self.f_num = float(first_num)
        self.num_entry.delete(0, tk.END)
    def btn_division(self):
        first_num = self.num_entry.get()
        self.math = "/"
        self.f_num = float(first_num)
        self.num_entry.delete(0, tk.END)
    def btn_comma(self):
        current_num = "."
        self.btn_click(current_num)
    def btn_square(self):
        first_num = self.num_entry.get()
        self.math = "*"
        self.f_num = float(first_num)
        self.num_entry.delete(0, tk.END)
        self.num_entry.insert(0, self.f_num * float(first_num))
    def btn_squareRoot(self):
        first_num = self.num_entry.get()
        self.num_entry.delete(0, tk.END)
        self.num_entry.insert(0, math.sqrt(float(first_num)))
    def btn_oneDivided(self):
        first_num = self.num_entry.get()
        self.num_entry.delete(0, tk.END)
        try:
            self.num_entry.insert(0, (1/float(first_num)))
        except ZeroDivisionError:
            self.btn_clear()
            current_num = "ZeroDivisionError"
            self.btn_click(current_num)
    def btn_equal(self):
        second_num = self.num_entry.get()
        self.num_entry.delete(0, tk.END)
        if self.math == '+':
            self.num_entry.insert(0, self.f_num + float(second_num))
        if self.math == '-':
            self.num_entry.insert(0, self.f_num - float(second_num))
        if self.math == '*':
            self.num_entry.insert(0, self.f_num * float(second_num))
        if self.math == '/':
            try:
                self.num_entry.insert(0, self.f_num / float(second_num))
            except ZeroDivisionError:
                self.btn_clear()
                current_num = "ZeroDivisionError"
                self.btn_click(current_num)

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calc(root)
    root.mainloop()