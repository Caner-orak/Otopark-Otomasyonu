from tkinter import *
import tkinter as tk
from datetime import datetime

ana_ekran = Tk()
ana_ekran.geometry('1200x600')
ana_ekran.title('ANA EKRAN')

etiket_zaman = Label(ana_ekran, font=("Arial", 15), fg="black")
etiket_zaman.place(y=10, x=1000)

etiket_baslik = Label(ana_ekran, text="KMÜ OTOPARK OTOMASYONU", font=("Arial", 20, "bold"), fg="black")
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

def arac_yikama_penceresi():
    yikama_pencere = Toplevel(ana_ekran)
    yikama_pencere.geometry('1200x600')
    yikama_pencere.title('ARAÇ YIKAMA')
    Label(yikama_pencere, text="Araç Yıkama Hizmeti", font=("Arial", 20)).pack(pady=20)

def vale_hizmeti_penceresi():
    vale_pencere = Toplevel(ana_ekran)
    vale_pencere.geometry('1200x600')
    vale_pencere.title('VALE HİZMETİ')
    Label(vale_pencere, text="Vale Hizmeti", font=("Arial", 20)).pack(pady=20)

def personel_penceresi():
    personel_pencere = Toplevel(ana_ekran)
    personel_pencere.geometry('1200x600')
    personel_pencere.title('PERSONEL İŞLEMLERİ')
    Label(personel_pencere, text="Personel İşlemleri", font=("Arial", 20)).pack(pady=20)

def otopark_penceresi():
    otopark_pencere = Toplevel(ana_ekran)
    otopark_pencere.geometry('1200x600')
    otopark_pencere.title('OTOPARK İŞLEMLERİ')
    Label(otopark_pencere, text="Otopark İşlemleri", font=("Arial", 20)).pack(pady=20)
    button = tk.Button(otopark_pencere, 
                       text="Aracın Girişini yap", 
                       font=("Arial", 16, "bold"),  
                       bg="green", 
                       fg="white",  
                       relief="raised",
                       width=20,  
                       height=2,  
                       bd=5,  
                       activebackground="dark green",  
                       activeforeground="white",  
                       command=Arac_ekle)
    button.pack(pady=60)

def Arac_ekle():
    print("Araç eklendi")

def rapor_penceresi():
    rapor_pencere = Toplevel(ana_ekran)
    rapor_pencere.geometry('1200x600')
    rapor_pencere.title('RAPOR İŞLEMLERİ')
    Label(rapor_pencere, text="Rapor İşlemleri", font=("Arial", 20)).pack(pady=20)

def cikis_yap():
    ana_ekran.quit()

def buton_stili(buton, metin, komut, arka_plan_rengi, aktif_arka_plan_rengi):
    buton.config(text=metin,
    font=("Arial", 18, "bold"),
                 bg=arka_plan_rengi,  
                 fg="white",  
                 relief="raised",  
                 width=20,
                 height=2,
                 bd=5,
                 activebackground=aktif_arka_plan_rengi,  
                 activeforeground="white",  
                 command=komut)                

buton_arac_yikama = Button(ana_ekran)
buton_stili(buton_arac_yikama, "Araç Yıkama", arac_yikama_penceresi, "green", "dark green")

buton_vale_hizmeti = Button(ana_ekran)
buton_stili(buton_vale_hizmeti, "Vale Hizmeti", vale_hizmeti_penceresi, "blue", "dodger blue")

buton_personel_islemleri = Button(ana_ekran)
buton_stili(buton_personel_islemleri, "Personel İşlemleri", personel_penceresi, "orange", "dark orange")

buton_otopark_islemleri = Button(ana_ekran)
buton_stili(buton_otopark_islemleri, "Otopark İşlemleri", otopark_penceresi, "red", "dark red")

buton_rapor_islemleri = Button(ana_ekran)
buton_stili(buton_rapor_islemleri, "Rapor İşlemleri", rapor_penceresi, "purple", "dark violet")

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
