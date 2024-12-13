CREATE PROCEDURE personelIslemi
	@personel_id sql_variant,
	@personel_ad nvarchar(50),
	@personel_soyad nvarchar(50),
	@personel_adres nvarchar(50),
	@personel_telefon_no nvarchar(50),  
	@personel_bolum NVARCHAR(50)  
AS
BEGIN
	INSERT INTO personel(personel_id, personel_ad, personel_soyad, personel_adres, personel_telefon_no, personel_bolum)
	VALUES (@personel_id, @personel_ad, @personel_soyad, @personel_adres, @personel_telefon_no, @personel_bolum);
END;
