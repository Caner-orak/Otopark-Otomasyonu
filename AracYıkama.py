import tkinter as tk
import Veritabani as vt


class AracYıkama(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Araç Yıkama")
        self.geometry("1200x600")  

        label = tk.Label(self, text="Araç Yıkama", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        Button_yikama_ekle = tk.Button(self, text="Yıkamaya Araç Ekle", font=("Arial", 18, "bold"), bg="green", fg="white", relief="raised", activebackground="darkblue", activeforeground="white", command=self.yıkama_hizmeti_ekle)
        Button_yikama_ekle.place(x=180, y=90)

        Button_personel_listele = tk.Button(self, text="Personel Listesi", font=("Arial", 18, "bold"), bg="purple", fg="white", relief="raised", activebackground="darkblue", activeforeground="white",command=self.personel_listele)
        Button_personel_listele.place(x=875, y=90)

        Button_arac_listele = tk.Button(self, text="Araç Listele", font=("Arial", 18, "bold"), bg="blue", fg="white", relief="raised", activebackground="darkblue", activeforeground="white", command=self.arac_listele)
        Button_arac_listele.place(x=675, y=90)

        Label_plaka_no = tk.Label(self, text="Plaka No:", font=("Arial", 16, "bold"), fg="black")
        Label_plaka_no.place(x=100, y=300)

        self.Txt_plaka_no = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_plaka_no.place(x=270, y=300)

        Label_musteri_ad = tk.Label(self, text="Müşteri Adı:", font=("Arial", 16, "bold"), fg="black")
        Label_musteri_ad.place(x=100, y=350)

        self.Txt_musteri_ad = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_musteri_ad.place(x=270, y=350)

        self.Txt_bilgi_ekrani = tk.Text(self, font=("Arial", 12, "bold"), width=60, height=22)
        self.Txt_bilgi_ekrani.place(x=600, y=160)

    def yıkama_hizmeti_ekle(self):
        personel_id = self.Txt_personel_id.get()
        plaka_no = self.Txt_plaka_no.get()
        musteri_ad = self.Txt_musteri_ad.get()
        hizmet_tipi = "Yıkama Hizmeti"
        hizmet_ucreti = "100"
        vt.yıkama_hizmeti_ekle(musteri_ad, plaka_no, hizmet_tipi, hizmet_ucreti)
        hizmet_tipi = "Yıkama Hizmeti"
        hizmet_ucreti = "100"
        vt.yıkama_hizmeti_ekle(musteri_ad, plaka_no, hizmet_tipi, hizmet_ucreti)
        self.hizmetler_listele()

    def arac_listele(self):
        araclar = vt.arac_listele()
        self.Txt_bilgi_ekrani.delete("1.0", tk.END)
        for arac in araclar:
            self.Txt_bilgi_ekrani.insert(tk.END, f"Adı: {arac[0]} - Plaka No: {arac[1]} - Araç ID: {arac[2]}\n")

    def personel_listele(self):
        personeller = vt.personel_listele()
        self.Txt_bilgi_ekrani.delete("1.0", tk.END)
        for personel in personeller:
            self.Txt_bilgi_ekrani.insert(tk.END, f"Adı: {personel[0]} - Soyadı: {personel[1]} - Personel ID: {personel[2]}\n")

   