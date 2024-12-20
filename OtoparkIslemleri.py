import tkinter as tk
from tkinter import Toplevel
import Veritabani as vt
from tkinter import messagebox as mb


class OtoparkIslemleri(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Otopark İşlemleri")
        self.geometry("1200x600")  

        txtAracSahibiAdi = tk.StringVar()
        txtPlakaNo = tk.StringVar()
        txtAracSahibiSoyadi = tk.StringVar()


        label = tk.Label(self, text="Otopark İşlemler", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        def arac_ekle():
            arac_sahibi = txtAracSahibiAdi.get()
            plaka_no = txtPlakaNo.get()
            vt.arac_ekle("plaka_no", "arac_sahibi_adi","arac_sahibi_soyadi")
        
        # ...existing code...
        AracEkleButon = tk.Button(self, text="Araç Ekle", font=("Arial", 14), bg="green", fg="white", command=lambda :arac_ekle()) 
        AracEkleButon.place(x=420, y=100)

        AracListele = tk.Button(self, text="Mevcut Araçları Listele", font=("Arial", 14), bg="blue", fg="white") 
        AracListele.place(x=570, y=100)

        BosParkalani= tk.Button(self, text="Boş Park Alanlarını Göster", font=("Arial", 14), bg="orange", fg="white")
        BosParkalani.place(x=840, y=100)

        self.text_arac_sahibi_adi = tk.Entry(self,font=("Arial", 14), textvariable=txtAracSahibiAdi)
        self.text_arac_sahibi_adi.pack(pady=130)

        self.text_arac_sahibi_soyadi = tk.Entry(self,font=("Arial", 14), textvariable=txtAracSahibiAdi)
        self.text_arac_sahibi_adi.pack(pady=130)

        
        self.text_plaka_no = tk.Entry(self, font=("Arial", 14), textvariable=txtPlakaNo)
        self.text_plaka_no.pack(pady=1)

        label_arac_sahibi = tk.Label(self, text="Araç Sahibi:", font=("Arial", 10, "bold"), fg="black")
        label_arac_sahibi.place(x=343, y=206)

        label_plaka_no = tk.Label(self, text="Plaka Numarası:", font=("Arial", 10, "bold"), fg="black")
        label_plaka_no.place(x=317, y=362)

        self.araclar_ve_park_alanları = tk.Text(self, height=10, width=30, font=("Arial", 14))
        self.araclar_ve_park_alanları.place(x=840, y=180)
        

        self.cikis_buton = tk.Button(self, text="Kapat", font=("Arial", 14), bg="red", fg="white", command=self.destroy)
        self.cikis_buton.place(x=0, y=0)  

        self.bind("<Configure>", self.buton_konumlandir)

    def buton_konumlandir(self, event=None):
        pass
        # buton_genislik = self.cikis_buton.winfo_reqwidth()
        # buton_yukseklik = self.cikis_buton.winfo_reqheight()
        # pencere_genislik = self.winfo_width()
        # pencere_yukseklik = self.winfo_height()

        # x = pencere_genislik - buton_genislik - 10  
        # y = pencere_yukseklik - buton_yukseklik - 10  

        # self.cikis_buton.place(x=x, y=y)

