import tkinter as tk
from tkinter import Toplevel
import Veritabani as VT


class ValeHizmetleri(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Vale Hizmeti")
        self.geometry("1200x600")  

        label = tk.Label(self, text="Vale Hizmeti", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        Button_vale_ekle = tk.Button(self, text="Vale Ekle", font=("Arial", 18, "bold"), bg="green", fg="white", relief="raised", activebackground="darkblue", activeforeground="white", command=self.vale_ekle)
        Button_vale_ekle.place(x=100, y=90)

        Button_vale_sil = tk.Button(self, text="Vale Sil", font=("Arial", 18, "bold"), bg="red", fg="white", relief="raised", activebackground="darkblue", activeforeground="white", command=self.vale_sil)
        Button_vale_sil.place(x=250, y=90)

        Button_vale_guncelle = tk.Button(self, text="Vale Güncelle", font=("Arial", 18, "bold"), bg="blue", fg="white", relief="raised",  activebackground="darkblue", activeforeground="white", command=self.vale_guncelle)
        Button_vale_guncelle.place(x=400, y=90)

        Button_vale_listele = tk.Button(self, text="Vale Listele", font=("Arial", 18, "bold"), bg="purple", fg="white", relief="raised",  activebackground="darkblue", activeforeground="white", command=self.vale_listele)
        Button_vale_listele.place(x=820, y=90)

        Button_vale_hizmeti_al = tk.Button(self, text="Hizmet Ver", font=("Arial", 18, "bold"), bg="orange", fg="white", relief="raised",  activebackground="darkblue", activeforeground="white", command=self.vale_hizmeti_ekle)
        Button_vale_hizmeti_al.place(x=650, y=90)

        Button_araclar_listele = tk.Button(self, text="Araç Listele", font=("Arial", 18, "bold"), bg="blue", fg="white", relief="raised", activebackground="darkblue", activeforeground="white", command=self.araclar_listele)
        Button_araclar_listele.place(x=1020, y=90)

        Label_vale_ad = tk.Label(self, text="Vale Adı:", font=("Arial", 16, "bold"), fg="black")
        Label_vale_ad.place(x=100, y=200)

        self.Txt_vale_ad = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_vale_ad.place(x=270, y=200)

        Label_vale_soyad = tk.Label(self, text="Vale Soyadı:", font=("Arial", 16, "bold"), fg="black")
        Label_vale_soyad.place(x=100, y=250)

        self.Txt_vale_soyad = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_vale_soyad.place(x=270, y=250)

        Label_vale_tel_no = tk.Label(self, text="Vale Tel No:", font=("Arial", 16, "bold"), fg="black")
        Label_vale_tel_no.place(x=100, y=350)

        self.Txt_vale_tel_no = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")    
        self.Txt_vale_tel_no.place(x=270, y=350)

        Label_vale_adres = tk.Label(self, text="Vale Adres:", font=("Arial", 16, "bold"), fg="black")
        Label_vale_adres.place(x=100, y=300)

        self.Txt_vale_adres = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_vale_adres.place(x=270, y=300)

        Label_vale_id = tk.Label(self, text="Vale ID:", font=("Arial", 16, "bold"), fg="black")
        Label_vale_id.place(x=100, y=400)

        self.Txt_vale_id = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_vale_id.place(x=270, y=400)

        Label_plaka_no = tk.Label(self, text="Plaka No:", font=("Arial", 16, "bold"), fg="black")
        Label_plaka_no.place(x=100, y=450)

        self.Txt_plaka_no = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_plaka_no.place(x=270, y=450)

        Label_musteri_ad = tk.Label(self, text="Müşteri Adı:", font=("Arial", 16, "bold"), fg="black")
        Label_musteri_ad.place(x=100, y=500)

        self.Txt_musteri_ad = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_musteri_ad.place(x=270, y=500)

        self.Txt_bilgi_ekrani = tk.Text(self, font=("Arial", 12, "bold"), width=60, height=22)
        self.Txt_bilgi_ekrani.place(x=600, y=160)

    def vale_ekle(self):
        vale_ad = self.Txt_vale_ad.get()
        vale_soyad = self.Txt_vale_soyad.get()
        vale_tel_no = self.Txt_vale_tel_no.get()
        vale_adres = self.Txt_vale_adres.get()
        VT.vale_ekle(vale_ad, vale_soyad, vale_tel_no, vale_adres)
        self.vale_listele()

    def vale_sil(self):
        vale_id = self.Txt_vale_id.get()
        VT.vale_sil(vale_id)
        self.vale_listele()

    def vale_guncelle(self):
        vale_id = self.Txt_vale_id.get()
        vale_ad = self.Txt_vale_ad.get()
        vale_soyad = self.Txt_vale_soyad.get()
        vale_tel_no = self.Txt_vale_tel_no.get()
        vale_adres = self.Txt_vale_adres.get()
        VT.vale_guncelle(vale_id, vale_ad, vale_soyad, vale_tel_no, vale_adres)
        self.vale_listele()

    def vale_listele(self):
        valeler = VT.vale_listele()
        self.Txt_bilgi_ekrani.delete(1.0, tk.END)
        for vale in valeler:
            vale_bilgileri = f"ID: {str(vale[0])[:50]}, Adı: {str(vale[1])[:50]}, Soyadı: {str(vale[2])[:50]}, Tel No: {str(vale[3])[:50]}, Adres: {str(vale[4])[:50]}\n"
            self.Txt_bilgi_ekrani.insert(tk.END, vale_bilgileri)

    def vale_hizmeti_ekle(self):
        musteri_ad = self.Txt_musteri_ad.get()
        plaka_no = self.Txt_plaka_no.get()
        hizmet_tipi = "Vale Hizmeti"
        hizmet_ucreti = "250"
        VT.vale_hizmeti_ekle(musteri_ad, plaka_no, hizmet_tipi, hizmet_ucreti)
        self.araclar_listele()

    def araclar_listele(self):
        araclar = VT.arac_listele()
        self.Txt_bilgi_ekrani.delete(1.0, tk.END)
        for arac in araclar:
            arac_bilgileri = f"ID: {str(arac[0])[:50]}, Sahibi: {str(arac[2])[:50]}, Plaka No: {str(arac[1])[:50]}\n"
            self.Txt_bilgi_ekrani.insert(tk.END, arac_bilgileri)