import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import Program_logic.ChartCreator


class MultiplePlotGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(600, 730))
        self.parent.resizable(False, False)
        self.number_of_plots = None
        self.frame_formula = None
        self.formula_list = []
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

        # frame z informacja wejsciowa
        info_frame = CTkFrame(self.frame_entry, width=600, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        intro = CTkLabel(info_frame, width=600, height=30, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
                        Funkcja musi być funkcją zmiennej x''', fg_color='white')

        intro.pack()
        info_frame.pack()

        # frame z przerwa
        pause1_frame = CTkFrame(self.frame_entry, width=600, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()

        # frame z informajca odnoszaca sie do ilosci funkcji ktore program ma narysowac
        upper_frame = CTkFrame(self.frame_entry, width=600, height=30, bg_color='white', fg_color='white',
                               border_color='white')

        label_upper_left = CTkLabel(upper_frame, text_color='white', width=125, height=30, bg_color='white',
                                    fg_color='white')
        label_size = CTkLabel(upper_frame, text='Wybierz ilość wykresów które chcesz narysować:', width=350, height=30,
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

        # frame z comboboxem sluzacym do wybrania ilosci funkcji do narysowania
        combobox_frame = CTkFrame(self.frame_entry, width=600, height=50, bg_color='white', fg_color='white',
                                  border_color='white')

        left2_label = CTkLabel(combobox_frame, text_color='white', width=125, height=50, bg_color='white',
                               fg_color='white')

        left2_label.grid(row=0, column=0)

        selected_number = tkinter.StringVar()
        number_of_plots_cb = ttk.Combobox(combobox_frame, textvariable=selected_number)
        number_of_plots_cb['values'] = ('1', '2', '3', '4', '5')
        number_of_plots_cb['state'] = 'readonly'

        number_of_plots_cb.grid(row=0, column=1)

        right2_label = CTkLabel(combobox_frame, text_color='white', width=125, height=50, bg_color='white',
                                fg_color='white')

        right2_label.grid(row=0, column=2)

        combobox_frame.pack()

        # metoda odpowiedzialna za dzialanie comboboxa i reagujaca na zmiany
        def number_changed(event):
            self.number_of_plots = selected_number.get()
            self.window_for_formula()

        number_of_plots_cb.bind('<<ComboboxSelected>>', number_changed)

        pause3_frame = CTkFrame(self.frame_entry, width=600, height=10, bg_color='white', fg_color='white',
                                border_color='white')

        pause3_frame.pack()

        self.frame_entry.pack()

    # metoda odpowiedzialna za utworzenie okna z zawartoscia okien wejsciowych do ktorych mozna wpisac wybrana ilosc formul
    def window_for_formula(self):
        newWindow = Toplevel(self.parent)
        newWindow.title('Wprowadź formuły')
        w = 500
        h = int(self.number_of_plots) * 75 + 100

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 20) - (w / 10)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newWindow.resizable(False, False)

        if len(self.formula_list) > 0:
            self.formula_list.clear()

        self.frame_formula = CTkFrame(newWindow, width=500, height=h, bg_color='white smoke',
                                      fg_color='white smoke',
                                      border_color='white smoke')

        title_frame = CTkFrame(self.frame_formula, width=500, height=50, bg_color='white smoke',
                               fg_color='white smoke',
                               border_color='white smoke')

        pause1_label = CTkLabel(title_frame, width=500, height=10, bg_color='white smoke',
                                fg_color='white smoke', text_color='white smoke')
        pause1_label.pack()
        result_label = CTkLabel(title_frame, width=500, height=30, bg_color='white smoke',
                                fg_color='white smoke', text="Podaj funkcje f(x):")
        result_label.pack()
        pause2_label = CTkLabel(title_frame, width=500, height=10, bg_color='white smoke',
                                fg_color='white smoke', text_color='white smoke')
        pause2_label.pack()
        title_frame.pack()

        entry_frame = CTkFrame(self.frame_formula, width=500, height=h - 100, bg_color='white smoke',
                               fg_color='white smoke',
                               border_color='white smoke')

        for i in range(int(self.number_of_plots)):
            frame_single_entry = CTkFrame(entry_frame, width=500, height=(h - 100) / int(self.number_of_plots),
                                          bg_color='white smoke',
                                          fg_color='white smoke',
                                          border_color='white smoke')
            CTkLabel(frame_single_entry, width=75, height=50, bg_color='white smoke',
                     fg_color='white smoke', text='{}. '.format(i + 1)).grid(row=0, column=0)

            en = CTkEntry(frame_single_entry, width=350, height=50)
            en.grid(row=0, column=1)
            self.formula_list.append(en)
            frame_single_entry.pack()
            pause__frame = CTkFrame(entry_frame, width=500, height=10, bg_color='white smoke',
                                    fg_color='white smoke',
                                    border_color='white smoke')

            pause__frame.pack()

        entry_frame.pack()

        pause3_frame = CTkFrame(self.frame_formula, width=400, height=10, bg_color='white smoke',
                                fg_color='white smoke',
                                border_color='white smoke')

        pause3_frame.pack()

        bottom_frame = CTkFrame(self.frame_formula, width=400, height=50, bg_color='white smoke',
                                fg_color='white smoke',
                                border_color='white smoke')

        accept_button = CTkButton(bottom_frame, text='potwierdź', width=70, height=30, command=self.add_widget)
        accept_button.pack()
        bottom_frame.pack()

        pause5_frame = CTkFrame(self.frame_formula, width=400, height=100, bg_color='white smoke',
                                fg_color='white smoke',
                                border_color='white smoke')
        pause5_frame.pack()

        self.frame_formula.pack()

    # funkcja tworzaca przestrzen wynikowa
    def add_widget(self):
        flag = True
        # jesli zostala juz wczeniej utworzona (drugie i kolejne wywolania funkcji) kasujemy przestrzen wynikowa
        if self.frame_widget is not None:
            MultiplePlotGui.del_widget(self)

        # tworzenie frame wynikowego
        self.frame_widget = CTkFrame(self.frame_entry, width=600, height=600, bg_color='white',
                                     fg_color='white',
                                     border_color='white')

        # jesli nie ma jednej z formul zwracamy komunikat
        for i in range(len(self.formula_list)):
            if self.formula_list[i].get() == '':
                tkinter.messagebox.showinfo('Brak formuły',
                                            "Nie wprowadzono formuły funkcji dla numeru {}".format(i + 1))
                flag = False

        if flag:
            if self.frame_widget is not None:
                MultiplePlotGui.del_widget(self)

            self.frame_widget = CTkFrame(self.frame_entry, width=600, height=600, bg_color='white',
                                         fg_color='white',
                                         border_color='white')

            formula_list = []
            for elem in range(len(self.formula_list)):
                formula_list.append(self.formula_list[elem].get())

            # wykorzystanie metody zwracajacej obraz wielu funkcji jednej zmiennej
            fig = self.chart.plot_a_several_function(self.start_w, self.stop_w,
                                                     self.if_grid, formula_list)

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
                if 'syntax error' in self.chart.info:
                    info = self.chart.info.replace('syntax error in ', '')
                    tkinter.messagebox.showerror('Błąd formuły', 'Błąd formuły, wystąpił błąd składni formuły - {}'.format(info))
                elif 'name error' in self.chart.info:
                    info = self.chart.info.replace('name error in ', '')
                    tkinter.messagebox.showerror('Błąd formuły',
                                                 'Błąd formuły, funkcja musi być funkcją zależną od zmiennej x - {}'.format(info))
                elif "zero division error" in self.chart.info:
                    info = self.chart.info.replace('zero division error in ', '')
                    tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpiła próba dzielenia przez 0 - {}".format(info))
                elif "type error" in self.chart.info:
                    info = self.chart.info.replace('type error in ', '')
                    tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpił błąd typu - {}".format(info))
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
