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
        self.parent.geometry("{}x{}".format(800, 350))
        self.parent.resizable(False, False)
        self.side = None
        self.side_char = None
        self.e_limit = None
        self.end_limit = None
        self.formula = None
        self.math_ = CalculusAndAnalysis
        self.create()

    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=800, height=410, bg_color='white', fg_color='white',
                                    border_color='white')

        pause0_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause0_frame.pack()

        info_frame = CTkFrame(self.frame_entry, width=800, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        intro = CTkLabel(info_frame, width=800, height=50, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
               Aby obliczyć granice funkcji musisz określić punkt do którego funkcja dąży - oo oraz inf oznaczają zakres do nieskończoności
               Możesz określić również strone do której granica dąży stawiając odpowiednio + lub -
               Funkcja musi być funkcją zmiennej x''', fg_color='white')

        intro.pack()
        info_frame.pack()
        pause1_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()

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

        frame_fun = CTkFrame(self.frame_entry, width=800, height=83, bg_color='white', fg_color='white',
                             border_color='white')

        frame_graphic = CTkFrame(frame_fun, width=225, height=83, bg_color='white', fg_color='white',
                                 border_color='white')

        frame_upper_graphic = CTkFrame(frame_graphic, width=225, height=43, bg_color='white', fg_color='white',
                                       border_color='white')

        label_upper_graphic_left = CTkLabel(frame_upper_graphic, text_color='white', width=141, height=43,
                                            bg_color='white',
                                            fg_color='white')
        label_upper_graphic_left.grid(row=0, column=0)

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

        frame_entry = CTkFrame(frame_fun, width=350, height=83, bg_color='white', fg_color='white',
                               border_color='white')

        self.formula = CTkEntry(frame_entry, width=350, height=50)
        self.formula.pack()
        frame_entry.grid(row=0, column=1)

        frame_fun_right = CTkFrame(frame_fun, width=225, height=83, bg_color='white', fg_color='white',
                                   border_color='white')
        frame_fun_right.grid(row=0, column=2)

        frame_fun.pack()

        pause4_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause4_frame.pack()

        bottom_frame = CTkFrame(self.frame_entry, width=800, height=50, bg_color='white', fg_color='white',
                                border_color='white')

        accept_button = CTkButton(bottom_frame, text='potwierdź', width=70, command=self.add_widget)
        accept_button.pack()
        bottom_frame.pack()

        pause5_frame = CTkFrame(self.frame_entry, width=800, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause5_frame.pack()

        self.frame_entry.pack()

    def add_widget(self):
        flag = True
        if self.frame_widget is not None:
            LimitsGui.del_widget(self)

        self.frame_widget = CTkFrame(self.frame_entry, width=800, height=100, bg_color='white smoke',
                                     fg_color='white smoke',
                                     border_color='white smoke')
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

        if self.formula.get() == '':
            tkinter.messagebox.showinfo('Brak formuły', "Nie wprowadzono formuły funkcji")
            flag = False

        if flag:
            if self.frame_widget is not None:
                LimitsGui.del_widget(self)

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

            if self.side.get() == '' or self.side.get() == '+' or self.side.get() == '-':
                if self.side.get() == '':
                    self.side_char = None
                elif self.side.get() == '+' or self.side.get() == '-':
                    self.side_char = self.side.get()

                result = self.math_.CalculusAndAnalysis.limits(formula, 'x', self.end_limit, self.side_char)

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
                    else:
                        tkinter.messagebox.showerror("Błąd", result)
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
            else:
                tkinter.messagebox.showerror('Błąd',
                                             'Użyto nieprawidłowego znaku do określenia strony, dopuszczalne znaki to: "+" i "-"')

    def del_widget(self):
        self.frame_widget.destroy()


if __name__ == '__main__':
    master = Tk()
    s = LimitsGui(master)
    s.mainloop()
