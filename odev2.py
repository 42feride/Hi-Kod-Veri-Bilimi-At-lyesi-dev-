#Hi-Kod Veri Bilimi Atölyesi, Ödev-2
#? Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri; 10000 ve altındaysa maaşından %5 kesinti olur. 25000 ve altındaysa maaşından %10 kesinti olur. 45000 ve altındaysa maaşından %25 kesinti olur. Diğer koşullarda %30 kesinti olur. Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

#Kullanıcıdan maaş bilgisi istenir:
maas = float(input("Aylık maaşınızı girin: "))
#Vergi kesintisi hesaplanır:
if maas <= 10000:
    kesinti_orani = 0.05 # %5 kesinti
elif maas <= 25000:
    kesinti_orani = 0.10 # %10 kesinti
elif maas <= 45000:
    kesinti_orani = 0.25# %25 kesinti
else: 
    kesinti_orani = 0.30 # %30 kesinti
#Vergi kesintisi hesaplanır:
vergi_kesintisi = maas * kesinti_orani
#Yeni maaş hesaplanır:
yeni_maas = maas - vergi_kesintisi
#Sonuçlar yazdırılır:
print(f"Gelir Vergisi Kesintisi: {vergi_kesintisi:.2f} TL")
print(f"Yeni Maaşınız: {yeni_maas:.2f} TL")

#? Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)
ad =(input("Lütfen Bir Kullanıcı Adı Oluşturunuz:"))
sifre =(input("Lütfen Bir Şifre Oluşturunuz:"))
if len(sifre) >= 6:
    print("Hesabınız Başarıyla Oluşturuldu!")
else:
    print("Şifre en az altı haneli olmalıdır. Lütfen daha uzun bir şifre seçiniz.")

#? Ödev-3: Bir önceki örnek geliştirilir. Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda. Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır. Koşulu sağlamıyorsa "Lütfen girdiğiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.Bunu oluştururken kullanıcı istenilen şartlarda şifre oluşturana kadar sormaya devam eder.
ad = input("Lütfen Bir Kullanıcı Adı Oluşturunuz:")
while True:
 sifre = input("Lütfen Bir Şifre Oluşturunuz:")
 if len(sifre) >= 5 and len(sifre) <= 10:
    print("Hesabınız Oluşturuldu.")
    break
else:
    print("Şifre 5 ila 10 karakter arasında olmalıdır. Tekrar Deneyin.")

#? Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir. Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. Tercihe göre kalan hak bilgisi verilir.
isim = input("İsminizi girin:")
sifre = input("Lütfen Bir Şifre Oluşturunuz:")
for deneme in range(3):
    sifre = input("Şifrenizi girin: ")
    if sifre == sifre:
        print("Giriş yapıldı.")
        break
    else:
        yanlıs_deneme_sayisi = 3 - (deneme + 1)
        if yanlıs_deneme_sayisi > 0:
            print(f"Yanlış şifre girildi! Kalan deneme hakkınız: {yanlıs_deneme_sayisi}")
        else:
            print("Üç kez yanlış şifre girdiniz. Program sonlandırılıyor.")