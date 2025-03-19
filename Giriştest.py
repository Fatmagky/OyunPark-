import unittest
from datetime import datetime

class TestGiris(unittest.TestCase):

    # Abonman Girişi Testi
    def test_abonman_giris_gecerli(self):
        result = abonman_giris("12345", "abonman")
        self.assertTrue(result)
    
    def test_abonman_giris_gecersiz(self):
        result = abonman_giris("12345", "nakit")
        self.assertFalse(result)

    # Nakit Giriş Testi
    def test_nakit_giris_yeterli(self):
        result = nakit_giris(15)
        self.assertTrue(result)

    def test_nakit_giris_yetersiz(self):
        result = nakit_giris(5)
        self.assertFalse(result)

    # Kart ile Gün Boyu Oyun Testi
    def test_kartla_gunboyu_oyun_gecerli(self):
        result = kartla_gunboyu_oyun("12345", "kart")
        self.assertTrue(result)

    def test_kartla_gunboyu_oyun_gecersiz(self):
        result = kartla_gunboyu_oyun("67890", "kart")
        self.assertFalse(result)

    # Okul ve Kuruluş Girişi Testi
    def test_okul_giris(self):
        result = okul_kurulus_giris("12345", "okul")
        self.assertTrue(result)

    def test_kurulus_giris(self):
        result = okul_kurulus_giris("67890", "kurulus")
        self.assertTrue(result)

    def test_gecersiz_giris(self):
        result = okul_kurulus_giris("12345", "aile")
        self.assertFalse(result)

    # QR Kart ile Doğrulama Testi
    def test_qr_kod_dogrulama_gecerli(self):
        result = qr_kart_dogrulama("gecerliQR")
        self.assertTrue(result)

    def test_qr_kod_dogrulama_gecersiz(self):
        result = qr_kart_dogrulama("gecersizQR")
        self.assertFalse(result)

    # Kart Süresi Hatırlatma Testi
    def test_kart_suresi_hatirlatma_gecersiz(self):
        current_date = datetime.now()
        # Süresi geçmiş bir kart
        bitis_tarihi = current_date.replace(year=current_date.year - 1)
        with self.assertRaises(ValueError):  # Burada bir ValueError bekliyoruz
            kart_suresi_hatirlatma("12345", bitis_tarihi)

    def test_kart_suresi_hatirlatma_gecerli(self):
        current_date = datetime.now()
        # Geçerli bir tarih
        bitis_tarihi = current_date.replace(year=current_date.year + 1)
        kart_suresi_hatirlatma("12345", bitis_tarihi)  # Sonuç print edilecek, kontrol etmemiz gerekebilir.


if __name__ == '__main__':
    unittest.main()
