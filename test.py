import datetime
import unittest

def kayit_binis_verisi(kullanici_id, oyuncak_adi, sure):
    """
    Kullanıcının biniş verisini kaydeder.
    """
    binis_zamani = datetime.datetime.now()
    return {
        "kullanici_id": kullanici_id,
        "oyuncak": oyuncak_adi,
        "sure": sure,
        "binis_zamani": binis_zamani.strftime("%Y-%m-%d %H:%M:%S")
    }

def yas_profili_ozellestirme(yas):
    """
    Kullanıcının yaşına göre hız, müzik ve süre ayarlaması yapar.
    """
    if yas < 7:
        return {"hiz": "yavas", "muzik": "cocuk", "sure": 60}
    elif 7 <= yas < 18:
        return {"hiz": "orta", "muzik": "pop", "sure": 120}
    elif 18 <= yas < 50:
        return {"hiz": "hizli", "muzik": "rock", "sure": 180}
    else:
        return {"hiz": "yavas", "muzik": "klasik", "sure": 90}

def veri_olcumu(gurultu_seviyesi, max_kapasite, mevcut_kisi):
    """
    Gürültü seviyesini ve doluluk oranını hesaplar.
    """
    doluluk_orani = (mevcut_kisi / max_kapasite) * 100
    return {
        "gurultu_seviyesi": gurultu_seviyesi,
        "doluluk_orani": round(doluluk_orani, 2)
    }

# Test Cases
class TestOyunAlani(unittest.TestCase):
    def test_kayit_binis_verisi(self):
        result = kayit_binis_verisi(101, "Roller Coaster", 120)
        self.assertEqual(result["kullanici_id"], 101)
        self.assertEqual(result["oyuncak"], "Roller Coaster")
        self.assertEqual(result["sure"], 120)
        self.assertIn("binis_zamani", result)
    
    def test_yas_profili_ozellestirme(self):
        self.assertEqual(yas_profili_ozellestirme(5), {"hiz": "yavas", "muzik": "cocuk", "sure": 60})
        self.assertEqual(yas_profili_ozellestirme(10), {"hiz": "orta", "muzik": "pop", "sure": 120})
        self.assertEqual(yas_profili_ozellestirme(25), {"hiz": "hizli", "muzik": "rock", "sure": 180})
        self.assertEqual(yas_profili_ozellestirme(60), {"hiz": "yavas", "muzik": "klasik", "sure": 90})
    
    def test_veri_olcumu(self):
        self.assertEqual(veri_olcumu(85, 100, 75), {"gurultu_seviyesi": 85, "doluluk_orani": 75.0})
        self.assertEqual(veri_olcumu(50, 200, 100), {"gurultu_seviyesi": 50, "doluluk_orani": 50.0})
        self.assertEqual(veri_olcumu(90, 150, 45), {"gurultu_seviyesi": 90, "doluluk_orani": 30.0})

if __name__ == "__main__":
    unittest.main()
