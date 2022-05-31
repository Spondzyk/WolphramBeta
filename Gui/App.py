# import tkinter as tk
# from customtkinter import *
# from tkinter import font as tkfont
#
# from Gui.DifferentiationGui import DifferentiationGui
# from Gui.DualIntegralGui import DualIntegralGui
# from Gui.DualMatrixGui import DualMatrixGui
# from Gui.IntegralGui import IntegralGui
# from Gui.LimitsGui import LimitsGui
# from Gui.LogarythmicScaleGui import LogarythmicScaleGui
# from Gui.MenuGui import MenuGui
# from Gui.MultiplePlotGui import MultiplePlotGui
# from Gui.OneVariableFunctionGui import OneVariableFunctionGui
# from Gui.SingleMatrixGui import SingleMatrixGui
# from Gui.TwoVariableFunctionGui import TwoVariableFunctionGui
#
#
# class SampleApp(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#         # for F in (
#         #         MenuGui, OneVariableFunctionGui, LogarythmicScaleGui, MultiplePlotGui, TwoVariableFunctionGui,
#         #         SingleMatrixGui,
#         #         DualMatrixGui, IntegralGui, DualIntegralGui, DifferentiationGui, LimitsGui):
#         for F in (
#                 MenuGui, OneVariableFunctionGui):
#             page_name = F.__name__
#             frame = F(master=container, controller=self)
#             self.frames[page_name] = frame
#
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("MenuGui")
#
#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()
