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
        self.txtAracID = tk.StringVar()
        self.txtParkAlaniNo = tk.StringVar()
        self.txtParkAlaniTipi = tk.StringVar()
        self.txtParkAlaniDurumu = tk.StringVar()

        label = tk.Label(self, text="Otopark İşlemler", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        def arac_ekle():
            arac_sahibi = self.txtAracSahibiAdi.get()
            plaka_no = self.txtPlakaNo.get()
            arac_sahibi_soyadi = self.txtAracSahibiSoyadi.get()
            vt.arac_ekle(plaka_no, arac_sahibi, arac_sahibi_soyadi)
            araclari_goster()

        def arac_sil():
            arac_id = self.txtAracID.get()
            vt.arac_sil(arac_id)
            araclari_goster()

        AracEkleButon = tk.Button(self, text="Araç Ekle", font=("Arial", 14), bg="green", fg="white", command=lambda: arac_ekle())
        AracEkleButon.place(x=420, y=100)

        AracListele = tk.Button(self, text="Mevcut Araçları Listele", font=("Arial", 14), bg="blue", fg="white", command=lambda: vt.arac_listele())
        AracListele.place(x=570, y=100)

        AracSil = tk.Button(self, text="Araç Sil", font=("Arial", 14), bg="red", fg="white", command=arac_sil)
        AracSil.place(x=320, y=100)

        Park_alani_guncelle = tk.Button(self, text="Park Durumunu Güncelle", font=("Arial", 14), bg="orange", fg="white", command=self.park_alani_guncelle)
        Park_alani_guncelle.place(x=70, y=100)

        BosParkalani = tk.Button(self, text="Park Alanlarının Durumunu Göster", font=("Arial", 14), bg="orange", fg="white", command=self.park_alanlari_goster)
        BosParkalani.place(x=840, y=100)

        label_arac_sahibi = tk.Label(self, text="Araç Sahibi:", font=("Arial", 10, "bold"), fg="black")
        label_arac_sahibi.place(x=317, y=362)

        self.text_arac_sahibi_adi = tk.Entry(self, font=("Arial", 14), textvariable=self.txtAracSahibiAdi)
        self.text_arac_sahibi_adi.place(x=480, y=360)

        label_arac_sahibi_soyadi = tk.Label(self, text="Araç Sahibi Soyadı:", font=("Arial", 10, "bold"), fg="black")
        label_arac_sahibi_soyadi.place(x=317, y=400)

        self.text_arac_sahibi_soyadi = tk.Entry(self, font=("Arial", 14), textvariable=self.txtAracSahibiSoyadi)
        self.text_arac_sahibi_soyadi.place(x=480, y=400)

        label_plaka_no = tk.Label(self, text="Plaka Numarası:", font=("Arial", 10, "bold"), fg="black")
        label_plaka_no.place(x=343, y=206)

        self.text_plaka_no = tk.Entry(self, font=("Arial", 14), textvariable=self.txtPlakaNo)
        self.text_plaka_no.place(x=480, y=200)

        label_arac_id = tk.Label(self, text="Silinecek Araç ID:", font=("Arial", 10, "bold"), fg="black")
        label_arac_id.place(x=343, y=250)

        self.text_arac_id = tk.Entry(self, font=("Arial", 14), textvariable=self.txtAracID)
        self.text_arac_id.place(x=480, y=250)

        label_park_alani_no = tk.Label(self, text="Park Alanı IDı:", font=("Arial", 10, "bold"), fg="black")
        label_park_alani_no.place(x=343, y=450)

        self.text_park_alani_no = tk.Entry(self, font=("Arial", 14), textvariable=self.txtParkAlaniNo)
        self.text_park_alani_no.place(x=480, y=450)

        label_park_alani_tipi = tk.Label(self, text="Park Alanının Adı:", font=("Arial", 10, "bold"), fg="black")
        label_park_alani_tipi.place(x=343, y=490)

        self.text_park_alani_tipi = tk.Entry(self, font=("Arial", 14), textvariable=self.txtParkAlaniTipi)
        self.text_park_alani_tipi.place(x=480, y=490)

        label_park_alani_durumu = tk.Label(self, text="Alanının Durumu:", font=("Arial", 10, "bold"), fg="black")
        label_park_alani_durumu.place(x=343, y=530)

        self.text_park_alani_durumu = tk.Entry(self, font=("Arial", 14), textvariable=self.txtParkAlaniDurumu)
        self.text_park_alani_durumu.place(x=480, y=530)

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

    def park_alanlari_goster(self):
        park_alanlari = vt.park_alanlari_goster()
        self.araclar_ve_park_alanları.delete(1.0, tk.END)
        for park_alani in park_alanlari:
            self.araclar_ve_park_alanları.insert(tk.END, f"Park Alanı ID: {park_alani[0]}, Adı: {park_alani[1]}, Durumu: {park_alani[2]}\n")

    def park_alani_guncelle(self):
        park_alani_id = self.txtParkAlaniNo.get()
        park_alani_adi = self.txtParkAlaniTipi.get()
        park_alani_durumu = self.txtParkAlaniDurumu.get()
        vt.park_alani_guncelle(park_alani_id, park_alani_adi, park_alani_durumu)
        self.park_alanlari_goster()
