import tkinter.messagebox
from tkinter import *

from PIL import ImageTk, Image
from customtkinter import *

from Program_logic import CalculusAndAnalysis


class DualIntegralGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(700, 410))
        self.parent.resizable(False, False)
        self.s_limit1 = None
        self.e_limit1 = None
        self.start_limit1 = None
        self.end_limit1 = None
        self.s_limit2 = None
        self.e_limit2 = None
        self.start_limit2 = None
        self.end_limit2 = None
        self.formula = None
        self.math_ = CalculusAndAnalysis
        self.create()

    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=700, height=410, bg_color='white', fg_color='white',
                                    border_color='white')

        pause0_frame = CTkFrame(self.frame_entry, width=700, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause0_frame.pack()

        info_frame = CTkFrame(self.frame_entry, width=700, height=100, bg_color='white', fg_color='white',
                              border_color='white')

        intro = CTkLabel(info_frame, width=700, height=30, bg_color='white', text='''W celu określenia wzoru posługuj się zapisem używanym w aplikacji WolframAlpha
        Aby obliczyć całkę oznaczoną uzupełnij granice całkowania - oo oraz inf oznaczają zakres do nieskończoności
        Aby obliczyć całke nieoznaczoną pozostaw granice całkowania puste
        Funkcja musi być funkcją zmiennej x oraz y''', fg_color='white')

        intro.pack()
        info_frame.pack()
        pause1_frame = CTkFrame(self.frame_entry, width=700, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()

        upper_frame = CTkFrame(self.frame_entry, width=700, height=30, bg_color='white', fg_color='white',
                               border_color='white')

        label_upper_left = CTkLabel(upper_frame, text_color='white', width=175, height=30, bg_color='white',
                                    fg_color='white')
        label_fun = CTkLabel(upper_frame, text='Podaj funkcje F(x, y):', width=350, height=30,
                             bg_color='white', text_font=("Arial Bold", 13),
                             fg_color='white')
        label_upper_right = CTkLabel(upper_frame, text_color='white', width=175, height=30, bg_color='white',
                                     fg_color='white')
        label_upper_left.grid(row=0, column=0)
        label_fun.grid(row=0, column=1)
        label_upper_right.grid(row=0, column=2)

        upper_frame.pack()

        pause2_frame = CTkFrame(self.frame_entry, width=700, height=40, bg_color='white', fg_color='white',
                                border_color='white')

        left_label = CTkLabel(pause2_frame, text_color='white', width=97, height=40, bg_color='white',
                              fg_color='white')
        left_label.grid(row=0, column=0)
        self.e_limit1 = CTkEntry(pause2_frame, width=40, height=40)
        self.e_limit1.grid(row=0, column=1)
        self.e_limit2 = CTkEntry(pause2_frame, width=40, height=40)
        self.e_limit2.grid(row=0, column=2)
        right_label = CTkLabel(pause2_frame, text_color='white', width=545, height=40, bg_color='white',
                               fg_color='white')
        right_label.grid(row=0, column=3)
        pause2_frame.pack()

        formula_frame = CTkFrame(self.frame_entry, width=700, height=64, bg_color='white', fg_color='white',
                                 border_color='white')

        left2_label = CTkLabel(formula_frame, text_color='white', width=93, height=64, bg_color='white',
                               fg_color='white')

        left2_label.grid(row=0, column=0)

        iconPath = 'images/dual_integral.jpg'
        icon = ImageTk.PhotoImage(Image.open(iconPath))
        icon_size = CTkLabel(formula_frame, bg_color='white', fg_color='white')
        icon_size.image = icon
        icon_size.configure(image=icon)
        icon_size.grid(row=0, column=1)

        self.formula = CTkEntry(formula_frame, width=350, height=64)
        self.formula.grid(row=0, column=2)

        iconPath1 = 'images/dxdy.jpg'
        icon1 = ImageTk.PhotoImage(Image.open(iconPath1))
        icon_size1 = CTkLabel(formula_frame, bg_color='white', fg_color='white')
        icon_size1.image = icon1
        icon_size1.configure(image=icon1)
        icon_size1.grid(row=0, column=3)

        right2_label = CTkLabel(formula_frame, text_color='white', width=72, height=64, bg_color='white',
                                fg_color='white')

        right2_label.grid(row=0, column=4)

        formula_frame.pack()

        pause3_frame = CTkFrame(self.frame_entry, width=700, height=40, bg_color='white', fg_color='white',
                                border_color='white')

        left3_label = CTkLabel(pause3_frame, text_color='white', width=97, height=40, bg_color='white',
                               fg_color='white')
        left3_label.grid(row=0, column=0)
        self.s_limit1 = CTkEntry(pause3_frame, width=40, height=40)
        self.s_limit1.grid(row=0, column=1)
        self.s_limit2 = CTkEntry(pause3_frame, width=40, height=40)
        self.s_limit2.grid(row=0, column=2)

        right3_label = CTkLabel(pause3_frame, text_color='white', width=545, height=40, bg_color='white',
                                fg_color='white')
        right3_label.grid(row=0, column=3)
        pause3_frame.pack()

        pause4_frame = CTkFrame(self.frame_entry, width=500, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause4_frame.pack()

        bottom_frame = CTkFrame(self.frame_entry, width=700, height=50, bg_color='white', fg_color='white',
                                border_color='white')

        accept_button = CTkButton(bottom_frame, text='potwierdź', width=70, command=self.add_widget)
        accept_button.pack()
        bottom_frame.pack()

        pause5_frame = CTkFrame(self.frame_entry, width=500, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause5_frame.pack()

        self.frame_entry.pack()

    def add_widget(self):

        if self.formula.get() == '':
            tkinter.messagebox.showinfo('Brak formuły', "Nie wprowadzono formuły funkcji")
        else:
            if self.frame_widget is not None:
                DualIntegralGui.del_widget(self)

            self.frame_widget = CTkFrame(self.frame_entry, width=700, height=100, bg_color='white smoke',
                                         fg_color='white smoke',
                                         border_color='white smoke')

            frame_pause = CTkFrame(self.frame_widget, width=700, height=10, bg_color='white smoke', fg_color='white smoke',
                                   border_color='white smoke')

            frame_pause.pack()

            frame_result = CTkFrame(self.frame_widget, width=700, height=50, bg_color='white smoke', fg_color='white smoke',
                                    border_color='white smoke')

            formula = self.formula.get()

            if self.s_limit1.get() == '':
                self.start_limit1 = None
            elif self.s_limit1.get().isdigit():
                self.start_limit1 = int(self.s_limit1.get())
            elif self.s_limit1.get() == 'oo' or self.s_limit1.get() == 'inf' or self.s_limit1.get() == '-oo' or self.s_limit1.get() == '-inf':
                self.start_limit1 = self.s_limit1.get()
            elif self.s_limit1.get().lstrip('-').isdigit():
                self.start_limit1 = self.s_limit1.get()
            else:
                tkinter.messagebox.showerror('Błąd',
                                             "Błędna pierwsza dolna granica całkowania, nie jest ona liczbą ani nieskończonością")

            if self.e_limit1.get() == '':
                self.end_limit1 = None
            elif self.e_limit1.get().isdigit():
                self.end_limit1 = int(self.e_limit1.get())
            elif self.e_limit1.get() == 'oo' or self.e_limit1.get() == 'inf' or self.e_limit1.get() == '-oo' or self.e_limit1.get() == '-inf':
                self.end_limit1 = self.e_limit1.get()
            elif self.e_limit1.get().lstrip('-').isdigit():
                self.end_limit1 = self.e_limit1.get()
            else:
                tkinter.messagebox.showerror('Błąd',
                                             "Błędna pierwsza górna granica całkowania, nie jest ona liczbą ani nieskończonością")

            if self.s_limit2.get() == '':
                self.start_limit2 = None
            elif self.s_limit2.get().isdigit():
                self.start_limit2 = int(self.s_limit2.get())
            elif self.s_limit2.get() == 'oo' or self.s_limit2.get() == 'inf' or self.s_limit2.get() == '-oo' or self.s_limit2.get() == '-inf':
                self.start_limit2 = self.s_limit2.get()
            elif self.s_limit2.get().lstrip('-').isdigit():
                self.start_limit2 = self.s_limit2.get()
            else:
                tkinter.messagebox.showerror('Błąd',
                                             "Błędna druga dolna granica całkowania, nie jest ona liczbą ani nieskończonością")

            if self.e_limit2.get() == '':
                self.end_limit2 = None
            elif self.e_limit2.get().isdigit():
                self.end_limit2 = int(self.e_limit2.get())
            elif self.e_limit2.get() == 'oo' or self.e_limit2.get() == 'inf' or self.e_limit2.get() == '-oo' or self.e_limit2.get() == '-inf':
                self.end_limit2 = self.e_limit2.get()
            elif self.e_limit2.get().lstrip('-').isdigit():
                self.end_limit2 = self.e_limit2.get()
            else:
                tkinter.messagebox.showerror('Błąd',
                                             "Błędna druga górna granica całkowania, nie jest ona liczbą ani nieskończonością")

            result = self.math_.CalculusAndAnalysis.dual_integration(formula, 'x', 'y', self.start_limit1, self.end_limit1,
                                                                     self.start_limit2, self.end_limit2)

            if isinstance(result, str):

                label_r = CTkLabel(frame_result, text='Wynik: ', width=350, height=50,
                                   bg_color='white smoke', text_font=("Arial Bold", 13),
                                   fg_color='white smoke')
                label_r.grid(row=0, column=0)

                label_final = CTkLabel(frame_result, text='Wystąpił błąd', width=350, height=50,
                                       bg_color='white smoke', text_font=("Arial Bold", 13),
                                       fg_color='white smoke')
                label_final.grid(row=0, column=1)

                if 'error' in result:
                    if result == 'syntax error':
                        tkinter.messagebox.showerror('Błąd formuły', '''Błąd formuły, wystąpił błąd składni formuły''')
                    elif result == 'name error':
                        tkinter.messagebox.showerror('Błąd formuły',
                                                     'Błąd formuły, funkcja musi być funkcją zależną od zmiennej x i/lub y')
                    elif result == "zero division error":
                        tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpiła próba dzielenia przez 0")
                    elif result == "type error":
                        tkinter.messagebox.showerror('Błąd formuły', "Błąd formuły, wystąpił błąd typu")
                    else:
                        tkinter.messagebox.showerror('Błąd formuły',
                                                     'Błąd formuły, wystąpił nieoczekiwany błąd, sprawdź poprawność zapisu albo spróbuj ponownie')
                else:
                    tkinter.messagebox.showerror("Błąd", result)
            else:
                label_r = CTkLabel(frame_result, text='Wynik: ', width=350, height=50,
                                   bg_color='white smoke', text_font=("Arial Bold", 13),
                                   fg_color='white smoke')
                label_r.grid(row=0, column=0)

                label_final = CTkLabel(frame_result, text=result, width=350, height=50,
                                       bg_color='white smoke', text_font=("Arial Bold", 13),
                                       fg_color='white smoke')
                label_final.grid(row=0, column=1)

            frame_result.pack()

            frame_pause1 = CTkFrame(self.frame_widget, width=700, height=10, bg_color='white smoke', fg_color='white smoke',
                                    border_color='white smoke')

            frame_pause1.pack()
            self.frame_widget.pack()

    def del_widget(self):
        self.frame_widget.destroy()


if __name__ == '__main__':
    master = Tk()
    s = DualIntegralGui(master)
    s.mainloop()
