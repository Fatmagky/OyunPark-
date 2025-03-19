from datetime import datetime, timedelta

class Raporlama:
    def __init__(self, veriler):
        self.veriler = veriler
    
    def gunluk_haftalik_rapor(self, baslangic, bitis):
        """Belirtilen tarih aralığında günlük/haftalık rapor oluşturur."""
        baslangic = datetime.strptime(baslangic, "%Y-%m-%d")
        bitis = datetime.strptime(bitis, "%Y-%m-%d")
        return [veri for veri in self.veriler if baslangic <= veri['tarih'] <= bitis]
    
    def aboneler_iptaller(self):
        """Yeni aboneleri ve iptal edilen abonelikleri listeler."""
        aboneler = [veri for veri in self.veriler if veri['tur'] == 'abone']
        iptaller = [veri for veri in self.veriler if veri['tur'] == 'iptal']
        return {"aboneler": aboneler, "iptaller": iptaller}
    
    def satis_raporu(self):
        """Satışların toplamı ve günlük bazda analizi."""
        toplam_satis = sum(veri['miktar'] for veri in self.veriler if veri['tur'] == 'satis')
        gunluk_satis = {}
        for veri in self.veriler:
            if veri['tur'] == 'satis':
                tarih = veri['tarih'].strftime("%Y-%m-%d")
                gunluk_satis[tarih] = gunluk_satis.get(tarih, 0) + veri['miktar']
        return {"toplam_satis": toplam_satis, "gunluk_satis": gunluk_satis}
    
    def program_raporu(self):
        """Programları tarih bazlı listeleyerek katılımcı sayılarını gösterir."""
        programlar = {}
        for veri in self.veriler:
            if veri['tur'] == 'program':
                tarih = veri['tarih'].strftime("%Y-%m-%d")
                if tarih not in programlar:
                    programlar[tarih] = {"etkinlikler": [], "katilimcilar": 0}
                programlar[tarih]["etkinlikler"].append(veri['ad'])
                programlar[tarih]["katilimcilar"] += veri['katilimci']
        return programlar
