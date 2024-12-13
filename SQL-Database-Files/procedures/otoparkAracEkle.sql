CREATE PROCEDURE otoparkAracEkle
	@plaka_no VARCHAR(100),
	@park_alani int,
	@arac_sahibi VARCHAR(50),
	@giris_saati smalldatetime,
	@cikis_saati smalldatetime
AS
BEGIN
	INSERT INTO otopark_islemleri(plaka_no,park_alani,arac_sahibi,giris_saati,cikis_saati)
	VALUES (@plaka_no,@park_alani,@arac_sahibi,@giris_saati,@cikis_saati);
END;
