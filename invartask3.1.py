import math
import tkinter.messagebox

from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        vcmd = (frame.register(self.validate), '%P', '%S')

        a_area = Listbox(frame)
        a_label = Label(a_area, text='a = ')
        self.a_value = Entry(a_area, validate='key', vcmd=vcmd)

        b_area = Listbox(frame)
        b_label = Label(b_area, text='b = ')
        self.b_value = Entry(b_area, validate='key', vcmd=vcmd)

        c_area = Listbox(frame)
        c_label = Label(c_area, text='c = ')
        self.c_value = Entry(c_area, validate='key', vcmd=vcmd)

        solve_button = Button(frame, text='Решить', command=self.solve)

        a_area.pack()
        a_label.pack(side=LEFT)
        self.a_value.pack(side=TOP, expand=True)
        b_area.pack()
        b_label.pack(side=LEFT)
        self.b_value.pack(side=TOP, expand=True)
        c_area.pack()
        c_label.pack(side=LEFT)
        self.c_value.pack(side=TOP, expand=True)
        solve_button.pack(expand=True)

    def validate(self, P, S):
        allowed = ['.', '-']
        cond_1 = S.isdigit() or S in allowed
        cond_2 = P.count('.') in range(2)
        cond_3 = P.count('-') in range(2) and '-' not in P[1:]
        return cond_1 and cond_2 and cond_3

    
    def solve(self):
        a = float(self.a_value.get() or 0)
        b = float(self.b_value.get() or 0)
        c = float(self.c_value.get() or 0)
        D = b ** 2 - 4 * a * c

        try:
            x1 = (-b - math.sqrt(D)) / (2 * a)
            x2 = (-b + math.sqrt(D)) / (2 * a)
        except ValueError:
            result = 'Корней нет'

        if D > 0:
            result = 'x1 = {}\nx2 = {}'.format(x1, x2)
        elif D == 0:
            result = 'x = {}'.format(x1)

        tkinter.messagebox.showinfo(title='Результат', message=result)

root = Tk()
root.title('quadratic equation solver')
root.resizable(0, 0)
app = App(root)
root.mainloop()

