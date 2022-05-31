import tkinter.messagebox
from tkinter import *

from customtkinter import *

from Program_logic.Matrix import Matrix, SquareMatrix


class SingleMatrixGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.parent = master
        self.parent.geometry("{}x{}".format(1100, 600))
        self.parent.resizable(False, False)
        self.row_size = None
        self.col_size = None
        self.list_matrix = []
        self.create()
        self.matrix_app = Matrix()

    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=1100, height=600, bg_color='white', fg_color='white',
                                    border_color='white')
        pause1_frame = CTkFrame(self.frame_entry, width=1100, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()
        upper_frame = CTkFrame(self.frame_entry, width=1100, height=80, bg_color='white', fg_color='white',
                               border_color='white')
        label_size = CTkLabel(upper_frame, text='Podaj rozmiar macierzy:', width=100, height=30, bg_color='white',
                              fg_color='white')
        label_size.grid(row=0, column=0)
        self.row_size = CTkEntry(upper_frame, placeholder_text='X', width=35)
        self.row_size.grid(row=0, column=1)
        label_x = CTkLabel(upper_frame, text='x', width=10, height=30)
        label_x.grid(row=0, column=2)
        self.col_size = CTkEntry(upper_frame, placeholder_text='Y', width=35)
        self.col_size.grid(row=0, column=3)
        upper_frame.pack()
        pause2_frame = CTkFrame(self.frame_entry, width=1100, height=25, bg_color='white', fg_color='white',
                                border_color='white')
        pause2_frame.pack()
        middle_frame = CTkFrame(self.frame_entry, width=1100, height=50, bg_color='white', fg_color='white',
                                border_color='white')
        accept_button = CTkButton(middle_frame, text='potwierdź', width=70, command=self.add_widget)
        accept_button.grid(row=0)
        middle_frame.pack()
        pause3_frame = CTkFrame(self.frame_entry, width=1100, height=25, bg_color='white', fg_color='white',
                                border_color='white')
        pause3_frame.pack()

        self.frame_entry.pack()

    def add_widget(self):

        if self.frame_widget is not None:
            SingleMatrixGui.del_widget(self)
            self.list_matrix.clear()

        self.frame_widget = CTkFrame(self.frame_entry, width=1100, height=350, bg_color='white smoke',
                                     fg_color='white smoke',
                                     border_color='white smoke')

        frame_pause = CTkFrame(self.frame_widget, width=1100, height=40, bg_color='white smoke', fg_color='white smoke',
                               border_color='white smoke')

        if not self.col_size.get().isdigit():
            tkinter.messagebox.showerror("Błąd danych", "dana wprowadzona do pola odpowiadającego za ilość kolumn nie jest liczbą")
        elif not self.row_size.get().isdigit():
            tkinter.messagebox.showerror("Błąd danych", "dana wprowadzona do pola odpowiadającego za ilość rzędów nie jest liczbą")
        else:
            if int(self.col_size.get()) <= 10 and int(self.row_size.get()) <= 10:

                frame_matrix = CTkFrame(self.frame_widget, width=1100, height=250, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')
                for x in range(int(self.row_size.get())):
                    for y in range(int(self.col_size.get())):
                        en = CTkEntry(frame_matrix, width=35)
                        en.grid(row=x, column=y)
                        self.list_matrix.append(en)

                frame_matrix.pack()

                pause3_frame = CTkFrame(self.frame_widget, width=1100, height=50, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')
                pause3_frame.pack()

                button_frame = CTkFrame(self.frame_widget, width=1100, height=60, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')

                transposition_button = CTkButton(button_frame, width=130, text='Transpozycja',
                                                 command=self.calculate_transposition)
                transposition_button.grid(row=0, column=0)
                label_pause1 = CTkLabel(button_frame, bg_color='white smoke', fg_color='white smoke', text_color='white smoke',
                                        width=5)
                label_pause1.grid(row=0, column=1)

                rank_button = CTkButton(button_frame, width=130, text='Rząd macierzy',
                                        command=self.calculate_rank_of_matrix)
                rank_button.grid(row=0, column=2)

                label_pause2 = CTkLabel(button_frame, bg_color='white smoke', fg_color='white smoke', text_color='white smoke',
                                        width=5)
                label_pause2.grid(row=0, column=3)

                trace_button = CTkButton(button_frame, width=130, text='Ślad macierzy',
                                         command=self.calculate_trace_of_matrix)
                trace_button.grid(row=0, column=4)

                label_pause3 = CTkLabel(button_frame, bg_color='white smoke', fg_color='white smoke', text_color='white smoke',
                                        width=5)
                label_pause3.grid(row=0, column=5)

                determinant_button = CTkButton(button_frame, width=130, text='Wyznacznik macierzy',
                                               command=self.calculate_determinant_of_the_matrix)
                determinant_button.grid(row=0, column=6)

                label_pause4 = CTkLabel(button_frame, bg_color='white smoke', fg_color='white smoke', text_color='white smoke',
                                        width=5)
                label_pause4.grid(row=0, column=7)

                inversion_button = CTkButton(button_frame, width=130, text='Macierz odwrotna',
                                             command=self.calculate_inverse_matrix)
                inversion_button.grid(row=0, column=8)

                button_frame.pack()

                pause4_frame = CTkFrame(self.frame_widget, width=1100, height=50, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')
                pause4_frame.pack()

                self.frame_widget.pack()

            else:
                tkinter.messagebox.showinfo("Błąd wymiarów", "Proszę wybrać wymiary do maksymalnie 10")

    def del_widget(self):
        self.frame_widget.destroy()

    def calculate_transposition(self):
        self.matrix_app.number_of_rows = int(self.row_size.get())
        self.matrix_app.number_of_columns = int(self.col_size.get())

        values = []
        for val in self.list_matrix:
            if val.get() != '':
                if val.get().isdigit():
                    values.append(int(val.get()))
                elif val.get().lstrip('-').isdigit():
                    values.append(int(val.get()))
                else:
                    tkinter.messagebox.showerror(
                        "Błąd danych",
                        'Wystąpił błąd w macierzy, wartość {} nie jest liczbą, zostanie ona zamieniona na 0'.format(
                            val.get()))
                    values.append(0)
            else:
                values.append(0)

        self.matrix_app.values = self.matrix_app.check_data(values)
        self.matrix_app.matrix_form = self.matrix_app.reshape_to_matrix()
        transposed_matrix = self.matrix_app.transpose_matrix()

        newWindow = Toplevel(self.parent)
        newWindow.title('Wynik')
        w = 400
        h = 400

        ws = newWindow.winfo_screenwidth()
        hs = newWindow.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        title_frame = CTkFrame(newWindow, width=400, height=50, bg_color='white smoke',
                               fg_color='white smoke',
                               border_color='white smoke')

        pause1_label = CTkLabel(title_frame, width=400, height=10, bg_color='white smoke',
                                fg_color='white smoke', text_color='white smoke')
        pause1_label.pack()
        result_label = CTkLabel(title_frame, width=400, height=30, bg_color='white smoke',
                                fg_color='white smoke', text="Macierz transponowana")
        result_label.pack()
        pause2_label = CTkLabel(title_frame, width=400, height=10, bg_color='white smoke',
                                fg_color='white smoke', text_color='white smoke')
        pause2_label.pack()
        title_frame.pack()

        result_frame = CTkFrame(newWindow, width=400, height=330, bg_color='white smoke',
                                fg_color='white smoke',
                                border_color='white smoke')

        for y in range(int(self.row_size.get())):
            for x in range(int(self.col_size.get())):
                label = CTkEntry(result_frame, width=35, placeholder_text=self.matrix_app.matrix_form[y][x])
                label.grid(row=x, column=y)

        result_frame.pack()

        end_frame = CTkFrame(newWindow, width=400, height=20, bg_color='white smoke',
                             fg_color='white smoke',
                             border_color='white smoke')

        end_frame.pack()

    def calculate_rank_of_matrix(self):
        self.matrix_app.number_of_rows = int(self.row_size.get())
        self.matrix_app.number_of_columns = int(self.col_size.get())

        values = []
        for val in self.list_matrix:
            if val.get() != '':
                if val.get().isdigit():
                    values.append(int(val.get()))
                elif val.get().lstrip('-').isdigit():
                    values.append(int(val.get()))
                else:
                    tkinter.messagebox.showerror(
                        "Błąd danych",
                        'Wystąpił błąd w macierzy, wartość {} nie jest liczbą, zostanie ona zamieniona na 0'.format(
                            val.get()))
                    values.append(0)
            else:
                values.append(0)

        self.matrix_app.values = self.matrix_app.check_data(values)
        self.matrix_app.matrix_form = self.matrix_app.reshape_to_matrix()

        rank_of_matrix = self.matrix_app.rank_of_matrix()

        tkinter.messagebox.showinfo('Rząd macierzy', 'Rząd macierzy wynosi: {}'.format(rank_of_matrix))

    def calculate_trace_of_matrix(self):
        self.matrix_app.number_of_rows = int(self.row_size.get())
        self.matrix_app.number_of_columns = int(self.col_size.get())

        values = []
        for val in self.list_matrix:
            if val.get() != '':
                if val.get().isdigit():
                    values.append(int(val.get()))
                elif val.get().lstrip('-').isdigit():
                    values.append(int(val.get()))
                else:
                    tkinter.messagebox.showerror(
                        "Błąd danych",
                        'Wystąpił błąd w macierzy, wartość {} nie jest liczbą, zostanie ona zamieniona na 0'.format(
                            val.get()))
                    values.append(0)
            else:
                values.append(0)

        self.matrix_app.values = self.matrix_app.check_data(values)
        self.matrix_app.matrix_form = self.matrix_app.reshape_to_matrix()

        trace_of_matrix = self.matrix_app.trace_of_matrix()

        tkinter.messagebox.showinfo('Ślad macierzy', 'Ślad macierzy wynosi: {}'.format(trace_of_matrix))

    def calculate_determinant_of_the_matrix(self):
        self.matrix_app.number_of_rows = int(self.row_size.get())
        self.matrix_app.number_of_columns = int(self.col_size.get())

        values = []
        for val in self.list_matrix:
            if val.get() != '':
                if val.get().isdigit():
                    values.append(int(val.get()))
                elif val.get().lstrip('-').isdigit():
                    values.append(int(val.get()))
                else:
                    tkinter.messagebox.showerror(
                        "Błąd danych",
                        'Wystąpił błąd w macierzy, wartość {} nie jest liczbą, zostanie ona zamieniona na 0'.format(
                            val.get()))
                    values.append(0)
            else:
                values.append(0)

        if self.matrix_app.number_of_rows == self.matrix_app.number_of_columns:
            self.matrix_app = SquareMatrix(self.matrix_app.number_of_rows)
            self.matrix_app.values = self.matrix_app.check_data(values)
            self.matrix_app.matrix_form = self.matrix_app.reshape_to_matrix()
            self.matrix_app.dimension = self.matrix_app.number_of_rows
            det = self.matrix_app.calculate_determinant_of_the_matrix()
            tkinter.messagebox.showinfo('Wyznacznik macierzy', 'Wyznacznik macierzy wynosi: {}'.format(det))
        else:
            tkinter.messagebox.showerror('Błąd wielkości',
                                         'Macierz nie jest macierzą kwadratową, więc nie można obliczyć wyznacznika.')

    def calculate_inverse_matrix(self):
        self.matrix_app.number_of_rows = int(self.row_size.get())
        self.matrix_app.number_of_columns = int(self.col_size.get())

        values = []
        for val in self.list_matrix:
            if val.get() != '':
                if val.get().isdigit():
                    values.append(int(val.get()))
                elif val.get().lstrip('-').isdigit():
                    values.append(int(val.get()))
                else:
                    tkinter.messagebox.showerror(
                        "Błąd danych",
                        'Wystąpił błąd w macierzy, wartość {} nie jest liczbą, zostanie ona zamieniona na 0'.format(
                            val.get()))
                    values.append(0)
            else:
                values.append(0)

        if self.matrix_app.number_of_rows == self.matrix_app.number_of_columns:

            self.matrix_app = SquareMatrix(self.matrix_app.number_of_rows)
            self.matrix_app.values = self.matrix_app.check_data(values)
            self.matrix_app.matrix_form = self.matrix_app.reshape_to_matrix()
            self.matrix_app.dimension = self.matrix_app.number_of_rows
            inverse_matrix = self.matrix_app.matrix_inversion()
            if isinstance(inverse_matrix, str):
                tkinter.messagebox.showinfo('Komunikat', inverse_matrix)
            else:
                self.matrix_app.matrix_form = inverse_matrix
                newWindow = Toplevel(self.parent)
                newWindow.title('Wynik')
                w = 400
                h = 400

                ws = newWindow.winfo_screenwidth()
                hs = newWindow.winfo_screenheight()

                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)

                newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

                title_frame = CTkFrame(newWindow, width=400, height=50, bg_color='white smoke',
                                       fg_color='white smoke',
                                       border_color='white smoke')

                pause1_label = CTkLabel(title_frame, width=400, height=10, bg_color='white smoke',
                                        fg_color='white smoke', text_color='white smoke')
                pause1_label.pack()
                result_label = CTkLabel(title_frame, width=400, height=30, bg_color='white smoke',
                                        fg_color='white smoke', text="Macierz odwrotna")
                result_label.pack()
                pause2_label = CTkLabel(title_frame, width=400, height=10, bg_color='white smoke',
                                        fg_color='white smoke', text_color='white smoke')
                pause2_label.pack()
                title_frame.pack()

                result_frame = CTkFrame(newWindow, width=400, height=330, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')

                for x in range(int(self.row_size.get())):
                    for y in range(int(self.col_size.get())):
                        label = CTkEntry(result_frame, width=50,
                                         placeholder_text="{:.2f}".format(self.matrix_app.matrix_form[x][y]))
                        label.grid(row=x, column=y)

                result_frame.pack()

                end_frame = CTkFrame(newWindow, width=400, height=20, bg_color='white smoke',
                                     fg_color='white smoke',
                                     border_color='white smoke')

                end_frame.pack()
        else:
            tkinter.messagebox.showerror('Błąd wielkości',
                                         'Macierz nie jest macierzą kwadratową, więc nie można obliczyć macierzy odwrotnej.')


if __name__ == '__main__':
    master = Tk()
    s = SingleMatrixGui(master)
    s.mainloop()
