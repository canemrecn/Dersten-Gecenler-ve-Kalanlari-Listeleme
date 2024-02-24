with open("ornek_metin.txt") as f:
    with open("gecenler.txt", "w") as g:
        with open("kalanlar.txt", "w") as k:
            icerik = f.readlines()
            m = 0
            for satir in icerik:
                if m == 0:
                    m += 1
                    continue
                satir = satir.replace("\n", "")
                # Satırdaki boşluk sayısını ve boşluk indekslerini bulma
                boluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for karakter in satir:
                    if karakter == " ":
                        boluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                # Ad ve soyadı ayırma
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) - 1].replace("-", " ")
                # Notları ayırma
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                birinci_vize = int(notlar[0])
                ikinci_vize = int(notlar[1])
                final = int(notlar[2])
                # Ortalama hesaplama
                ortalama = birinci_vize * 0.3 + ikinci_vize * 0.3 + final * 0.4
                # Bölümü ayırma
                bolum = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[len(bosluk_indexleri) - 1]]
                # Geçenler ve kalanlar dosyalarına yazma
                if ortalama >= 70 and final >= 70:
                    g.write(ad)
                    g.write(" " * (25 - len(ad)))
                    g.write(soyad)
                    g.write(" " * (25 - len(soyad)))
                    g.write(bolum)
                    g.write(" " * (25 - len(bolum)))
                    g.write(str(round(ortalama, 1)))
                    g.write(" " * 21)
                    g.write("Geçti")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" " * (25 - len(ad)))
                    k.write(soyad)
                    k.write(" " * (25 - len(soyad)))
                    k.write(bolum)
                    k.write(" " * (25 - len(bolum)))
                    k.write(str(round(ortalama, 1)))
                    k.write(" " * 21)
                    k.write("Kaldı")
                    k.write("\n")
