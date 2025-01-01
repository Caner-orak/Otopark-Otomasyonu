import pyodbc
# from OtoparkIslemleri import OtoparkIslemleri

conString = (
    r"DRIVER={SQL Server};"
    r"SERVER=.;"
    r"DATABASE=otopark_otomasyonu;"
    r"Trusted_Connection=yes;"
)

Arac_Ekle="exec AracEkle @PlakaNo = ?, @AracSahibiAdi = ?, @AracSahibiSoyadi = ?"
AracListele="exec AracListele"



def get_connection():
    return pyodbc.connect(conString)


def arac_listele():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM arac")
    return cursor.fetchall()

def arac_ekle(plaka_no, arac_sahibi_adi, arac_sahibi_soyadi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(Arac_Ekle, plaka_no, arac_sahibi_adi, arac_sahibi_soyadi)
    cursor.commit()

def arac_sil(arac_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM arac WHERE arac_id = ?",arac_id)
    cursor.commit()
    

def personel_listele():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personel")
    return cursor.fetchall()

def personel_ekle(personel_adi, personel_soyadi, personel_adres, personel_telefon, personel_email, personel_tipi, personel_maas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO personel (personel_ad, personel_soyad, personel_adresi, personel_tel_no, personel_email, personel_tipi, personel_maas) VALUES (?, ?, ?, ?, ?, ?, ?)", personel_adi, personel_soyadi, personel_adres, personel_telefon, personel_email, personel_tipi, personel_maas)
    cursor.commit()

def personel_sil(personel_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personel WHERE personel_id = ?", personel_id)
    cursor.commit()

def personel_guncelle(personel_id, personel_adi, personel_soyadi, personel_adres, personel_telefon, personel_email, personel_tipi, personel_maas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE personel SET personel_ad = CAST(? AS nvarchar(50)), personel_soyad = CAST(? AS nvarchar(50)), personel_adresi = CAST(? AS nvarchar(50)), personel_tel_no = CAST(? AS nvarchar(50)), personel_email = CAST(? AS nvarchar(50)), personel_tipi = CAST(? AS nvarchar(50)), personel_maas = CAST(? AS nvarchar(50)) WHERE personel_id = ?", personel_adi, personel_soyadi, personel_adres, personel_telefon, personel_email, personel_tipi, personel_maas, personel_id)
    cursor.commit()

def park_alanlari_goster():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM park_alanlari")
    return cursor.fetchall()

def park_alani_guncelle(park_alani_id, park_alani_adi, park_alani_durumu):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE park_alanlari SET park_alani_adi = ?, park_alani_durumu = ? WHERE park_alani_id = ?", park_alani_adi, park_alani_durumu, park_alani_id)
    cursor.commit()