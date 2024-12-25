import tkinter as tk
from tkinter import Toplevel


class AracYıkama(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Araç Yıkama")
        self.geometry("1200x600")  

        label = tk.Label(self, text="Araç Yıkama", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        self.cikis_buton = tk.Button(self, text="Kapat", font=("Arial", 14), bg="red", fg="white", command=self.destroy)
        self.cikis_buton.place(x=0, y=0)  


        self.arac_yıkamaya_ekle=tk.Button(self,text="Araç Yıkamaya Ekle",font=("Arial",14),bg="green",fg="white")
        self.arac_yıkamaya_ekle.place(x=420,y=100)
        
        
        self.yıkama_gecmisi=tk.Button(self,text="Yıkama Geçmişi",font=("Arial",14),bg="blue",fg="white")
        self.yıkama_gecmisi.place(x=670,y=100)

        self.text_arac_sahibi_adi = tk.Entry(self, font=("Arial", 14))
        self.text_arac_sahibi_adi.pack(pady=130)
        label_arac_sahibi.place(x=317, y=362)
        label_arac_sahibi = tk.Label(self, text="Araç Sahibi:", font=("Arial", 10, "bold"), fg="black")

        self.text_plaka_no = tk.Entry(self, font=("Arial", 14))
        self.text_plaka_no.pack(pady=1)
        
        


        self.bind("<Configure>", self.buton_konumlandir)

    def buton_konumlandir(self, event=None):
        buton_genislik = self.cikis_buton.winfo_reqwidth()
        buton_yukseklik = self.cikis_buton.winfo_reqheight()
        pencere_genislik = self.winfo_width()
        pencere_yukseklik = self.winfo_height()

        x = pencere_genislik - buton_genislik - 10  
        y = pencere_yukseklik - buton_yukseklik - 10  

        self.cikis_buton.place(x=x, y=y)

        
