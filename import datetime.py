import datetime

def kayit_binis_verisi(kullanici_id, oyuncak_adi, sure):
    """
    Kullanicinin biniş verisini kaydeder.
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
    Kullanicinin yaşina göre hiz, müzik ve süre ayarlamasi yapar.
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

# Örnek Kullanım
if __name__ == "__main__":
    print(kayit_binis_verisi(101, "Roller Coaster", 120))
    print(yas_profili_ozellestirme(25))
    print(veri_olcumu(85, 100, 75))
