import tkinter.messagebox
from tkinter import *

from customtkinter import *

from Program_logic.Matrix import Matrix
from Program_logic.MatrixOperations import MatrixOperations


class DualMatrixGui(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.frame_widget = None
        self.frame_result = None
        self.parent = master
        self.parent.geometry("{}x{}".format(1200, 770))
        self.parent.resizable(False, False)
        self.row_size1 = None
        self.col_size1 = None
        self.row_size2 = None
        self.col_size2 = None
        self.list_matrix1 = []
        self.list_matrix2 = []
        self.entry_operation = None
        self.create()
        self.matrix1 = Matrix()
        self.matrix2 = Matrix()
        self.matrix_operations = MatrixOperations()

    def create(self):
        self.frame_entry = CTkFrame(self.parent, width=1200, height=770, bg_color='white', fg_color='white',
                                    border_color='white')
        pause1_frame = CTkFrame(self.frame_entry, width=1200, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause1_frame.pack()
        upper_frame = CTkFrame(self.frame_entry, width=1200, height=30, bg_color='white', fg_color='white',
                               border_color='white')
        upper_frame_left = CTkFrame(upper_frame, width=400, height=30, bg_color='white', fg_color='white',
                                    border_color='white')
        label_size = CTkLabel(upper_frame_left, text='Podaj rozmiar macierzy pierwszej:', width=100, height=30,
                              bg_color='white',
                              fg_color='white')
        label_size.grid(row=0, column=0)
        self.row_size1 = CTkEntry(upper_frame_left, placeholder_text='X', width=35)
        self.row_size1.grid(row=0, column=1)
        label_x = CTkLabel(upper_frame_left, text='x', width=10, height=30)
        label_x.grid(row=0, column=2)
        self.col_size1 = CTkEntry(upper_frame_left, placeholder_text='Y', width=35)
        self.col_size1.grid(row=0, column=3)
        upper_frame_left.grid(row=0, column=0)

        upper_frame_middle = CTkFrame(upper_frame, width=800, height=30, bg_color='white', fg_color='white',
                                      border_color='white')
        upper_frame_middle.grid(row=0, column=1)

        upper_frame_middle1 = CTkFrame(upper_frame, width=800, height=30, bg_color='white', fg_color='white',
                                       border_color='white')
        upper_frame_middle1.grid(row=1, column=1)

        upper_frame_right = CTkFrame(upper_frame, width=400, height=30, bg_color='white', fg_color='white',
                                     border_color='white')
        label_size = CTkLabel(upper_frame_right, text='Podaj rozmiar macierzy drugiej:    ', width=100, height=30,
                              bg_color='white',
                              fg_color='white')
        label_size.grid(row=0, column=0)
        self.row_size2 = CTkEntry(upper_frame_right, placeholder_text='X', width=35)
        self.row_size2.grid(row=0, column=1)
        label_x = CTkLabel(upper_frame_right, text='x', width=10, height=30)
        label_x.grid(row=0, column=2)
        self.col_size2 = CTkEntry(upper_frame_right, placeholder_text='Y', width=35)
        self.col_size2.grid(row=0, column=3)
        upper_frame_right.grid(row=2, column=0)
        upper_frame.pack()

        pause2_frame = CTkFrame(self.frame_entry, width=1200, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause2_frame.pack()
        middle_frame = CTkFrame(self.frame_entry, width=1200, height=30, bg_color='white', fg_color='white',
                                border_color='white')
        accept_button = CTkButton(middle_frame, text='potwierdź', width=70, command=self.add_widget)
        accept_button.grid(row=0)
        middle_frame.pack()
        pause3_frame = CTkFrame(self.frame_entry, width=1200, height=20, bg_color='white', fg_color='white',
                                border_color='white')
        pause3_frame.pack()

        self.frame_entry.pack()

    def add_widget(self):
        if self.frame_widget is not None:
            DualMatrixGui.del_widget(self)
            self.list_matrix1.clear()
            self.list_matrix2.clear()

        self.frame_widget = CTkFrame(self.frame_entry, width=1200, height=450, bg_color='white smoke',
                                     fg_color='white smoke',
                                     border_color='white smoke')

        frame_pause = CTkFrame(self.frame_widget, width=1200, height=30, bg_color='white smoke', fg_color='white smoke',
                               border_color='white smoke')
        frame_pause.pack()

        if not self.col_size1.get().isdigit():
            tkinter.messagebox.showerror("Błąd danych",
                                         "dana wprowadzona do pola odpowiadającego za ilość kolumn macierzy 1, nie jest liczbą większą od 0")
        elif not self.row_size1.get().isdigit():
            tkinter.messagebox.showerror("Błąd danych",
                                         "dana wprowadzona do pola odpowiadającego za ilość rzędów macierzy 1, nie jest liczbą większą od 0")
        elif not self.col_size2.get().isdigit():
            tkinter.messagebox.showerror("Błąd danych",
                                         "dana wprowadzona do pola odpowiadającego za ilość kolumn macierzy 2, nie jest liczbą większą od 0")
        elif not self.row_size2.get().isdigit():
            tkinter.messagebox.showerror("Błąd danych",
                                         "dana wprowadzona do pola odpowiadającego za ilość rzędów macierzy 2, nie jest liczbą większą od 0")
        else:
            if int(self.row_size1.get()) <= 10 and int(self.row_size2.get()) <= 10 and int(
                    self.col_size1.get()) <= 10 and int(self.col_size2.get()) <= 10:

                frame_wp = CTkFrame(self.frame_widget, width=400, height=450, bg_color='white smoke',
                                    fg_color='white smoke',
                                    border_color='white smoke')

                label_m1 = CTkLabel(frame_wp, width=400, height=30, text='Macierz pierwsza')
                label_m1.grid(row=0, column=0)

                frame_matrix_left = CTkFrame(frame_wp, width=400, height=450, bg_color='white smoke',
                                             fg_color='white smoke',
                                             border_color='white smoke')
                for x in range(int(self.row_size1.get())):
                    for y in range(int(self.col_size1.get())):
                        en = CTkEntry(frame_matrix_left, width=35)
                        en.grid(row=x, column=y)
                        self.list_matrix1.append(en)

                frame_matrix_left.grid(row=1, column=0)

                frame_pause1 = CTkFrame(frame_wp, width=100, height=450, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')

                frame_pause1.grid(row=1, column=1)

                label_op = CTkLabel(frame_wp, width=50, height=30, text='Operacja')
                label_op.grid(row=0, column=2)

                frame_operation = CTkFrame(frame_wp, width=50, height=450, bg_color='white smoke',
                                           fg_color='white smoke',
                                           border_color='white smoke')

                self.entry_operation = CTkEntry(frame_operation, width=30)
                self.entry_operation.pack()

                frame_operation.grid(row=1, column=2)

                frame_matrix_right = CTkFrame(frame_wp, width=400, height=450, bg_color='white smoke',
                                              fg_color='white smoke',
                                              border_color='white smoke')
                for x in range(int(self.row_size2.get())):
                    for y in range(int(self.col_size2.get())):
                        en = CTkEntry(frame_matrix_right, width=35)
                        en.grid(row=x, column=y)
                        self.list_matrix2.append(en)

                frame_pause2 = CTkFrame(frame_wp, width=100, height=450, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')

                frame_pause2.grid(row=1, column=3)

                label_m2 = CTkLabel(frame_wp, width=400, height=30, text='Macierz druga')
                label_m2.grid(row=0, column=4)

                frame_matrix_right.grid(row=1, column=4)

                accept_button = CTkButton(frame_wp, text='oblicz', width=50, command=self.calculate)
                accept_button.grid(row=2, column=2)

                frame_last_pause = CTkFrame(frame_wp, width=400, height=50, bg_color='white smoke',
                                            fg_color='white smoke',
                                            border_color='white smoke')
                frame_last_pause.grid(row=3)
                frame_wp.pack()

                self.frame_widget.pack()

            else:
                tkinter.messagebox.showinfo("Błąd wymiarów", "Proszę wybrać wymiary do maksymalnie 10")

    def del_widget(self):
        self.frame_widget.destroy()

    def calculate(self):
        if self.entry_operation.get() != '+' and self.entry_operation.get() != '*' and self.entry_operation.get() != '-':
            tkinter.messagebox.showerror('Błąd operacji',
                                         "Podany znak operacji jest błędny lub nie jest obsługiwany, proszę użyć jednego ze znaków: '+','-','*'")
        else:

            self.matrix1.number_of_rows = int(self.row_size1.get())
            self.matrix1.number_of_columns = int(self.col_size1.get())

            self.matrix2.number_of_rows = int(self.row_size2.get())
            self.matrix2.number_of_columns = int(self.col_size2.get())

            values1 = []
            for val in self.list_matrix1:
                if val.get() != '':
                    if val.get().isdigit():
                        values1.append(int(val.get()))
                    elif val.get().lstrip('-').isdigit():
                        values1.append(int(val.get()))
                    else:
                        tkinter.messagebox.showerror(
                            "Błąd danych",
                            'Wystąpił błąd w macierzy 1, wartość {} nie jest liczbą, zostanie ona zamieniona na 0'.format(
                                val.get()))
                        values1.append(0)
                else:
                    values1.append(0)

            values2 = []
            for val in self.list_matrix2:
                if val.get() != '':
                    if val.get().isdigit():
                        values2.append(int(val.get()))
                    elif val.get().lstrip('-').isdigit():
                        values2.append(int(val.get()))
                    else:
                        tkinter.messagebox.showerror(
                            "Błąd danych",
                            'Wystąpił błąd w macierzy 2, wartość {} nie jest liczbą, zostanie ona zamieniona na 0'.format(
                                val.get()))
                        values2.append(0)
                else:
                    values2.append(0)

            self.matrix1.values = values1
            self.matrix2.values = values2

            self.matrix1.matrix_form = self.matrix1.reshape_to_matrix()
            self.matrix2.matrix_form = self.matrix2.reshape_to_matrix()

            if self.entry_operation.get() == '+':
                result = self.matrix_operations.matrix_add(self.matrix1, self.matrix2)
            elif self.entry_operation.get() == '-':
                result = self.matrix_operations.matrix_subtraction(self.matrix1, self.matrix2)
            else:
                result = self.matrix_operations.matrix_multiply(self.matrix1, self.matrix2)

            if isinstance(result, str):
                tkinter.messagebox.showerror('Błąd wymiarów', result)
            else:
                newWindow = Toplevel(self.parent)
                newWindow.title('Wynik')
                w = 400
                h = 100 + int(self.row_size1.get()) * 30

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
                                        fg_color='white smoke', text="Macierz wynikowa")
                result_label.pack()
                pause2_label = CTkLabel(title_frame, width=400, height=10, bg_color='white smoke',
                                        fg_color='white smoke', text_color='white smoke')
                pause2_label.pack()
                title_frame.pack()

                result_frame = CTkFrame(newWindow, width=400, height=h - 80, bg_color='white smoke',
                                        fg_color='white smoke',
                                        border_color='white smoke')

                for x in range(result.number_of_rows):
                    for y in range(result.number_of_columns):
                        label = CTkEntry(result_frame, width=35,
                                         placeholder_text=result.matrix_form[x][y])
                        label.grid(row=x, column=y)

                result_frame.pack()

                end_frame = CTkFrame(newWindow, width=400, height=100, bg_color='white smoke',
                                     fg_color='white smoke',
                                     border_color='white smoke')

                end_frame.pack()


if __name__ == '__main__':
    master = Tk()
    s = DualMatrixGui(master)
    s.mainloop()
