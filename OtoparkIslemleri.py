import tkinter as tk
from tkinter import Toplevel

class OtoparkIslemleri(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Otopark İşlemleri")
        self.geometry("1200x600")

        self.label = tk.Label(self, text="Otopark İşlemleri", font=("Arial", 18, "bold"), fg="black")
        self.label.pack(pady=20)

        self.buton_cerceve = tk.Frame(self)
        self.buton_cerceve.pack(pady=10, fill="x")

        self.arac_ekle_buton = tk.Button(self.buton_cerceve, text="Araç Ekle", font=("Arial", 14), bg="green", fg="white", command=self.arac_ekle)
        self.arac_ekle_buton.pack(side="left", padx=10, expand=True)

        self.arac_cikar_buton = tk.Button(self.buton_cerceve, text="Araç Çıkar", font=("Arial", 14), bg="blue", fg="white", command=self.arac_cikar)
        self.arac_cikar_buton.pack(side="left", padx=10, expand=True)

        self.arac_listele_buton = tk.Button(self.buton_cerceve, text="Araçları Listele", font=("Arial", 14), bg="orange", fg="white", command=self.arac_listele)
        self.arac_listele_buton.pack(side="left", padx=10, expand=True)

        self.bilgi_cerceve = tk.Frame(self)
        self.bilgi_cerceve.pack(pady=10, fill="both", expand=True)

        self.plaka_frame = tk.Frame(self.bilgi_cerceve)
        self.plaka_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.plaka_label = tk.Label(self.plaka_frame, text="Plaka Listesi", font=("Arial", 14, "bold"))
        self.plaka_label.pack(pady=5)
        self.plaka_alani = tk.Text(self.plaka_frame, font=("Arial", 12), wrap="word", height=10, width=40)
        self.plaka_alani.pack(pady=5)

        self.sahip_frame = tk.Frame(self.bilgi_cerceve)
        self.sahip_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.sahip_label = tk.Label(self.sahip_frame, text="Araç Sahipleri", font=("Arial", 14, "bold"))
        self.sahip_label.pack(pady=5)
        self.sahip_alani = tk.Text(self.sahip_frame, font=("Arial", 12), wrap="word", height=10, width=40)
        self.sahip_alani.pack(pady=5)

        self.araclar_frame = tk.Frame(self.bilgi_cerceve)
        self.araclar_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.araclar_label = tk.Label(self.araclar_frame, text="Varolan Araçlar", font=("Arial", 14, "bold"))
        self.araclar_label.pack(pady=5)
        self.araclar_alani = tk.Text(self.araclar_frame, font=("Arial", 12), wrap="word", height=10, width=40)
        self.araclar_alani.pack(pady=5)

        self.cikis_buton = tk.Button(self, text="Kapat", font=("Arial", 14), bg="red", fg="white", command=self.destroy)
        self.cikis_buton.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    def arac_ekle(self):
        arac_ekle_pencere = Toplevel(self)
        arac_ekle_pencere.title("Araç Ekle")
        arac_ekle_pencere.geometry("500x400")

        tk.Label(arac_ekle_pencere, text="Plaka No:", font=("Arial", 12)).pack(pady=10)
        plaka_entry = tk.Entry(arac_ekle_pencere, font=("Arial", 12))
        plaka_entry.pack(pady=10)

        tk.Label(arac_ekle_pencere, text="Araç Sahibi:", font=("Arial", 12)).pack(pady=10)
        sahibi_entry = tk.Entry(arac_ekle_pencere, font=("Arial", 12))
        sahibi_entry.pack(pady=10)

        tk.Label(arac_ekle_pencere, text="Park Edilecek Alan:", font=("Arial", 12)).pack(pady=10)
        park_alani_entry = tk.Entry(arac_ekle_pencere, font=("Arial", 12))
        park_alani_entry.pack(pady=10)

        tk.Label(arac_ekle_pencere, text="Boş Alanlar:", font=("Arial", 12)).pack(pady=10)
        bos_alanlar = tk.Listbox(arac_ekle_pencere, font=("Arial", 12), height=5)
        bos_alanlar.pack(pady=10)
        bos_alanlar.insert(tk.END, "Park Alanı 1")
        bos_alanlar.insert(tk.END, "Park Alanı 2")
        bos_alanlar.insert(tk.END, "Park Alanı 3")
        bos_alanlar.insert(tk.END, "Park Alanı 4")
        bos_alanlar.insert(tk.END, "Park Alanı 5")
        bos_alanlar.insert(tk.END, "Park Alanı 6")
        bos_alanlar.insert(tk.END, "Park Alanı 7")
        bos_alanlar.insert(tk.END, "Park Alanı 8")
        bos_alanlar.insert(tk.END, "Park Alanı 9")
        bos_alanlar.insert(tk.END, "Park Alanı 10")

        tk.Button(arac_ekle_pencere, text="Kaydet", font=("Arial", 12), bg="green", fg="white", command=lambda: self.kaydet_arac(plaka_entry.get(), sahibi_entry.get(), park_alani_entry.get(), bos_alanlar.get(tk.ACTIVE))).pack(pady=10)

    def kaydet_arac(self, plaka, sahibi, park_alani, bos_alan):
        print(f"Plaka: {plaka}, Sahibi: {sahibi}, Park Alanı: {park_alani}, Seçilen Boş Alan: {bos_alan}")

    def arac_cikar(self):
        pass

    def arac_listele(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    otopark = OtoparkIslemleri(master=root)
    otopark.mainloop()
