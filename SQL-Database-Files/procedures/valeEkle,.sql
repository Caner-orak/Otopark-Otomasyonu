CREATE PROCEDURE personelIslemi
	@vale_id sql_variant,
	@vale_ad nvarchar(50),
	@vale_soyad nvarchar(50),
	@vale_adres nvarchar(50),
	@vale_telefon_no nvarchar(50),  
	@plaka_no sql_variant,
	@vale_ucreti int
AS
BEGIN
	INSERT INTO vale_hizmetleri(vale_id, vale_ad, vale_soyad, vale_adres, vale_telefon_no, plaka_no,vale_ucreti)
	VALUES (@vale_id, @vale_ad, @vale_soyad, @vale_adres, @vale_telefon_no, @plaka_no,@vale_ucreti);
END;
