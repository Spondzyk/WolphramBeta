import tkinter.messagebox
from tkinter import *

from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import Program_logic.ChartCreator


class OneVariableFunctionGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(600, 800))
        self.parent.resizable(False, False)
        self.formula = None
        self.if_grid = False
        # wykorzystanie wcześniej wykonanego backend'u
        self.chart = Program_logic.ChartCreator.ChartCreator()
        self.start_w = self.chart.start_w
        self.stop_w = self.chart.stop_w
        self.start_h = self.chart.start_h
        self.stop_h = self.chart.stop_h
        self.create()

    # funkcja tworzaca przestrzen pracy dla danego okna
    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=600, height=800, bg_color='white', fg_color='white',
                                    border_color='white')

        # frame z przerwa
        pause0_frame = CTkFrame(self.frame_entry, width=600, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause0_frame.pack()

        info_frame = CTkFrame(self.frame_entry, width=600, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        # frame z informacja wejsciowa
        intro = CTkLabel(info_frame, width=600, height=30, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
                Funkcja musi być funkcją zmiennej x''', fg_color='white')

        intro.pack()
        info_frame.pack()

        # frame z przerwa
        pause1_frame = CTkFrame(self.frame_entry, width=600, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()

        # frame z informajca odnoszaca sie do wprowadzanej funkcji
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

        # frame z przerwa
        pause2_frame = CTkFrame(self.frame_entry, width=600, height=10, bg_color='white', fg_color='white',
                                border_color='white')

        pause2_frame.pack()

        # frame z oknem do ktorego wprowadzamy funkcje
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

        # frame z przerwa
        pause3_frame = CTkFrame(self.frame_entry, width=600, height=10, bg_color='white', fg_color='white',
                                border_color='white')

        pause3_frame.pack()

        # frame z guzikiem ktory przetwarza wyrazenie i zwraca wynik
        bottom_frame = CTkFrame(self.frame_entry, width=600, height=50, bg_color='white', fg_color='white',
                                border_color='white')

        accept_button = CTkButton(bottom_frame, text='potwierdź', width=70, command=self.add_widget)
        accept_button.pack()
        bottom_frame.pack()

        # frame z przerwa
        pause5_frame = CTkFrame(self.frame_entry, width=600, height=10, bg_color='white', fg_color='white',
                                border_color='white')
        pause5_frame.pack()

        self.frame_entry.pack()

    # funkcja tworzaca przestrzen wynikowa
    def add_widget(self):
        flag = True
        # jesli zostala juz wczeniej utworzona (drugie i kolejne wywolania funkcji) kasujemy przestrzen wynikowa
        if self.frame_widget is not None:
            OneVariableFunctionGui.del_widget(self)

        # tworzenie frame wynikowego
        self.frame_widget = CTkFrame(self.frame_entry, width=600, height=600, bg_color='white',
                                     fg_color='white',
                                     border_color='white')
        # jesli nie ma formuly zwracamy komunikat
        if self.formula.get() == '':
            tkinter.messagebox.showinfo('Brak formuły', "Nie wprowadzono formuły funkcji")
            flag = False

        if flag:
            if self.frame_widget is not None:
                OneVariableFunctionGui.del_widget(self)

            self.frame_widget = CTkFrame(self.frame_entry, width=600, height=600, bg_color='white',
                                         fg_color='white',
                                         border_color='white')
            # wykorzystanie metody zwracajacej obraz funkcji jednej zmiennej
            fig = self.chart.plot_a_function_of_one_variable(self.formula.get(), self.start_w, self.stop_w,
                                                             self.if_grid)

            if self.chart.info == 'done':
                # przypisanie obrazu funkcji do kanwy
                canvas = FigureCanvasTkAgg(fig, master=self.frame_widget)
                canvas.draw()
                canvas.get_tk_widget().pack()

                # frame z guzikami sluzacymi do zmiany wymiarow osi x
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

                # frame z przerwa
                frame_pause = CTkFrame(bottom_frame, width=400, height=100, bg_color='white',
                                       fg_color='white',
                                       border_color='white')

                # frame z guzikiem ktorym mozemy wybierac czy chcemy aby wykres zawieral siatke
                frame_grid = CTkFrame(bottom_frame, width=100, height=100, bg_color='white',
                                      fg_color='white',
                                      border_color='white')
                grid = CTkButton(frame_grid, text="siatka", width=60, command=self.change_grid)
                grid.pack()

                frame_pause.grid(row=0, column=1)
                frame_grid.grid(row=0, column=2)
                bottom_frame.pack()
            # obsluga bledow i wyswietlanie komunikatow
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

    # metoda odpowiadajaca za dzialanie guzika + wzgledem osi x
    def plus_button(self):
        self.chart.change_size_w(True)
        self.start_w = self.chart.start_w
        self.stop_w = self.chart.stop_w
        self.start_h = self.chart.start_h
        self.stop_h = self.chart.stop_h
        self.add_widget()

    # metoda odpowiadajaca za dzialanie guzika - wzgledem osi x
    def minus_button(self):
        self.chart.change_size_w(False)
        self.start_w = self.chart.start_w
        self.stop_w = self.chart.stop_w
        self.start_h = self.chart.start_h
        self.stop_h = self.chart.stop_h
        self.add_widget()

    # funkcja odpowiedzialna za zmiane wykresu - dodanie/usuniecie siatki
    def change_grid(self):
        if self.if_grid:
            self.if_grid = False
        else:
            self.if_grid = True
        self.add_widget()

    # metoda odpowiedzialna za niszczenie obszaru wynikowego
    def del_widget(self):
        self.frame_widget.destroy()
