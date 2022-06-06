import tkinter.messagebox
from tkinter import *

from PIL import ImageTk, Image
from customtkinter import *

from Program_logic import CalculusAndAnalysis


class DifferentiationGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(800, 315))
        self.parent.resizable(False, False)
        self.formula = None
        self.symbol = None
        # wykorzystanie wcześniej wykonanego backend'u
        self.math_ = CalculusAndAnalysis
        self.create()

    # funkcja tworzaca przestrzen pracy dla danego okna
    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=800, height=410, bg_color='white', fg_color='white',
                                    border_color='white')

        # frame z przerwa
        pause0_frame = CTkFrame(self.frame_entry, width=700, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause0_frame.pack()

        # frame z informacja wejsciowa
        info_frame = CTkFrame(self.frame_entry, width=700, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        intro = CTkLabel(info_frame, width=700, height=30, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
              Funkcja może być funkcją dowolnej zmiennej''', fg_color='white')

        intro.pack()
        info_frame.pack()

        # frame z przerwa
        pause1_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()

        # frame z informajca odnoszaca sie do wprowadzanej funkcji
        upper_frame = CTkFrame(self.frame_entry, width=800, height=30, bg_color='white', fg_color='white',
                               border_color='white')

        label_upper_left = CTkLabel(upper_frame, text_color='white', width=225, height=30, bg_color='white',
                                    fg_color='white')
        label_fun = CTkLabel(upper_frame, text='Podaj funkcje by wyliczyć pochodną:', width=350, height=30,
                             bg_color='white', text_font=("Arial Bold", 13),
                             fg_color='white')
        label_upper_right = CTkLabel(upper_frame, text_color='white', width=225, height=30, bg_color='white',
                                     fg_color='white')
        label_upper_left.grid(row=0, column=0)
        label_fun.grid(row=0, column=1)
        label_upper_right.grid(row=0, column=2)

        upper_frame.pack()

        # frame z przerwa
        pause2_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause2_frame.pack()

        # frame funkcji
        function_frame = CTkFrame(self.frame_entry, width=800, height=43, bg_color='white', fg_color='white',
                                  border_color='white')

        label_left = CTkLabel(upper_frame, text_color='white', width=98, height=43, bg_color='white',
                              fg_color='white')

        label_left.grid(row=0, column=0)

        # wstawienie obrazka pochodnej
        iconPath1 = 'images/f_.jpg'
        icon1 = ImageTk.PhotoImage(Image.open(iconPath1))
        icon_size1 = CTkLabel(function_frame, bg_color='white', fg_color='white')
        icon_size1.image = icon1
        icon_size1.configure(image=icon1)
        icon_size1.grid(row=0, column=1)

        # okreslenie zmiennej pochodnej
        self.symbol = CTkEntry(function_frame, width=40, height=43)

        self.symbol.grid(row=0, column=2)

        # wstawienie obrazka pochodnej 2
        iconPath2 = 'images/bracket.jpg'
        icon2 = ImageTk.PhotoImage(Image.open(iconPath2))
        icon_size2 = CTkLabel(function_frame, bg_color='white', fg_color='white')
        icon_size2.image = icon2
        icon_size2.configure(image=icon2)
        icon_size2.grid(row=0, column=3)

        label_eq = CTkLabel(function_frame, text='=\t', width=43, height=43,
                            bg_color='white', text_font=("Arial Bold", 15),
                            fg_color='white')
        label_eq.grid(row=0, column=4)

        # wprowadzenie formuły funkcji
        self.formula = CTkEntry(function_frame, width=350, height=43)

        self.formula.grid(row=0, column=5)

        label_right = CTkLabel(upper_frame, text_color='white', width=98, height=43, bg_color='white',
                               fg_color='white')

        label_right.grid(row=0, column=6)

        function_frame.pack()

        # frame z przerwa
        pause4_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause4_frame.pack()

        # frame z guzikiem ktory przetwarza wyrazenie i zwraca wynik
        bottom_frame = CTkFrame(self.frame_entry, width=800, height=50, bg_color='white', fg_color='white',
                                border_color='white')

        accept_button = CTkButton(bottom_frame, text='potwierdź', width=70, command=self.add_widget)
        accept_button.pack()
        bottom_frame.pack()

        # frame z przerwa
        pause5_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause5_frame.pack()

        self.frame_entry.pack()

    # funkcja tworzaca przestrzen wynikowa
    def add_widget(self):

        # jesli nie ma formuly zwracamy komunikat
        if self.formula.get() == '':
            tkinter.messagebox.showinfo('Brak formuły', "Nie wprowadzono formuły funkcji")
        # jesli nie ma symbolu zwracamy komunikat
        elif self.symbol.get() == '':
            tkinter.messagebox.showinfo('Brak symbolu', "Nie wprowadzono symbolu funkcji")
        else:
            # jesli zostala juz wczeniej utworzona (drugie i kolejne wywolania funkcji) kasujemy przestrzen wynikowa
            if self.frame_widget is not None:
                DifferentiationGui.del_widget(self)

            # tworzenie frame wynikowego
            self.frame_widget = CTkFrame(self.frame_entry, width=800, height=100, bg_color='white smoke',
                                         fg_color='white smoke',
                                         border_color='white smoke')

            frame_pause = CTkFrame(self.frame_widget, width=800, height=10, bg_color='white smoke',
                                   fg_color='white smoke',
                                   border_color='white smoke')

            frame_pause.pack()

            frame_result = CTkFrame(self.frame_widget, width=800, height=50, bg_color='white smoke',
                                    fg_color='white smoke',
                                    border_color='white smoke')

            formula = self.formula.get()

            # wykorzystanie metody zwracajacej wynik dzialania
            result = self.math_.CalculusAndAnalysis.differentiation(formula, self.symbol.get())

            # jesli wynik zawiera podstring error wtedy blad i odpowiednie dzialanie
            if 'error' in result:
                if result == 'syntax error':
                    tkinter.messagebox.showerror('Błąd formuły', '''Błąd formuły, wystąpił błąd składni formuły''')
                elif result == 'name error':
                    tkinter.messagebox.showerror('Błąd formuły',
                                                 'Błąd formuły, funkcja musi być funkcją zależną od zmiennej {}'.format(
                                                     self.symbol.get()))
                elif result == "zero division error":
                    tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpiła próba dzielenia przez 0")
                elif result == "type error":
                    tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpił błąd typu")
                else:
                    tkinter.messagebox.showerror('Błąd formuły',
                                                 'Błąd formuły, wystąpił nieoczekiwany błąd, sprawdź poprawność zapisu albo spróbuj ponownie')
            # jesli wynik zawiera podstring formula wtedy blad i odpowiednie dzialanie
            elif 'formuła' in result:
                tkinter.messagebox.showerror('Błąd formuły', result)
            # w przecwinym przypadku wynik prawidlowy i wypisanie
            else:

                label_r = CTkLabel(frame_result, text='Wynik: ', width=100, height=50,
                                   bg_color='white smoke', text_font=("Arial Bold", 13),
                                   fg_color='white smoke')
                label_r.grid(row=0, column=0)

                label_final = CTkLabel(frame_result, text=result, width=700, height=50,
                                       bg_color='white smoke', text_font=("Arial Bold", 13),
                                       fg_color='white smoke')
                label_final.grid(row=0, column=1)

            frame_result.pack()

            frame_pause1 = CTkFrame(self.frame_widget, width=800, height=10, bg_color='white smoke',
                                    fg_color='white smoke',
                                    border_color='white smoke')

            frame_pause1.pack()
            self.frame_widget.pack()

    # metoda odpowiedzialna za niszczenie obszaru wynikowego
    def del_widget(self):
        self.frame_widget.destroy()
