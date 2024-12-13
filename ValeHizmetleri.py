import tkinter as tk
from tkinter import Toplevel


class ValeHizmetleri(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Vale Hizmeti")
        self.geometry("1200x600")  

        label = tk.Label(self, text="Vale Hizmeti", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        self.cikis_buton = tk.Button(self, text="Kapat", font=("Arial", 14), bg="red", fg="white", command=self.destroy)
        self.cikis_buton.place(x=0, y=0)  

        self.bind("<Configure>", self.buton_konumlandir)

    def buton_konumlandir(self, event=None):
        buton_genislik = self.cikis_buton.winfo_reqwidth()
        buton_yukseklik = self.cikis_buton.winfo_reqheight()
        pencere_genislik = self.winfo_width()
        pencere_yukseklik = self.winfo_height()
        x = pencere_genislik - buton_genislik - 10  
        y = pencere_yukseklik - buton_yukseklik - 10  

        
        self.cikis_buton.place(x=x, y=y)

        
