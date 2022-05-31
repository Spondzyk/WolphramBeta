import tkinter.messagebox
from tkinter import *

from PIL import ImageTk, Image
from customtkinter import *

from Gui.DifferentiationGui import DifferentiationGui
from Gui.DualIntegralGui import DualIntegralGui
from Gui.DualMatrixGui import DualMatrixGui
from Gui.IntegralGui import IntegralGui
from Gui.LimitsGui import LimitsGui
from Gui.LogarythmicScaleGui import LogarythmicScaleGui
from Gui.MultiplePlotGui import MultiplePlotGui
from Gui.OneVariableFunctionGui import OneVariableFunctionGui
from Gui.SingleMatrixGui import SingleMatrixGui
from Gui.TwoVariableFunctionGui import TwoVariableFunctionGui


class MenuGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.parent = master
        self.create_work_place()
        master.protocol("WM_DELETE_WINDOW", self.file_quit)
        self.parent.geometry("900x450")
        self.parent.resizable(False, False)

        self.parent.columnconfigure(0, weight=2)
        self.parent.columnconfigure(1, weight=1)
        self.parent.rowconfigure(0, weight=9999)
        self.parent.rowconfigure(1, weight=1)

    def file_quit(self):
        reply = tkinter.messagebox.askyesno("End", "Do you want to quit", parent=self.parent)
        if reply:
            self.parent.destroy()

    def create_work_place(self):
        self.frame = CTkFrame(self.parent, width=1700, height=1500, bg_color='white', fg_color='white',
                              border_color='white')

        upper_frame = CTkFrame(self.frame)

        pause_frame1_ = CTkFrame(self.frame, height=30, width=1700, bg_color='white', fg_color='white',
                                 border_color='white')
        pause_frame1_.pack()

        iconPath = "images/menu_image.jpg"
        icon = ImageTk.PhotoImage(Image.open(iconPath))
        icon_size = CTkLabel(upper_frame, bg_color='white', fg_color='white')
        icon_size.image = icon
        icon_size.configure(image=icon)
        icon_size.pack()

        upper_frame.pack()

        pause_frame2_ = CTkFrame(self.frame, height=30, width=1700, bg_color='white', fg_color='white',
                                 border_color='white')
        pause_frame2_.pack()

        middle_frame = CTkFrame(self.frame, height=500, width=1700, bg_color='white', fg_color='white',
                                border_color='white')

        pause_label = CTkLabel(middle_frame, height=20, bg_color='white', fg_color='white', text_color='white')
        pause_label_buttons_1 = CTkLabel(middle_frame, width=1, bg_color='white', fg_color='white', text_color='white')
        pause_label_buttons_2 = CTkLabel(middle_frame, width=1, bg_color='white', fg_color='white', text_color='white')

        # Plotting part
        plotting_label = CTkLabel(middle_frame, text="Plotting", width=30, text_font=("Arial Bold", 12))
        plotting_label.grid(column=0, row=0)

        pause_label.grid(column=0, row=1)

        one_var_button = CTkButton(middle_frame, text="One variable function plot", width=200, height=25,
                                   text_font=("Arial Bold", 10), command=self.plot_one_variable)
        one_var_button.grid(column=0, row=2)

        log_scale_button = CTkButton(middle_frame, text="Plot on a logarithmic scale", width=200, height=25,
                                     text_font=("Arial Bold", 10), command=self.plot_logarithmic_scale)
        log_scale_button.grid(column=0, row=3)

        few_function_button = CTkButton(middle_frame, text="Few plots on one picture", width=200, height=25,
                                        text_font=("Arial Bold", 10), command=self.plot_few_function)
        few_function_button.grid(column=0, row=4)

        two_variables_button = CTkButton(middle_frame, text="Two variable function plot", width=200, height=25,
                                         text_font=("Arial Bold", 10), command=self.plot_two_variables)
        two_variables_button.grid(column=0, row=5)

        pause_label_buttons_1.grid(column=1)

        # Matrix part
        matrix_label = CTkLabel(middle_frame, text="Matrix", width=30, text_font=("Arial Bold", 12))
        matrix_label.grid(column=2, row=0)
        middle_frame.pack()

        pause_label.grid(column=2, row=1)

        single_matrix_button = CTkButton(middle_frame, text="Operation - single matrix", width=200, height=25,
                                         text_font=("Arial Bold", 10), command=self.operation_on_single_matrix)
        single_matrix_button.grid(column=2, row=2)

        two_matrix_button = CTkButton(middle_frame, text="Operation - two matrix", width=200, height=25,
                                      text_font=("Arial Bold", 10), command=self.operation_on_two_matrix)
        two_matrix_button.grid(column=2, row=3)

        pause_label_buttons_2.grid(column=3)

        # Operation part
        operation_label = CTkLabel(middle_frame, text="Math operations", width=30, text_font=("Arial Bold", 12))
        operation_label.grid(column=4, row=0)

        pause_label.grid(column=4, row=1)

        integral_button = CTkButton(middle_frame, text="Integral", width=200, height=25,
                                    text_font=("Arial Bold", 10), command=self.integral)
        integral_button.grid(column=4, row=2)

        dual_integral_button = CTkButton(middle_frame, text="Dual integral", width=200, height=25,
                                         text_font=("Arial Bold", 10), command=self.dual_integral)
        dual_integral_button.grid(column=4, row=3)

        different_button = CTkButton(middle_frame, text="Different", width=200, height=25,
                                     text_font=("Arial Bold", 10), command=self.different)
        different_button.grid(column=4, row=4)

        limits_button = CTkButton(middle_frame, text="Limits", width=200, height=20,
                                  text_font=("Arial Bold", 10), command=self.limit)
        limits_button.grid(column=4, row=5)

        middle_frame.pack()

        bottom_frame = CTkFrame(self.frame, height=100, width=1700, bg_color='white', fg_color='white',
                                border_color='white')
        bottom_frame.pack()

        self.frame.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

    def plot_one_variable(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Wykres jednej zmiennej')
        w = 600
        h = 800

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 1.75) - (w / 1.75)
        y = (hs / 10) - (h / 9)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        OneVariableFunctionGui(newWindow)

    def plot_logarithmic_scale(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Wykres na skali logarytmicznej')
        w = 600
        h = 800

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 1.75) - (w / 1.75)
        y = (hs / 10) - (h / 9)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        LogarythmicScaleGui(newWindow)

    def plot_few_function(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Kilka funkcji na jednym wykresie')
        w = 600
        h = 730

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 1.75) - (w / 1.75)
        y = (hs / 10) - (h / 9)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        MultiplePlotGui(newWindow)

    def plot_two_variables(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Wykres dwóch zmiennych')
        w = 600
        h = 800

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 1.75) - (w / 1.75)
        y = (hs / 10) - (h / 9)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        TwoVariableFunctionGui(newWindow)

    def operation_on_single_matrix(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Operacje na pojedyńczej macierzy')
        w = 1100
        h = 600

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        SingleMatrixGui(newWindow)

    def operation_on_two_matrix(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Operacje na macierzach')
        w = 1200
        h = 770

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        DualMatrixGui(newWindow)

    def integral(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Całkowanie')
        w = 800
        h = 410

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        IntegralGui(newWindow)

    def different(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Różniczkowanie')
        w = 800
        h = 315

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        DifferentiationGui(newWindow)

    def limit(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Granice')
        w = 800
        h = 350

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        LimitsGui(newWindow)

    def dual_integral(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Całki podwójne')
        w = 700
        h = 410

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        DualIntegralGui(newWindow)


if __name__ == '__main__':
    master = Tk()
    master.title("Menu główne")
    app = MenuGui(master)
    app.mainloop()
