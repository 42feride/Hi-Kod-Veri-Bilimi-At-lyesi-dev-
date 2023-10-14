#Hi-Kod Veri Bilimi Atölyesi)i, Ödev-1
#?Ödev-1: Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.
sayi = 4
ondalik_sayi = float(sayi)
print(ondalik_sayi)

ondalik_sayi1 = 3.16
tam_sayi = int(ondalik_sayi1)
print(ondalik_sayi1)

sayi1 = 34
sayi_metin = str(sayi1)
print(sayi1)

#?Ödev-2: İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. Bu karşılaştırmalara mantıksal operatörler de eklenir.

# Üç isme yaş değerleri atanır
yas1 = 15
yas2 = 20
yas3 = 25
#Karşılaştırma operatörleri ile yaşları karşılaştırma
karsilastirma1 = yas1 < yas2
karsilastirma2 = yas2 > yas3
#Mantıksal operatörlerle karşılaştırmaları birleştirme
sonuc = karsilastirma1 and not karsilastirma2 #Birinci koşul doğru ve ikinci koşul yanlış mı?
#Sonucu yazdırma
print("yas1 < yas2:", karsilastirma1)
print("yas2 > yas3:", karsilastirma2)
print("sonuc:", sonuc)


#? Ödev-3: Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.
#Kullanıcıdan iki değer girmesini istenir.
sayi_1 = float(input("Birinci sayıyı girin: "))
sayi_2 = float(input("İkinci sayıyı girin: "))
#Toplama işlemi
toplam = sayi_1 + sayi_2
print("Toplama Sonucu:", toplam) 
#Çıkarma işlemi
cikarma = sayi_1 - sayi_2
print("Çıkarma Sonucu:", cikarma)
#Çarpma işlemi
carpma = sayi_1 * sayi_2
print("Çarpma Sonucu:", carpma)
#Bölme işlemi
if sayi_2 != 4:
    bolme = sayi_1 / sayi_2
    print("Bölme Sonucu:", bolme)

#?Ödev-4: Kullanıcıdan isim, yaş, şehir ve meslek bilgileri istenir ve cevapları yazdırılır.
#Kullanıcıdan bilgileri iste
isim = input("İsminizi girin: ")
yas = input("Yaşinizi girin: ")
sehir = input("Şehrinizi girin: ")
meslek = input("Mesleğinizi girin: ")
#Bilgileri ekrana yazdır
print("Merhaba, " + isim + "!")
print("Yaş: " + yas)
print("Şehir: " + sehir)
print("Meslek: " + meslek)

#?Ödev-5: "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır. İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir. İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ")İfadeyi hepsini küçük harf olacak hale çevrilir. ("hi-kod veri bilimi atölyesi") "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "02468")

#"Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır. 
degisken_adi = "Hi-Kod Veri Bilimi Atölyesi"
print(degisken_adi)
#İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.
cumle = "Hi-Kod Veri Bilimi Atölyesi"
kelimeler = cumle.split()
#Kelimeleri ekrana yazdır
for kelime in kelimeler:
    print(kelime)
#İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ")
cumle1 = "Hi-Kod Veri Bilimi Atölyesi"
kelimeler = cumle1.split()
#Kelimeleri büyük harfle yazdır
for kelime in kelimeler:
    buyuk_kelime = kelime.upper()
    print(buyuk_kelime)
#İfadelerin hepsini küçük harf olacak hale çevrilir. ("hi-kod veri bilimi atölyesi")
cumle2 = "Hi-Kod Veri Bilimi Atölyesi"
kelimeler = cumle2.split()
#Kelimeleri küçük harfle yazdır
for kelime in kelimeler:
    kucuk_kelime = kelime.lower()
    print(kucuk_kelime)

#"0123456789" ifadesindeki yalnızca çift sayıları seç. ("02468")
sayi = "0123456789"
cift_sayilar = "".join([karakter for karakter in sayi if karakter.isdigit() and int(karakter) % 2 == 0])
print(cift_sayilar)

#"0123456789" ifadesindeki yalnızca tek sayıları seç. ("13579") 
sayi1_ = "0123456789" 
tek_sayilar = ""
for karakter in sayi:
    if karakter.isdigit(): #Karakter bir rakam mı?
        rakam = int(karakter)
        if rakam % 2 != 0: #Rakam tek mi?
            tek_sayilar += karakter
print(tek_sayilar)
#todo(tek sayılarıda döngü kullanarak farklı bir versiyonda kullandım:) )
