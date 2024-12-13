CREATE PROCEDURE aracYika
	@plaka_no VARCHAR(100),
	@arac_sahibi VARCHAR(100),
	@giris_saati smalldatetime,
	@cikis_saati smalldatetime,
	@yikama_ucreti INT,  
	@yikama_turu NVARCHAR(50),
	@yikama_id NVARCHAR(10)  
AS
BEGIN
	INSERT INTO arac_yikama(plaka_no, arac_sahibi, giris_saati, cikis_saati, yikama_ucreti, yikama_turu, yikama_id)
	VALUES (@plaka_no, @arac_sahibi, @giris_saati, @cikis_saati, @yikama_ucreti, @yikama_turu, @yikama_id);
END;
