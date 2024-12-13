CREATE PROCEDURE Musterilistele
AS
BEGIN
    SELECT musteri_id, musteri_ad, musteri_soyad, musteri_adres, musteri_telefon_no
    FROM Musterilistele;
END;
