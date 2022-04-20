import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.pack()


root = tk.Tk()
myapp = App(root)
myapp.mainloop()
