while True:
    print('''1.Soru 1
2.Soru 2
3.Soru 3
4.Soru 4
5.Soru 5
6.Çıkış''')
    sec=int(input("Görüntülemek istediğiniz soru sayısını giriniz: "))

    if sec==1:
        miktar=500
        fiyat=20
        ay=0
        while True:
            ciro=miktar*fiyat
            miktar=miktar+200
            fiyat=fiyat+10
            ay=ay+1
            if ciro>500000:
                print("Şirketinizin cirosu",ay,"ay sonra",ciro,"TL olup ,500.000 Tl'nin üzerine çıkar.")
                break
    elif sec==2:
        stok=10000
        ay=0
        while stok>0:
            stok=stok-500
            stok=stok+100
            ay=ay+1
        print("Şirketinizin stokları",ay,"ay sonra 0 olacaktır.")
        print(ay,"ay sonraki mevcut stok:",stok)
    elif sec==3:
        print("Program girdiniz 0 olana kadar girdiğiniz sayıların 3'e bölümünden kalanlarını toplayacaktır.")
        toplamKalan=0
        girdi=1
        while(girdi!=0):
            girdi=int(input("Sayınızı giriniz: "))
            kalan=girdi%3
            toplamKalan=toplamKalan+kalan
            print("Şuana kadarki girdilerinizin 3'e bölümünden kalanlarının toplamı:",toplamKalan)
    elif sec==4:
        haftalik=40
        gunlukYev=90
        mesaiUcreti=gunlukYev*0.10
        aylikOdeme=haftalik*4*gunlukYev
        mesai=int(input("Haftalık mesai saatinizi giriniz: "))
        if mesai>22:
            print("Haftalık mesai saatiniz 22 saatten fazla olamaz.")
            break
        while mesai<=22:
            ekle=1
            while ekle<=mesai:
                aylikOdeme=aylikOdeme+mesaiUcreti
                ekle=ekle+1
            print("Personelin aylık ücreti:",aylikOdeme,"TL")
            break
    elif sec==5:
        uretim=200
        maxDefo=uretim*0.20
        toplamDefo=0
        gun=0
        while True:
            defolu=int(input("Günlük defolu ürün sayınızı giriniz: "))
            while defolu>maxDefo:
                print("Günlük defolu ürün sayınız %20'yi aşmıştır.%20 sınırından",defolu-maxDefo,"adet defolu ürün fazlası vardır.")
                break
            while defolu<=maxDefo:
                toplamDefo=toplamDefo+defolu
                gun=gun+1
                print(gun,"günlük toplam defolu ürün sayısı",toplamDefo,"adettir.")                
                break
    elif sec==6:
        break
    else:
        print("Hatalı giriş yaptınız!")
