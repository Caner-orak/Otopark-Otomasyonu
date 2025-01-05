import pyodbc

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

def park_alani_guncelle(park_alani_id, park_alani_durumu, park_alani_adi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE park_alanlari SET park_alani_durumu = CAST(? AS nvarchar(50)), park_alani_adi = CAST(? AS nvarchar(50)) WHERE park_alani_id = ?", park_alani_durumu, park_alani_adi, park_alani_id)
    cursor.commit()


def otopark_hizmeti_ekle(musteri_ad, plaka_no, hizmet_tipi, hizmet_ucreti):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hizmetler (musteri_ad, plaka_no, hizmet_tipi, hizmet_ucreti) VALUES (?, ?, ?, ?)", musteri_ad, plaka_no, hizmet_tipi, hizmet_ucreti)
    cursor.commit()

def vale_ekle(vale_ad, vale_soyad, vale_tel_no, vale_adres):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vale_bilgileri (vale_ad, vale_soyad, vale_tel_no, vale_adres) VALUES (?, ?, ?, ?)", vale_ad, vale_soyad, vale_tel_no, vale_adres)
    cursor.commit()

def vale_sil(vale_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vale_bilgileri WHERE vale_id = ?", vale_id)
    cursor.commit()

def vale_guncelle(vale_id, vale_ad, vale_soyad, vale_tel_no, vale_adres):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE vale_bilgileri SET vale_ad = CAST(? AS nvarchar(50)), vale_soyad = CAST(? AS nvarchar(50)), vale_tel_no = CAST(? AS nvarchar(50)), vale_adres = CAST(? AS nvarchar(50)) WHERE vale_id = ?", vale_ad, vale_soyad, vale_tel_no, vale_adres, vale_id)
    cursor.commit()

def vale_listele():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vale_bilgileri")
    return cursor.fetchall()

def vale_hizmeti_ekle(vale_id, plaka_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hizmetler (vale_id, plaka_no) VALUES (?, ?)", vale_id, plaka_no)
    cursor.commit()

def vale_hizmeti_ekle(musteri_ad, plaka_no,hizmet_tipi,hizmet_ucreti):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hizmetler (musteri_ad, plaka_no,hizmet_tipi,hizmet_ucreti) VALUES (?, ?, ?, ?)", musteri_ad, plaka_no,hizmet_tipi,hizmet_ucreti)
    cursor.commit()

def yıkama_hizmeti_ekle(musteri_ad, plaka_no,hizmet_tipi,hizmet_ucreti):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hizmetler (musteri_ad, plaka_no,hizmet_tipi,hizmet_ucreti) VALUES (?, ?, ?, ?)",musteri_ad, plaka_no,hizmet_tipi,hizmet_ucreti)
    cursor.commit()

def hizmetler_listele():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hizmetler")
    return cursor.fetchall()

def hizmet_sil(hizmet_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hizmetler WHERE hizmet_id = ?", hizmet_id)
    cursor.commit()