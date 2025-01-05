import tkinter as tk
import Veritabani as vt

class RaporIslemleri(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Rapor İşlemleri")
        self.geometry("1200x600")  

        label = tk.Label(self, text="Otopark İşlemleri", font=("Arial", 18, "bold"), fg="black")
        label.pack(pady=20)

        Button_hizmetler_listele = tk.Button(self, text="Hizmetleri Listele", font=("Arial", 18), bg="orange", fg="white", relief="raised", activebackground="darkblue", activeforeground="white", command=self.hizmetler_listele)
        Button_hizmetler_listele.place(x=590, y=90)

        Button_hizmet_sil = tk.Button(self, text="Hizmet Sil", font=("Arial", 18), bg="red", fg="white", relief="raised", activebackground="darkblue", activeforeground="white", command=self.hizmet_sil)    
        Button_hizmet_sil.place(x=400, y=90)

        self.Txt_bilgi_ekrani = tk.Text(self, font=("Arial", 12, "bold"), width=65, height=18)
        self.Txt_bilgi_ekrani.place(x=300, y=220)

        self.Txt_hizmet_id = tk.Entry(self, font=("Arial", 16, "bold"), fg="black")
        self.Txt_hizmet_id.place(x=546, y=160)

        label_hizmet_id = tk.Label(self, text="Hizmet ID:", font=("Arial", 16, "bold"), fg="black")
        label_hizmet_id.place(x=400, y=160)


    def hizmetler_listele(self):
        hizmetler = vt.hizmetler_listele()
        self.Txt_bilgi_ekrani.delete("1.0", tk.END)
        for hizmet in hizmetler:
            self.Txt_bilgi_ekrani.insert(tk.END, f"ID: {hizmet[0]} - Plaka: {hizmet[3]} - Hizmet Tipi: {hizmet[5]} - Ücreti: {hizmet[6]}\n")
    
    def hizmet_sil(self):   
        hizmet_id = self.Txt_hizmet_id.get()
        vt.hizmet_sil(hizmet_id)
        self.hizmetler_listele()