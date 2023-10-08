#Hi-Kod Veri Bilimi Atölyesi, Ödev-5
#? Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik,Fizik,Kimya notları tutulur. Kullanıcıdan isim ve ders ismi(Matematik,Fizik,Kimya) istenir ve bu bilgilere göre çıktı verilir.
ogrenciler = {
    "Oğuz": {
        "Matematik": 90,
        "Fizik": 95,
        "Kimya": 100,
    },
    "Gökçe": {
        "Matematik": 85,
        "Fizik": 90,
        "Kimya": 95,
    },
     "Buğra": {
        "Matematik": 90,
        "Fizik": 85,
        "Kimya": 95,
    },
}
ogrenci_adi = input("Lütfen Öğrenci Adını Giriniz: ")
ders_adi = input("Lütfen Notunu Öğrenmek İstediğiniz Dersin Adını Giriniz (Matematik, Fizik, Kimya): ")

if ogrenci_adi in ogrenciler and ders_adi in ogrenciler[ogrenci_adi]:
    notu = ogrenciler[ogrenci_adi][ders_adi]
    print(f"{ogrenci_adi}'nin {ders_adi} notu {notu}")
else:
    print(f"{ogrenci_adi} notu bulunamadı.")
#Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.
ogrenciler = {"ad": "Oğuz", "not": 90}
ogrenciler["not"] = 85
    print(ogrenciler)

ogrenciler["yas"] = 20

yeni_ogrenci = {}
yeni_ogrenci["ad"] = input("Öğrencinin adını girin: ")
yeni_ogrenci["not"] = int(input("Öğrencinin notunu girin: "))
ogrenciler[yeni_ogrenci["ad"]] = yeni_ogrenci

    print("Yeni öğrenci bilgileri:")
    print(yeni_ogrenci)
