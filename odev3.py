#Hi-Kod Veri Bilimi Atölyesi, Ödev-3
#?Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

def daire_alani(pi, yaricap):
    alan = pi * yaricap ** 2
    return alan
pi_degeri = float(input("Lütfen pi degerini girin (örn: 3.14159)"))
yaricap = float(input("Lütfen dairenin yariçapını girin: "))
alan = daire_alani(pi_degeri, yaricap)
print("Dairenin Alanı:", alan)

#?Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. Format metodunu kullanılarak ekrana yazdırılır.

def faktoriyel(sayi):
    faktoriyel_degeri = 1
    for i in range(1, sayi + 1):
        faktoriyel_degeri *= i
    return faktoriyel_degeri
    
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
sonuc = faktoriyel(sayi)
print("{}! = {}".format(sayi, sonuc))

#?Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun.
 
import datetime
def yas_hesapla(dogum_yili):
    su_an = datetime.datetime.now().year
    yas = su_an - dogum_yili
    return yas
dogum_yili = int(input("Doğum yılınızı girin: "))
yas = yas_hesapla(dogum_yili)
print("Yaşınız:", yas)

#?Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin. (Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın. (Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını varsin, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.

import datetime
def yas_hesapla(dogum_yili):
    su_an = datetime.datetime.now().year
    yas = su_an - dogum_yili
    return yas
def emeklilik_durumu(isim, dogum_yili):
    yas = yas_hesapla(dogum_yili)
    emeklilik_yasi = 65

    if yas >= emeklilik_yasi:
        return f"{isim}, emekli oldunuz."
    else:
        kalan_yil = emeklilik_yasi - yas
        return f"{isim}, emekliliğinize {kalan_yil} yıl kaldı."
    
isim = input("Adınızı girin: ")
dogum_yili = int(input("Doğum yılınızı girin: "))

sonuc = emeklilik_durumu(isim, dogum_yili)
print(sonuc)