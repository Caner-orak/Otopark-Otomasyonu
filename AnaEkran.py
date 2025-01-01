from tkinter import *
import tkinter as tk
from datetime import datetime
from AracYıkama import AracYıkama
from PersonelIslemleri import PersonelIslemleri
from ValeHizmetleri import ValeHizmetleri
from RaporIslemleri import RaporIslemleri
from OtoparkIslemleri import OtoparkIslemleri  


ana_ekran = Tk()
ana_ekran.geometry('1200x600')
ana_ekran.title('ANA EKRAN')

etiket_zaman = Label(ana_ekran, font=("Arial", 15), fg="black")
etiket_zaman.place(y=10, x=1000)

etiket_baslik = Label(ana_ekran, text="ÖZ ORAK OTOPARK OTOMASYONU", font=("Arial", 20, "bold"), fg="black")
etiket_baslik.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")



def zaman_guncelle():
    current_time = datetime.now().strftime("%Y-%m-%d  --  %H:%M:%S")
    etiket_zaman.config(text=current_time)
    ana_ekran.after(1000, zaman_guncelle)

def zaman_gostergesi_hizalama():
    pencere_genislik = ana_ekran.winfo_width()  
    etiket_genislik = etiket_zaman.winfo_reqwidth()  
    x_position = pencere_genislik - etiket_genislik - 10
    etiket_zaman.place(x=x_position, y=10)  
    ana_ekran.after(100, zaman_gostergesi_hizalama)

def cikis_yap():
    ana_ekran.quit()

def buton_stili(buton, metin, komut, arka_plan_rengi, aktif_arka_plan_rengi):
    buton.config(
        text=metin,
        font=("Arial", 18, "bold"),
        bg=arka_plan_rengi,  
        fg="white",  
        relief="raised",  
        width=20,
        height=2,
        bd=5,
        activebackground=aktif_arka_plan_rengi,  
        activeforeground="white",  
        command=komut
    )

def otopark_islemleri_ac():
    OtoparkIslemleri(ana_ekran)

def arac_yıkama_ac():
    AracYıkama(ana_ekran)

def personel_islemleri_ac():
    PersonelIslemleri(ana_ekran)

def vale_hzimetleri_ac():
    ValeHizmetleri(ana_ekran)

def rapor_islemleri_ac():
    RaporIslemleri(ana_ekran)

buton_arac_yikama = Button(ana_ekran)
buton_stili(buton_arac_yikama, "Araç Yıkama", arac_yıkama_ac, "green", "dark green")

buton_otopark_islemleri = Button(ana_ekran)
buton_stili(buton_otopark_islemleri, "Otopark İşlemleri", otopark_islemleri_ac, "red", "dark red")

buton_vale_hizmeti = Button(ana_ekran)
buton_stili(buton_vale_hizmeti, "Vale Hizmeti", vale_hzimetleri_ac, "blue", "dodger blue")

buton_personel_islemleri = Button(ana_ekran)
buton_stili(buton_personel_islemleri, "Personel İşlemleri", personel_islemleri_ac, "orange", "dark orange")

buton_rapor_islemleri = Button(ana_ekran)
buton_stili(buton_rapor_islemleri, "Rapor İşlemleri", rapor_islemleri_ac, "purple", "dark violet")

buton_cikis = Button(ana_ekran)
buton_stili(buton_cikis, "Çıkış", cikis_yap, "firebrick", "dark red")

buton_arac_yikama.grid(row=1, column=0, padx=50, pady=20, sticky="ew")
buton_vale_hizmeti.grid(row=1, column=1, padx=50, pady=20, sticky="ew")
buton_personel_islemleri.grid(row=2, column=0, padx=50, pady=20, sticky="ew")
buton_otopark_islemleri.grid(row=2, column=1, padx=50, pady=20, sticky="ew")
buton_rapor_islemleri.grid(row=3, column=0, padx=50, pady=20, sticky="ew")
buton_cikis.grid(row=3, column=1, padx=50, pady=20, sticky="ew")

ana_ekran.grid_columnconfigure(0, weight=1)
ana_ekran.grid_columnconfigure(1, weight=1)
ana_ekran.grid_rowconfigure(0, weight=1)
ana_ekran.grid_rowconfigure(1, weight=1)
ana_ekran.grid_rowconfigure(2, weight=1)
ana_ekran.grid_rowconfigure(3, weight=1)

zaman_guncelle()
zaman_gostergesi_hizalama()

ana_ekran.mainloop()
