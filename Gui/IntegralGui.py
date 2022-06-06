import tkinter.messagebox
from tkinter import *

from PIL import ImageTk, Image
from customtkinter import *

from Program_logic import CalculusAndAnalysis


class IntegralGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(800, 410))
        self.parent.resizable(False, False)
        self.s_limit = None
        self.e_limit = None
        self.start_limit = None
        self.end_limit = None
        self.formula = None
        # wykorzystanie wcześniej wykonanego backend'u
        self.math_ = CalculusAndAnalysis
        self.create()

    # funkcja tworzaca przestrzen pracy dla danego okna
    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=800, height=410, bg_color='white', fg_color='white',
                                    border_color='white')

        # frame z przerwa
        pause0_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause0_frame.pack()

        # frame z informacja wejsciowa
        info_frame = CTkFrame(self.frame_entry, width=800, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        intro = CTkLabel(info_frame, width=800, height=30, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
        Aby obliczyć całkę oznaczoną uzupełnij granice całkowania - oo oraz inf oznaczają zakres do nieskończoności
        Aby obliczyć całke nieoznaczoną pozostaw granice całkowania puste
        Funkcja musi być funkcją zmiennej x''', fg_color='white')

        intro.pack()
        info_frame.pack()

        # frame z przerwa
        pause1_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()

        # frame z informajca odnoszaca sie do wprowadzanej funkcji
        upper_frame = CTkFrame(self.frame_entry, width=800, height=30, bg_color='white', fg_color='white',
                               border_color='white')

        label_upper_left = CTkLabel(upper_frame, text_color='white', width=200, height=30, bg_color='white',
                                    fg_color='white')
        label_size = CTkLabel(upper_frame, text='Podaj funkcje F(x):', width=350, height=30,
                              bg_color='white', text_font=("Arial Bold", 13),
                              fg_color='white')
        label_upper_right = CTkLabel(upper_frame, text_color='white', width=300, height=30, bg_color='white',
                                     fg_color='white')
        label_upper_left.grid(row=0, column=0)
        label_size.grid(row=0, column=1)
        label_upper_right.grid(row=0, column=2)

        upper_frame.pack()

        # frame z przerwa
        pause2_frame = CTkFrame(self.frame_entry, width=800, height=40, bg_color='white', fg_color='white',
                                border_color='white')

        left_label = CTkLabel(pause2_frame, text_color='white', width=89, height=40, bg_color='white',
                              fg_color='white')
        left_label.grid(row=0, column=0)
        # ustalenie limitow calkowania
        self.e_limit = CTkEntry(pause2_frame, width=40, height=40)
        self.e_limit.grid(row=0, column=1)
        right_label = CTkLabel(pause2_frame, text_color='white', width=701, height=40, bg_color='white',
                               fg_color='white')
        right_label.grid(row=0, column=2)
        pause2_frame.pack()

        # frame funkcji
        formula_frame = CTkFrame(self.frame_entry, width=800, height=64, bg_color='white', fg_color='white',
                                 border_color='white')

        left2_label = CTkLabel(formula_frame, text_color='white', width=59, height=64, bg_color='white',
                               fg_color='white')

        left2_label.grid(row=0, column=0)

        # wstawienie obrazka calki
        iconPath = 'images/integral.jpg'
        icon = ImageTk.PhotoImage(Image.open(iconPath))
        icon_size = CTkLabel(formula_frame, bg_color='white', fg_color='white')
        icon_size.image = icon
        icon_size.configure(image=icon)
        icon_size.grid(row=0, column=1)

        # okno do wprowadzenia formuly
        self.formula = CTkEntry(formula_frame, width=350, height=64)
        self.formula.grid(row=0, column=2)

        # obrazek calkowania po dx
        iconPath1 = 'images/dx.jpg'
        icon1 = ImageTk.PhotoImage(Image.open(iconPath1))
        icon_size1 = CTkLabel(formula_frame, bg_color='white', fg_color='white')
        icon_size1.image = icon1
        icon_size1.configure(image=icon1)
        icon_size1.grid(row=0, column=3)

        right2_label = CTkLabel(formula_frame, text_color='white', width=300, height=64, bg_color='white',
                                fg_color='white')

        right2_label.grid(row=0, column=4)

        formula_frame.pack()

        # frame z przerwa
        pause3_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')

        left3_label = CTkLabel(pause3_frame, text_color='white', width=89, height=40, bg_color='white',
                               fg_color='white')
        left3_label.grid(row=0, column=0)
        # ustalenie limitow calkowania
        self.s_limit = CTkEntry(pause3_frame, width=40, height=40)
        self.s_limit.grid(row=0, column=1)
        right3_label = CTkLabel(pause3_frame, text_color='white', width=701, height=40, bg_color='white',
                                fg_color='white')
        right3_label.grid(row=0, column=2)
        pause3_frame.pack()

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
        else:
            # jesli zostala juz wczeniej utworzona (drugie i kolejne wywolania funkcji) kasujemy przestrzen wynikowa
            if self.frame_widget is not None:
                IntegralGui.del_widget(self)

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

            # sprawdzenie poprawnosci granicy calkowania
            if self.s_limit.get() == '':
                self.start_limit = None
            elif self.s_limit.get().isdigit():
                self.start_limit = int(self.s_limit.get())
            elif self.s_limit.get() == 'oo' or self.s_limit.get() == 'inf' or self.s_limit.get() == '-oo' or self.s_limit.get() == '-inf':
                self.start_limit = self.s_limit.get()
            elif self.s_limit.get().lstrip('-').isdigit():
                self.start_limit = self.s_limit.get()
            else:
                tkinter.messagebox.showerror('Błąd',
                                             "Błędna dolna granica całkowania, nie jest ona liczbą ani nieskończonością")

            if self.e_limit.get() == '':
                self.end_limit = None
            elif self.e_limit.get().isdigit():
                self.end_limit = int(self.e_limit.get())
            elif self.e_limit.get() == 'oo' or self.e_limit.get() == 'inf' or self.e_limit.get() == '-oo' or self.e_limit.get() == '-inf':
                self.end_limit = self.e_limit.get()
            elif self.e_limit.get().lstrip('-').isdigit():
                self.end_limit = self.e_limit.get()
            else:
                tkinter.messagebox.showerror('Błąd',
                                             "Błędna górna granica całkowania, nie jest ona liczbą ani nieskończonością")

            # wykorzystanie metody zwracajacej wynik dzialania
            result = self.math_.CalculusAndAnalysis.integration(formula, 'x', self.start_limit, self.end_limit)

            # jesli wynik jest stringiem wtedy blad i odpowiednie dzialanie
            if isinstance(result, str):

                label_r = CTkLabel(frame_result, text='Wynik: ', width=150, height=50,
                                   bg_color='white smoke', text_font=("Arial Bold", 13),
                                   fg_color='white smoke')
                label_r.grid(row=0, column=0)

                label_final = CTkLabel(frame_result, text='Wystąpił błąd', width=650, height=50,
                                       bg_color='white smoke', text_font=("Arial Bold", 13),
                                       fg_color='white smoke')
                label_final.grid(row=0, column=1)

                if 'error' in result:
                    if result == 'syntax error':
                        tkinter.messagebox.showerror('Błąd formuły', '''Błąd formuły, wystąpił błąd składni formuły''')
                    elif result == 'name error':
                        tkinter.messagebox.showerror('Błąd formuły',
                                                     'Błąd formuły, funkcja musi być funkcją zależną od zmiennej x')
                    elif result == "zero division error":
                        tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpiła próba dzielenia przez 0")
                    elif result == "type error":
                        tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpił błąd typu")
                    else:
                        tkinter.messagebox.showerror('Błąd formuły',
                                                     'Błąd formuły, wystąpił nieoczekiwany błąd, sprawdź poprawność zapisu albo spróbuj ponownie')
                else:
                    tkinter.messagebox.showerror("Błąd", result)
            # jesli nie jest stringiem to wtedy wynik prawidlowy i wypisanie
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
