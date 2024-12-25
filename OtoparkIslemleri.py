import tkinter as tk
import tkinter.messagebox as messagebox
import Veritabani as vt

class OtoparkIslemleri(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Otopark İşlemleri")
        self.geometry("1200x600")

        self.txtAracSahibiAdi = tk.StringVar()
        self.txtPlakaNo = tk.StringVar()
        self.txtAracSahibiSoyadi = tk.StringVar()
        self.txtAracID = tk.StringVar()  # New variable for vehicle ID

        label = tk.Label(self, text="Otopark İşlemler", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        def arac_ekle():
            arac_sahibi = self.txtAracSahibiAdi.get()
            plaka_no = self.txtPlakaNo.get()
            arac_sahibi_soyadi = self.txtAracSahibiSoyadi.get()
            vt.arac_ekle(plaka_no, arac_sahibi, arac_sahibi_soyadi)
            araclari_goster()  # Refresh the vehicle list
            
        def arac_sil(): 
            arac_id = self.txtAracID.get()
            vt.arac_sil(arac_id)
            araclari_goster()  # Refresh the vehicle list

        AracEkleButon = tk.Button(self, text="Araç Ekle", font=("Arial", 14), bg="green", fg="white", command=lambda: arac_ekle())
        AracEkleButon.place(x=420, y=100)

        AracListele = tk.Button(self, text="Mevcut Araçları Listele", font=("Arial", 14), bg="blue", fg="white", command=lambda: vt.arac_listele())
        AracListele.place(x=570, y=100)

        AracSil = tk.Button(self, text="Araç Sil", font=("Arial", 14), bg="red", fg="white", command=arac_sil)
        AracSil.place(x=220, y=100)

        BosParkalani = tk.Button(self, text="Park Alanlarının Durumunu Göster", font=("Arial", 14), bg="orange", fg="white")
        BosParkalani.place(x=840, y=100)

        self.text_arac_sahibi_adi = tk.Entry(self, font=("Arial", 14), textvariable=self.txtAracSahibiAdi)
        self.text_arac_sahibi_adi.pack(pady=130)

        self.text_arac_sahibi_soyadi = tk.Entry(self, font=("Arial", 14), textvariable=self.txtAracSahibiAdi)
        self.text_arac_sahibi_adi.pack(pady=130)

        self.text_plaka_no = tk.Entry(self, font=("Arial", 14), textvariable=self.txtPlakaNo)
        self.text_plaka_no.pack(pady=1)

        label_arac_sahibi = tk.Label(self, text="Araç Sahibi:", font=("Arial", 10, "bold"), fg="black")
        label_arac_sahibi.place(x=317, y=362)

        label_plaka_no = tk.Label(self, text="Plaka Numarası:", font=("Arial", 10, "bold"), fg="black")
        label_plaka_no.place(x=343, y=206)

        label_arac_id = tk.Label(self, text="Silinecek Araç ID:", font=("Arial", 10, "bold"), fg="black")
        label_arac_id.place(x=343, y=250)

        self.text_arac_id = tk.Entry(self, font=("Arial", 14), textvariable=self.txtAracID)
        self.text_arac_id.place(x=480, y=250)

        self.araclar_ve_park_alanları = tk.Text(self, height=10, width=40, font=("Arial", 14))
        self.araclar_ve_park_alanları.place(x=750, y=180)

        def araclari_goster():
            araclar = vt.arac_listele()
            self.araclar_ve_park_alanları.delete(1.0, tk.END)
            for arac in araclar:
                self.araclar_ve_park_alanları.insert(tk.END, f"Araç ID: {arac[0]}, Sahibi: {arac[1]}, Plaka No: {arac[2]}\n")

        AracListele = tk.Button(self, text="Mevcut Araçları Listele", font=("Arial", 14), bg="blue", fg="white", command=araclari_goster)
        AracListele.place(x=570, y=100)

        self.cikis_buton = tk.Button(self, text="Kapat", font=("Arial", 14), bg="red", fg="white", command=self.destroy)
        self.cikis_buton.place(x=0, y=0)

        self.bind("<Configure>", self.buton_konumlandir)

    def buton_konumlandir(self, event=None):
        if event:
            pass
