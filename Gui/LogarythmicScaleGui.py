import tkinter.messagebox
from tkinter import *

from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import Program_logic.ChartCreator


class LogarythmicScaleGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(600, 800))
        self.parent.resizable(False, False)
        self.formula = None
        self.if_grid = False
        self.chart = Program_logic.ChartCreator.ChartCreator()
        self.start_w = self.chart.start_w
        self.stop_w = self.chart.stop_w
        self.start_h = self.chart.start_h
        self.stop_h = self.chart.stop_h
        self.create()

    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=600, height=800, bg_color='white', fg_color='white',
                                    border_color='white')

        pause0_frame = CTkFrame(self.frame_entry, width=600, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause0_frame.pack()

        info_frame = CTkFrame(self.frame_entry, width=600, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        intro = CTkLabel(info_frame, width=600, height=30, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
                Funkcja musi być funkcją zmiennej x
                Będzie to funkcja na skali logarytmicznej''', fg_color='white')

        intro.pack()
        info_frame.pack()
        pause1_frame = CTkFrame(self.frame_entry, width=600, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()

        upper_frame = CTkFrame(self.frame_entry, width=600, height=30, bg_color='white', fg_color='white',
                               border_color='white')

        label_upper_left = CTkLabel(upper_frame, text_color='white', width=125, height=30, bg_color='white',
                                    fg_color='white')
        label_size = CTkLabel(upper_frame, text='Podaj funkcje f(x):', width=350, height=30,
                              bg_color='white', text_font=("Arial Bold", 13),
                              fg_color='white')
        label_upper_right = CTkLabel(upper_frame, text_color='white', width=125, height=30, bg_color='white',
                                     fg_color='white')
        label_upper_left.grid(row=0, column=0)
        label_size.grid(row=0, column=1)
        label_upper_right.grid(row=0, column=2)

        upper_frame.pack()

        pause2_frame = CTkFrame(self.frame_entry, width=600, height=10, bg_color='white', fg_color='white',
                                border_color='white')

        pause2_frame.pack()

        formula_frame = CTkFrame(self.frame_entry, width=600, height=50, bg_color='white', fg_color='white',
                                 border_color='white')

        left2_label = CTkLabel(formula_frame, text_color='white', width=125, height=50, bg_color='white',
                               fg_color='white')

        left2_label.grid(row=0, column=0)

        self.formula = CTkEntry(formula_frame, width=350, height=50)

        self.formula.grid(row=0, column=1)

        right2_label = CTkLabel(formula_frame, text_color='white', width=125, height=50, bg_color='white',
                                fg_color='white')

        right2_label.grid(row=0, column=2)

        formula_frame.pack()

        pause3_frame = CTkFrame(self.frame_entry, width=600, height=10, bg_color='white', fg_color='white',
                                border_color='white')

        pause3_frame.pack()

        bottom_frame = CTkFrame(self.frame_entry, width=600, height=50, bg_color='white', fg_color='white',
                                border_color='white')

        accept_button = CTkButton(bottom_frame, text='potwierdź', width=70, command=self.add_widget)
        accept_button.pack()
        bottom_frame.pack()

        pause5_frame = CTkFrame(self.frame_entry, width=600, height=10, bg_color='white', fg_color='white',
                                border_color='white')
        pause5_frame.pack()

        self.frame_entry.pack()

    def add_widget(self):
        flag = True
        if self.frame_widget is not None:
            LogarythmicScaleGui.del_widget(self)

        self.frame_widget = CTkFrame(self.frame_entry, width=600, height=600, bg_color='white',
                                     fg_color='white',
                                     border_color='white')
        if self.formula.get() == '':
            tkinter.messagebox.showinfo('Brak formuły', "Nie wprowadzono formuły funkcji")
            flag = False

        if flag:
            if self.frame_widget is not None:
                LogarythmicScaleGui.del_widget(self)

            self.frame_widget = CTkFrame(self.frame_entry, width=600, height=600, bg_color='white',
                                         fg_color='white',
                                         border_color='white')
            fig = self.chart.plot_a_function_on_a_logarithmic_scale(self.formula.get(), self.start_w, self.stop_w,
                                                                    self.if_grid)

            if self.chart.info == 'done':
                canvas = FigureCanvasTkAgg(fig, master=self.frame_widget)
                canvas.draw()
                canvas.get_tk_widget().pack()

                bottom_frame = CTkFrame(self.frame_widget, width=600, height=100, bg_color='white',
                                        fg_color='white',
                                        border_color='white')
                frame_buttons = CTkFrame(bottom_frame, width=100, height=100, bg_color='white',
                                         fg_color='white',
                                         border_color='white')

                plus_button = CTkButton(frame_buttons, text='+', width=40, command=self.plus_button)
                plus_button.grid(row=0, column=0)
                minus_button = CTkButton(frame_buttons, text='-', width=40, command=self.minus_button)
                minus_button.grid(row=0, column=1)

                frame_buttons.grid(row=0, column=0)

                frame_pause = CTkFrame(bottom_frame, width=400, height=100, bg_color='white',
                                       fg_color='white',
                                       border_color='white')

                frame_grid = CTkFrame(bottom_frame, width=100, height=100, bg_color='white',
                                      fg_color='white',
                                      border_color='white')
                grid = CTkButton(frame_grid, text="siatka", width=60, command=self.change_grid)
                grid.pack()

                frame_pause.grid(row=0, column=1)
                frame_grid.grid(row=0, column=2)
                bottom_frame.pack()
            else:
                if self.chart.info == 'syntax error':
                    tkinter.messagebox.showerror('Błąd formuły', '''Błąd formuły, wystąpił błąd składni formuły''')
                elif self.chart.info == 'name error':
                    tkinter.messagebox.showerror('Błąd formuły',
                                                 'Błąd formuły, funkcja musi być funkcją zależną od zmiennej x')
                elif self.chart.info == "zero division error":
                    tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpiła próba dzielenia przez 0")
                elif self.chart.info == "type error":
                    tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpił błąd typu")
                else:
                    tkinter.messagebox.showerror('Błąd formuły',
                                                 'Błąd formuły, wystąpił nieoczekiwany błąd, sprawdź poprawność zapisu albo spróbuj ponownie')

            self.frame_widget.pack()

    def plus_button(self):
        self.chart.change_size_w(True)
        self.start_w = self.chart.start_w
        self.stop_w = self.chart.stop_w
        self.start_h = self.chart.start_h
        self.stop_h = self.chart.stop_h
        self.add_widget()

    def minus_button(self):
        self.chart.change_size_w(False)
        self.start_w = self.chart.start_w
        self.stop_w = self.chart.stop_w
        self.start_h = self.chart.start_h
        self.stop_h = self.chart.stop_h
        self.add_widget()

    def change_grid(self):
        if self.if_grid:
            self.if_grid = False
        else:
            self.if_grid = True
        self.add_widget()

    def del_widget(self):
        self.frame_widget.destroy()


if __name__ == '__main__':
    master = Tk()
    s = LogarythmicScaleGui(master)
    s.mainloop()
