#Hi-Kod Veri Bilimi Atölyesi, Ödev-3
#? Enumerate method araştırılır ve belirlenen örnek enumerate metodu ile yapılır.
#? Örnek: for index in range(len(meyveler)): print("{}. indexte bulunan meyve: {}".format(index,meyveler[index])

meyveler = ["elma", "armut", "çilek", "muz"]
for index, meyve in enumerate(meyveler):
    print("{}. indexte bulunan meyve: {}".format(index, meyve))

#? Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

meyveler = ["elma", "armut", "çilek", "muz"]
yeni_liste = []
for index, meyve in enumerate(meyveler):
    yeni_liste.append((index, meyve))
print(yeni_liste)