import tkinter.messagebox
from tkinter import *

from PIL import ImageTk, Image
from customtkinter import *

from Program_logic import CalculusAndAnalysis


class LimitsGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(800, 400))
        self.parent.resizable(False, False)
        self.side = None
        self.side_char = None
        self.e_limit = None
        self.end_limit = None
        self.formula = None
        self.last_logs_results = LimitsGui.read_formula_file(self)
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


        button_log_frame = CTkFrame(self.frame_entry, width=800, height=50, bg_color='white', fg_color='white',
                                    border_color='white')

        label_pau = CTkLabel(button_log_frame, text_color='white', width=600, height=30, bg_color='white',
                             fg_color='white')
        log_button = CTkButton(button_log_frame, text='pokaż ostatnie działania', width=150,
                               command=self.show_last_logs)
        label_pau.grid(row=0, column=0)
        log_button.grid(row=0, column=1)
        button_log_frame.pack()

        # frame z przerwa
        pause__frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause__frame.pack()

        # frame z informacja wejsciowa
        info_frame = CTkFrame(self.frame_entry, width=800, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        intro = CTkLabel(info_frame, width=800, height=50, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
               Aby obliczyć granice funkcji musisz określić punkt do którego funkcja dąży - oo oraz inf oznaczają zakres do nieskończoności
               Możesz określić również strone do której granica dąży stawiając odpowiednio + lub -
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

        label_upper_left = CTkLabel(upper_frame, text_color='white', width=225, height=30, bg_color='white',
                                    fg_color='white')
        label_size = CTkLabel(upper_frame, text='Podaj funkcje f(x):', width=350, height=30,
                              bg_color='white', text_font=("Arial Bold", 13),
                              fg_color='white')
        label_upper_right = CTkLabel(upper_frame, text_color='white', width=225, height=30, bg_color='white',
                                     fg_color='white')
        label_upper_left.grid(row=0, column=0)
        label_size.grid(row=0, column=1)
        label_upper_right.grid(row=0, column=2)

        upper_frame.pack()

        # frame funkcji
        frame_fun = CTkFrame(self.frame_entry, width=800, height=83, bg_color='white', fg_color='white',
                             border_color='white')

        # frame z graficznym przedstawieniem granicy
        frame_graphic = CTkFrame(frame_fun, width=225, height=83, bg_color='white', fg_color='white',
                                 border_color='white')

        frame_upper_graphic = CTkFrame(frame_graphic, width=225, height=43, bg_color='white', fg_color='white',
                                       border_color='white')

        label_upper_graphic_left = CTkLabel(frame_upper_graphic, text_color='white', width=141, height=43,
                                            bg_color='white',
                                            fg_color='white')
        label_upper_graphic_left.grid(row=0, column=0)

        # wczytanie obrazu granicy
        iconPath = 'images/lim.jpg'
        icon = ImageTk.PhotoImage(Image.open(iconPath))
        icon_size = CTkLabel(frame_upper_graphic, bg_color='white', fg_color='white')
        icon_size.image = icon
        icon_size.configure(image=icon)
        icon_size.grid(row=0, column=1)

        label_upper_graphic_right = CTkLabel(frame_upper_graphic, text_color='white', width=26, height=43,
                                             bg_color='white',
                                             fg_color='white')
        label_upper_graphic_right.grid(row=0, column=2)

        frame_upper_graphic.pack()

        frame_bottom_graphic = CTkFrame(frame_graphic, width=225, height=40, bg_color='white', fg_color='white',
                                        border_color='white')

        label_bottom_graphic_left = CTkLabel(frame_bottom_graphic, text_color='white', width=66, height=43,
                                             bg_color='white',
                                             fg_color='white')
        label_bottom_graphic_left.grid(row=0, column=0)

        # wczytanie obrazu x dazy do
        iconPath1 = 'images/lim_x.jpg'
        icon1 = ImageTk.PhotoImage(Image.open(iconPath1))
        icon_size1 = CTkLabel(frame_bottom_graphic, bg_color='white', fg_color='white')
        icon_size1.image = icon1
        icon_size1.configure(image=icon1)
        icon_size1.grid(row=0, column=1)

        self.e_limit = CTkEntry(frame_bottom_graphic, width=40, height=40)
        self.e_limit.grid(row=0, column=2)

        self.side = CTkEntry(frame_bottom_graphic, width=23, height=23)
        self.side.grid(row=0, column=3)

        frame_bottom_graphic.pack()

        frame_graphic.grid(row=0, column=0)

        # frame z oknem do ktorego wprowadzamy funkcje
        frame_entry = CTkFrame(frame_fun, width=350, height=83, bg_color='white', fg_color='white',
                               border_color='white')

        self.formula = CTkEntry(frame_entry, width=350, height=50)
        self.formula.pack()
        frame_entry.grid(row=0, column=1)

        frame_fun_right = CTkFrame(frame_fun, width=225, height=83, bg_color='white', fg_color='white',
                                   border_color='white')
        frame_fun_right.grid(row=0, column=2)

        frame_fun.pack()

        # frame z przerwa
        pause4_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause4_frame.pack()

        bottom_frame = CTkFrame(self.frame_entry, width=800, height=50, bg_color='white', fg_color='white',
                                border_color='white')

        # frame z guzikiem ktory przetwarza wyrazenie i zwraca wynik
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
        flag = True
        # jesli zostala juz wczeniej utworzona (drugie i kolejne wywolania funkcji) kasujemy przestrzen wynikowa
        if self.frame_widget is not None:
            LimitsGui.del_widget(self)

        # tworzenie frame wynikowego
        self.frame_widget = CTkFrame(self.frame_entry, width=800, height=100, bg_color='white smoke',
                                     fg_color='white smoke',
                                     border_color='white smoke')
        # jesli nie ma punktu granicznego zwracamy komunikat
        if self.e_limit.get() == '':
            tkinter.messagebox.showinfo('Brak granicy', "Nie wprowadzono punktu określającego granice funkcji")
            flag = False
        elif self.e_limit.get().isdigit():
            self.end_limit = int(self.e_limit.get())
        elif self.e_limit.get() == 'oo' or self.e_limit.get() == 'inf' or self.e_limit.get() == '-oo' or self.e_limit.get() == '-inf':
            self.end_limit = self.e_limit.get()
        elif self.e_limit.get().lstrip('-').isdigit():
            self.end_limit = self.e_limit.get()
        else:
            tkinter.messagebox.showerror('Błąd',
                                         "Błędny punkt określający granice, nie jest on liczbą ani nieskończonością")
            flag = False

        # jesli nie ma formuly zwracamy komunikat
        if self.formula.get() == '':
            tkinter.messagebox.showinfo('Brak formuły', "Nie wprowadzono formuły funkcji")
            flag = False

        if flag:
            # frame z przerwa
            frame_pause = CTkFrame(self.frame_widget, width=800, height=10, bg_color='white smoke',
                                   fg_color='white smoke',
                                   border_color='white smoke')

            frame_pause.pack()

            # frame z wynikiem obliczen
            frame_result = CTkFrame(self.frame_widget, width=800, height=50, bg_color='white smoke',
                                    fg_color='white smoke',
                                    border_color='white smoke')

            formula = self.formula.get()

            if self.side.get() == '' or self.side.get() == '+' or self.side.get() == '-':
                if self.side.get() == '':
                    self.side_char = None
                elif self.side.get() == '+' or self.side.get() == '-':
                    self.side_char = self.side.get()

                # wykorzystanie metody zwracajacej wynik dzialania
                result = self.math_.CalculusAndAnalysis.limits(formula, 'x', self.end_limit, self.side_char)

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
                            tkinter.messagebox.showerror('Błąd formuły',
                                                         '''Błąd formuły, wystąpił błąd składni formuły''')
                        elif result == 'name error':
                            tkinter.messagebox.showerror('Błąd formuły',
                                                         'Błąd formuły, funkcja musi być funkcją zależną od zmiennej x')
                        elif result == "zero division error":
                            tkinter.messagebox.showerror('Błąd formuły',
                                                         "Błąd formuły, wystąpiła próba dzielenia przez 0")
                        elif result == "type error":
                            tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpił błąd typu")
                        else:
                            tkinter.messagebox.showerror('Błąd formuły',
                                                         'Błąd formuły, wystąpił nieoczekiwany błąd, sprawdź poprawność zapisu albo spróbuj ponownie')
                        self.add_log_to_file(formula, result)
                    else:
                        tkinter.messagebox.showerror("Błąd", result)
                        self.add_log_to_file(formula, result)
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
                    self.add_log_to_file(formula, result)

                frame_result.pack()

                frame_pause1 = CTkFrame(self.frame_widget, width=800, height=10, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')

                frame_pause1.pack()
                self.frame_widget.pack()
            else:
                tkinter.messagebox.showerror('Błąd',
                                             'Użyto nieprawidłowego znaku do określenia strony, dopuszczalne znaki to: "+" i "-"')

    # metoda odpowiedzialna za niszczenie obszaru wynikowego
    def del_widget(self):
        self.frame_widget.destroy()

    def read_formula_file(self):
        f = open("logs/limits_logs.txt", "r")
        whole_file = []
        for line in f:
            whole_file.append(line)
        f.close()
        whole_file.reverse()

        last_logs = []
        if len(whole_file) >= 5:
            for i in range(5):
                last_logs.append(whole_file[i])
        else:
            for i in range(len(whole_file)):
                last_logs.append(whole_file[i])

        return last_logs

    def add_log_to_file(self, formula, result):
        f = open("logs/limits_logs.txt", "a")
        f.write('\nformula: {} - result: {}'.format(formula, result))
        f.close()

    def show_last_logs(self):
        self.last_logs_results = LimitsGui.read_formula_file(self)
        newWindow = Toplevel(self.parent)
        newWindow.title("Ostatnie obliczenia")
        newWindow.geometry("400x120")
        newWindow.resizable(False, False)
        v = Scrollbar(newWindow, orient='horizontal')
        v.pack(side=BOTTOM, fill='x')

        t = Text(newWindow, wrap=NONE, xscrollcommand=v.set)

        for i in range(len(self.last_logs_results)):
            if i == 0:
                s = str(self.last_logs_results[i]+'\n')
            else:
                s = str(self.last_logs_results[i])
            t.insert(END, s)
        t.pack()
        v.config(command=t.xview)

        newWindow.mainloop()
