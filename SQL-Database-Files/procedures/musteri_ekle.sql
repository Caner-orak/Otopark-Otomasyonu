CREATE PROCEDURE MusteriEkle
	@musteri_ad VARCHAR(100),
	@musteri_soyad VARCHAR(100),
	@musteri_telefon_no VARCHAR(15),
	@mutseri_adres VARCHAR(255)
AS
BEGIN
	INSERT INTO musteri(musteri_ad,musteri_soyad,musteri_telefon_no,musteri_adres)
	VALUES (@musteri_ad,@musteri_soyad,@musteri_telefon_no,@mutseri_adres);
END;
