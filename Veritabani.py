import pyodbc
# from OtoparkIslemleri import OtoparkIslemleri

conString = (
    r"DRIVER={SQL Server};"
    r"SERVER=DESKTOP-DEH6QNE;"
    r"DATABASE=otopark_otomasyonu;"
    r"Trusted_conneciton=yes;"
)

arac_ekle="exec AracEkle @PlakaNo = ?, @AracSahibiAdi = ?, @AracSahibiSoyadi = ?"




def get_connection():
    return pyodbc.connect(conString)


def arac_listele():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM arac")
    return cursor.fetchall()

def arac_ekle(plaka_no, arac_sahibi_adi, arac_sahibi_soyadi):
    conn = get_connection()
    conn.execute(arac_ekle, plaka_no, arac_sahibi_adi, arac_sahibi_soyadi)
    conn.commit()
    