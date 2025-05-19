from tkinter import *

class App:
    def __init__(self, root):
        self.frame1 = Frame(root)
        self.frame1.pack()
        Label(self.frame1,text="Conversão de Centímetro pra Polegadas",
        font=("Verdana","14","bold"), height=3).pack()

        Label(self.frame1,text="Centímetro(s):").pack(side=LEFT)
        self.centimetro=Entry(self.frame1)
        self.centimetro.focus_force()
        self.centimetro.pack(side=LEFT)
        Button(self.frame1,text="Converter",command=self.converter())


        Label(self.frame1,text="Polegadas(s):").pack(side=LEFT)
        self.polegada=Entry(self.frame1)
        self.centimetro.focus_force()
        self.centimetro.pack(side=LEFT)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()