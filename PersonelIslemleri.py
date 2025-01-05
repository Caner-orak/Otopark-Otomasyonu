import tkinter as tk
from tkinter import END
import Veritabani as vt

class PersonelIslemleri(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Personel İşlemleri")
        self.geometry("1200x600") 

        label = tk.Label(self, text="Personel İşlemleri", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        self.personel_ekle_buton = tk.Button(self, text="Personel Ekle", font=("Arial", 14), bg="green", fg="white", command=self.personel_ekle)
        self.personel_ekle_buton.place(x=200, y=100)

        self.personel_sil_buton = tk.Button(self, text="Personel Sil", font=("Arial", 14), bg="red", fg="white", command=self.personel_sil)
        self.personel_sil_buton.place(x=350, y=100)

        self.personel_listele_buton = tk.Button(self, text="Personel Listele", font=("Arial", 14), bg="blue", fg="white", command=self.personel_listele)
        self.personel_listele_buton.place(x=840, y=100)

        self.personel_guncelle_buton = tk.Button(self, text="Personel Güncelle", font=("Arial", 14), bg="orange", fg="white", command=self.personel_guncelle)
        self.personel_guncelle_buton.place(x=490, y=100)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=20)

        label_personel_adi = tk.Label(form_frame, text="Personel Adı:", font=("Arial", 14))
        label_personel_adi.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        self.text_personel_adi = tk.Entry(form_frame, font=("Arial", 14))
        self.text_personel_adi.grid(row=0, column=1, padx=10, pady=5)

        label_personel_soyadi = tk.Label(form_frame, text="Personel Soyadı:", font=("Arial", 14))
        label_personel_soyadi.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.text_personel_soyadi = tk.Entry(form_frame, font=("Arial", 14))
        self.text_personel_soyadi.grid(row=1, column=1, padx=10, pady=5)

        label_personel_adres = tk.Label(form_frame, text="Personel Adres:", font=("Arial", 14))
        label_personel_adres.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        
        self.text_personel_adres = tk.Entry(form_frame, font=("Arial", 14))
        self.text_personel_adres.grid(row=2, column=1, padx=10, pady=5)

        label_personel_telefon = tk.Label(form_frame, text="Personel Telefon:", font=("Arial", 14))
        label_personel_telefon.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        
        self.text_personel_telefon = tk.Entry(form_frame, font=("Arial", 14))
        self.text_personel_telefon.grid(row=3, column=1, padx=10, pady=5)

        label_personel_email = tk.Label(form_frame, text="Personel Email:", font=("Arial", 14))
        label_personel_email.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.text_personel_email = tk.Entry(form_frame, font=("Arial", 14))
        self.text_personel_email.grid(row=4, column=1, padx=10, pady=5)

        label_personel_tipi = tk.Label(form_frame, text="Personel Tipi:", font=("Arial", 14))
        label_personel_tipi.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        
        self.text_personel_tipi = tk.Entry(form_frame, font=("Arial", 14))
        self.text_personel_tipi.grid(row=5, column=1, padx=10, pady=5)

        label_personel_maas = tk.Label(form_frame, text="Personel Maaş:", font=("Arial", 14))
        label_personel_maas.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.text_personel_maas = tk.Entry(form_frame, font=("Arial", 14))
        self.text_personel_maas.grid(row=6, column=1, padx=10, pady=5)
        

        self.text_personel_listesi = tk.Text(self, height=16, width=58, font=("Arial", 13))
        self.text_personel_listesi.place(x=650, y=200)  
        
        label_personel_listesi = tk.Label(self, text="Personel Listesi", font=("Arial", 14))
        label_personel_listesi.place(x=850, y=170)  

        label_silinecek_personel_id = tk.Label(form_frame, text="Silinecek/Güncellenecek Personel ID:", font=("Arial", 14))
        label_silinecek_personel_id.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        
        self.silinecek_personel_id = tk.Entry(form_frame, font=("Arial", 14))
        self.silinecek_personel_id.grid(row=7, column=1, padx=10, pady=5)
       
        form_frame.place(x=20, y=200)  

    
    def personel_ekle(self):
        personel_adi = self.text_personel_adi.get()
        personel_soyadi = self.text_personel_soyadi.get()
        personel_adres = self.text_personel_adres.get()
        personel_telefon = self.text_personel_telefon.get()
        personel_email = self.text_personel_email.get()
        personel_tipi = self.text_personel_tipi.get()
        personel_maas = self.text_personel_maas.get()

        vt.personel_ekle(personel_adi, personel_soyadi, personel_adres, personel_telefon, 
                         personel_email, personel_tipi, personel_maas)
        self.personel_listele()

    def personel_sil(self):
        personel_listesi = vt.personel_listele()
        personel_id = self.silinecek_personel_id.get()
        if personel_id:
            vt.personel_sil(personel_id)
            self.personel_listele()
        

    def personel_listele(self):
        personel_listesi = vt.personel_listele()
        self.text_personel_listesi.delete(1.0, tk.END)
        for personel in personel_listesi:
            self.text_personel_listesi.insert(tk.END, f"ID: {personel[0]}, Adı: {personel[1]}, Soyadı: {personel[2]}, Adres: {personel[3]}, Telefon: {personel[4]}, Email: {personel[5]}, Tipi: {personel[6]}, Maaş: {personel[7]}\n")

    def personel_guncelle(self):
        personel_id = self.silinecek_personel_id.get()
        personel_adi = self.text_personel_adi.get()
        personel_soyadi = self.text_personel_soyadi.get()
        personel_adres = self.text_personel_adres.get()
        personel_telefon = self.text_personel_telefon.get()
        personel_email = self.text_personel_email.get()
        personel_tipi = self.text_personel_tipi.get()
        personel_maas = self.text_personel_maas.get()

        if personel_id:
            vt.personel_guncelle(personel_id, personel_adi, personel_soyadi, personel_adres, 
                                 personel_telefon, personel_email, personel_tipi, personel_maas)
            self.personel_listele()

    def personel_guncelle(self):
        personel_id = self.silinecek_personel_id.get()
        personel_adi = self.text_personel_adi.get()
        personel_soyadi = self.text_personel_soyadi.get()
        personel_adres = self.text_personel_adres.get()
        personel_telefon = self.text_personel_telefon.get()
        personel_email = self.text_personel_email.get()
        personel_tipi = self.text_personel_tipi.get()
        personel_maas = self.text_personel_maas.get()

        if personel_id:
            vt.personel_guncelle(personel_id, personel_adi, personel_soyadi, personel_adres, 
                                 personel_telefon, personel_email, personel_tipi, personel_maas)
            self.personel_listele()