from tkinter import Entry, Label, Frame, Tk, filedialog, Misc
from tkinter import *
import os

#listeler
from typing import Any, Union

ekleme = ["1","2","3","4","5","6","7","8","9","0","01","02","03","04","05","06","07","08","09","10","11","12","123",
"001","002","003","007","1903","1905","1907","1954","1963","1966","1919","1923","1881","2019","bjk","BJK","gs","GS","fb",
"FB","ads","ADS","ts","TS","ABC","abc","qwe","QWE","asd","ASD","SAD","sad","12345"]


isimsoyisimekleme = ["1","2","3","4","5","6","7","8","9","0","01","02","03","04","05","06","07","08","09","10","11","12","123",
"001","002","003","007","1903","1905","1907","1954","1963","1966","12345"]


klasikler = ["123456","1234567","12345678","123456789","1234567890","Qwerty","qwerty","QWERTY","Password","password","PASSWORD",
          "123abc","123qwe","666666","7777777","654321","111111","12345","987654321","9876543210","qweasd123","qweasd"]


wordpress_liste = [ 'admin','admin@123', '!admin', 'Admin', 'ADMIN', 'admin00', 'admin000', 'admin1', 'admin_1', 'Admin1', 'admin123', 'admin1234', 'admin2', 'admin256', 'Admin5', 'adminadmin', 'Administrative', 'administrator',
                    'Administrator', 'ADMINISTRATOR', 'adminpass', 'adminpwd', 'adminstat', 'adminstrator', 'adminttd', 'adminuser', 'adminview', 'admn', 'ADMN', 'tester', 'password', 'test', 'demo', 'root', 'testing', '123@admin',
                    'root@123', 'test@123', 'tester@123', 'testing@123', 'demo@123', 'panel', 'user', 'useradmin', '123admin', 'sysadmin', 'test123', 'toor', 'qwerty', 'qwerty123', 'qwerty123456', 'qwerty123456789', '123456qwerty',
                    '123456789qwerty', 'password1', 'password123', 'master', 'rootadmin', 'pass', 'pass123', 'joomla', 'abc@123', '0123456789', '012345', '12345678910', '12212112', '123321', '321123', '357159', '123654789', '321456987',
                    '1234567', '123123', '123456admin', '123456a', 'asdfghjkl123', '123asd', 'asd123', 'qwe123', 'zxc123', '123zxc', '00000', '000000', '0000000', '00000000', '111111', '1111111', '11111111', '11223344', '12341',
                    '12341234', '12345', '123454', '123456', '12345678', '1234567890', '1234admin', '123qwe', '2222',
                    '22222', '22222222', '22332323', '77777777', '88888888', 'abc123', 'ABCD', 'abd234', 'access', 'Access', 'ACCESS']
noktalama = [".","_"]

# yazilar

girisyazi = r"""
Bu program 'gl0balfox' tarafından TurkHackTeam'e yazılmıştır.Destek ve önerileriniz için www.turkhackteam.org/members/861651.html

BlackRed programi genel olarak kisiye  ozel WordList hazirlamak icin yazildiysa da,benzer amaclari kapsayacak iki modu daha bulunmaktadir.
Destek ve onerileriniz ile bu rakam arttilabilir.Konunun aldigi tesekkur sayisi,geri donusler,oneriler bunu saglayacaktir.


Mod 1 - Kisisel Mod

Birinci mod hakkinda yeterince bilgi sahibi oldugunuz insanlar icin tasarlanmistir.Benzer diger programlar gibi degil,hem kisa ve oz,
hem de kapsamli bir hizmet sunar.Menuden Kisisel Mod'u secerek ulasabilirsiniz.

Mod 2 - Tarih Modu

Ikinci mod hakkinda yeterince bilgi sahibi olmadiginiz,tercihen 30+ yaslardaki kisilere ozel sifre listesi olusturur.Kisinin adi ve anahtar
kelimelerin sonuna 1950'den 2023'e kadar tarihleri ekler.45+ yaslarda teknoloji hakkinda bilgi sahibi olmayan bir insanin sifresini WordList'e
dahil etme ihtimali neredeyse kesindir.Menuden Tarih Modu'nu secerek ulasabilirsiniz.

Mod 3 - WP Sifre Modu

Ucuncu mod 110 klasik WordPress sifresi icerir.Bu moddaki sifreler en temel WordPress sifreleridir.Menuden WP Sifre'yi secerek ulasabilirsiniz.


Mod 4 - Dork Birlestirme Modu

Dorduncu mod WordPress dork birlestirme aracidir.Daha onceden sectiginiz kelimeleri WordPress dorklariyla birlestirir.Menuden secerek ulasabilirsiniz.
"""
mod1yazi = """
Kisisel Mod,hakkinda yeterince bilgi sahibi oldugunuz kisiler
icin wordlist hazirlamaniza olanak sunar.Olusturulan wordlist,
sectiginiz dizine txt dosyasi olarak kaydedilir..

DIKKAT!

Isim-Soyisim-Anahtar kelime yazarken ozel karakter kullanma-
maya dikkat edin.Genelde sifrelerde ozel karakter bulunmaz.

Eger buyuk harf secenegini kullanacaksaniz,Isim,Soyisim ve
Anahtar kelimelerin tum harflerini kucuk yazin.Eger kullan-
mayacaksaniz yine tum harfleri kucuk yazmaniz onerilir.

Dogum Gunu/Ayi/Yili yazarken sadece rakam kullanin.Ornegin
5 Subat 2000 dogumlu biri icin Gun 05,Ay 02,Yil 2000 olmali.

Anahtar kelimeler kisinin cocugunun,esinin adi,lakabi,eger fa-
natikse tuttugu takimin adi vs. olabilir.

Butun bosluklari doldurmak zorunda degilsiniz.Ornegin kisinin
soyadini bilmiyorsaniz ya da ucuncu anahtar kelimeyi bulamadiysaniz
bos birakabilirsiniz.Kisa,oz ama etkili!


"""

mod2yazi = """
Tarih Modu,hakkinda yeterince bilgi sahibi olmadiniz,teknolojiden
anlamayan 30+ kisiler icin wordlist hazirlamaniza olanak sunar.
Olusturlan wordlist,txt dosyasi olarak kaydedilir.Bu mod,45+ yasinda,
teknolojiden anlamayan biri icin neredeyse kesin sonuc verir.
Program,kelimelerin sonuna 1950'den 2023'e kadar tarihleri ekler.

DIKKAT!

Isim-Soyisim-Anahtar kelime yazarken ozel karakter kullanma-
maya dikkat edin.Genelde sifrelerde ozel karakter bulunmaz.

Eger buyuk harf secenegini kullanacaksaniz,Isim,Soyisim ve
Anahtar kelimelerin tum harflerini kucuk yazin.Eger kullan-
mayacaksaniz yine tum harfleri kucuk yazmaniz onerilir.

Bu modda anahtar kelimeler tercihen kisinin cocugunun,
esinin adi olmali.

Butun bosluklari doldurmak zorunda degilsiniz.Ornegin kisinin
soyadini bilmiyorsaniz ya da ucuncu anahtar kelimeyi bulamadiysaniz
bos birakabilirsiniz.

"""

mod3yazi = """
WP Sifre Modu,WordPress sitelerinde kullanilar 110 klasik sifreyi icerir.WordList,sectiginiz dizine txt dosyasi olarak kaydedilir.
Bu modun gayet eksik oldugunun farkindayim.Eger bu modu gelistirmek ya da WordPress'te kullanilar sifre yapilari hakkinda beni bilgilendirmek isterseniz,
www.turkhackteam.org/members/861651.html profiline PM atabilirsiniz.
"""

mod4yazi = r"""
Dork Birlestirme Modu,WordPress dorklari icin hazinlanmis bir aractir.
Daha onceden bir WordList olarak hazirladiginiz kelimeleri sectiginiz
dorklarla birlestirir.Bu kelimeleri randomwordgenerator.com adresinden
alabilir ya da kendiniz hazirlayabilirsiniz.

Kullanmak istediginiz dorklari sectikten sonra Wordlist Sec butonuna
tiklayin.Ilk asamada dorklarla birlestirmek istediginiz kelimele dosyasini,
hemen ardindan birlestirilen dorklari nereye kaydetmek istediginizi secin.

ONERILEN DORKLAR

("author/admin") --> Paneldeki kullanici adi admin olan siteleri verir.

("Welcome The WordPress,this is your first post") --> Yakin zamanda a-
cilan siteleri verir.Sifreleri genellikle basit olur.Mod 3'teki sifre-
leri deneyebilirsiniz.

("Comment on Hello World!") --> Acildiktan sonra duzenlenmemis site-
leri verir.Mod 3'teki sifreleri deneyebilirsiniz.

("uncategorized/hello-world") --> Acildiktan sonra kategori secilmemis
siteleri verir.Mod 3'teki sifreleri deneyebilirsiniz.





"""


def mod1():
    for i in main.winfo_children():
        if i == menubar or i == modmenu or i == saydammenu:
            pass
        else:
            i.destroy()

    #algoritmalar
    def mod1alg():

        mod1sifreliste = []
        mod1buyukliste = []
        mod1fbuyukliste = []

        mod1sifreliste.clear()
        mod1buyukliste.clear()
        mod1fbuyukliste.clear()

        main.dosya_yeri = filedialog.asksaveasfilename(initialdir = "Desktop",title = "Wordlist'i Kaydet",filetypes = (("txt Files","*.txt"),("All Files","*.*")))
        mod1dosya = open(main.dosya_yeri+".txt","a")

        isim = isimentry.get()
        soyisim = soyisimentry.get()
        dogum_yil = dogum_yilentry.get()
        dogum_ay = dogum_ayentry.get()
        dogum_gun = dogum_gunentry.get()
        anahtar1 = anahtar1entry.get()
        anahtar2 = anahtar2entry.get()
        anahtar3 = anahtar3entry.get()


        #degisken kontrol

        isimdegisken = False
        soyisimdegisken = False
        dogum_yildegisken = False
        dogum_aydegisken = False
        dogum_gundegisken = False
        anahtar1degisken = False
        anahtar2degisken = False
        anahtar3degisken = False


        if len(isim) >=1:
            isimdegisken = True
        if len(soyisim) >=1:
            soyisimdegisken = True
        if len(dogum_yil) >=1:
            dogum_yildegisken = True
        if len(dogum_ay) >=1:
            dogum_aydegisken = True
        if len(dogum_gun) >=1:
            dogum_gundegisken = True
        if len(anahtar1) >=1:
            anahtar1degisken = True
        if len(anahtar2) >=1:
            anahtar2degisken = True
        if len(anahtar3) >=1:
            anahtar3degisken = True



        nokta = False
        buyuk = False
        klasik = False
        silme = False
        silme2 = False

        if noktadeger.get() == 1:
            nokta = True

        if buyukdeger.get() == 1:
            buyuk = True

        if klasikdeger.get() == 1:
            klasik = True

        if silmedeger.get() == 1:
            silme = True

        if silme2deger.get() == 1:
            silme2 = True


        def islem():

            if dogum_yildegisken == True:
                ekleme.append(dogum_yil)

            if dogum_gundegisken == True:
                ekleme.append(dogum_gun)

            if dogum_gundegisken == True and dogum_aydegisken == True and dogum_yildegisken == True:
                ekleme.append(str(dogum_gun) + str(dogum_ay) + str(dogum_yil))
                isimsoyisimekleme.append(str(dogum_gun) + str(dogum_ay) + str(dogum_yil))


            if isimdegisken == True:
                for i in ekleme:
                    mod1sifreliste.append(isim+i)
                if nokta == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1sifreliste.append(isim+a+i)
                if buyuk == True:
                    for i in ekleme:
                        mod1buyukliste.append(isim.capitalize()+i)
                        mod1fbuyukliste.append(isim.upper()+i)

                if nokta == True and buyuk == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1buyukliste.append(isim.capitalize()+a+i)
                            mod1fbuyukliste.append(isim.capitalize()+a+i)



            if soyisimdegisken == True:
                for i in ekleme:
                    mod1sifreliste.append(soyisim + i)
                if nokta == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1sifreliste.append(soyisim + a + i)
                if buyuk == True:
                    for i in ekleme:
                        mod1buyukliste.append(soyisim.capitalize() + i)
                        mod1fbuyukliste.append(soyisim.upper() + i)

                if nokta == True and buyuk == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1buyukliste.append(soyisim.capitalize() + a + i)
                            mod1fbuyukliste.append(soyisim.capitalize() + a + i)



            if isimdegisken == True and soyisimdegisken == True:
                for i in isimsoyisimekleme:
                    mod1sifreliste.append(isim + soyisim + i)
                if nokta == True:
                    for i in isimsoyisimekleme:
                        for a in noktalama:
                            mod1sifreliste.append(isim + soyisim + a + i)
                if buyuk == True:
                    for i in isimsoyisimekleme:
                        mod1buyukliste.append(isim.capitalize() + soyisim.capitalize() + i)
                        mod1fbuyukliste.append(isim.upper() + soyisim.upper() + i)

                if nokta == True and buyuk == True:
                    for i in isimsoyisimekleme:
                        for a in noktalama:
                            mod1buyukliste.append(isim.capitalize() + soyisim.capitalize() +a + i)
                            mod1fbuyukliste.append(isim.upper() + soyisim.upper() +a + i)



            if anahtar1degisken == True:
                for i in ekleme:
                    mod1sifreliste.append(anahtar1 + i)


                if nokta == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1sifreliste.append(anahtar1 + a + i)
                if buyuk == True:
                    for i in ekleme:
                        mod1buyukliste.append(anahtar1.capitalize() + i)
                        mod1fbuyukliste.append(anahtar1.upper() + i)

                if nokta == True and buyuk == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1buyukliste.append(anahtar1.capitalize() + a + i)
                            mod1fbuyukliste.append(anahtar1.upper() + a + i)



            if anahtar2degisken == True:
                for i in ekleme:
                    mod1sifreliste.append(anahtar2 + i)


                if nokta == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1sifreliste.append(anahtar2 + a + i)
                if buyuk == True:
                    for i in ekleme:
                        mod1buyukliste.append(anahtar2.capitalize() + i)
                        mod1fbuyukliste.append(anahtar2.upper() + i)

                if nokta == True and buyuk == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1buyukliste.append(anahtar2.capitalize() + a + i)
                            mod1fbuyukliste.append(anahtar2.upper() + a + i)



            if anahtar3degisken == True:
                for i in ekleme:
                    mod1sifreliste.append(anahtar3 + i)


                if nokta == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1sifreliste.append(anahtar3 + a + i)
                if buyuk == True:
                    for i in ekleme:
                        mod1buyukliste.append(anahtar3.capitalize() + i)
                        mod1fbuyukliste.append(anahtar3.upper() + i)

                if nokta == True and buyuk == True:
                    for i in ekleme:
                        for a in noktalama:
                            mod1buyukliste.append(anahtar3.capitalize() + a + i)
                            mod1fbuyukliste.append(anahtar3.upper() + a + i)

        islem()
        if klasik == True:
            for i in klasikler:
                if silme == True:
                    if len(i) < 6:
                        pass
                    else:
                        mod1dosya.write(i + "\n")
                if silme2 == True:
                    if len(i) < 8:
                        pass
                    else:
                        mod1dosya.write(i + "\n")
                if silme == False and silme2 == False:
                    mod1dosya.write(i + "\n")

        for i in mod1sifreliste:
            if mod1sifreliste.count(i) >= 2:
                for a in range(mod1sifreliste.count(i)-1):
                    mod1sifreliste.remove(i)
            else:
                if silme == True and len(i) < 6 or silme2 == True and len(i) < 8:
                    pass
                else:
                    mod1dosya.write(i + "\n")

        for i in mod1buyukliste:
            if mod1buyukliste.count(i) >= 2:
                for a in range(mod1buyukliste.count(i)-1):
                    mod1buyukliste.remove(i)
            else:
                if silme == True and len(i) < 6 or silme2 == True and len(i) < 8:
                    pass
                else:
                    mod1dosya.write(i + "\n")

        for i in mod1fbuyukliste:
            if mod1fbuyukliste.count(i) >= 2:
                for a in range(mod1fbuyukliste.count(i)-1):
                    mod1fbuyukliste.remove(i)
            else:
                if silme == True and len(i) < 6 or silme2 == True and len(i) < 8:
                    pass
                else:
                    mod1dosya.write(i + "\n")


        mod1dosya.flush()
        mod1dosya.close()
        os.startfile(main.dosya_yeri+".txt")

    solparca = Frame(bg="black")
    sagparca = Frame(bg="black")

    solparca.pack(side="left")
    sagparca.pack(side="right")

    isimyazi = Label(solparca, text="Isim:", bg="black", fg="red")
    isimyazi.grid(row=0, column=0)

    isimentry = Entry(solparca, bg="black", fg="red")
    isimentry.grid(row=0, column=1)

    soyisimyazi = Label(solparca, text="Soyisim:", bg="black", fg="red")
    soyisimyazi.grid(row=1, column=0)

    soyisimentry = Entry(solparca, bg="black", fg="red")
    soyisimentry.grid(row=1, column=1)

    # bosluk
    bosluk1 = Label(solparca, text="", bg="black")
    bosluk1.grid(row=2, column=0)

    dogum_yilyazi = Label(solparca, text="Dogum Yili(Rakamla):", bg="black", fg="red")
    dogum_yilyazi.grid(row=3, column=0)

    dogum_yilentry = Entry(solparca, bg="black", fg="red")
    dogum_yilentry.grid(row=3, column=1)

    dogum_ayyazi = Label(solparca, text="Dogum Ayi(Rakamla):", bg="black", fg="red")
    dogum_ayyazi.grid(row=4, column=0)

    dogum_ayentry = Entry(solparca, bg="black", fg="red")
    dogum_ayentry.grid(row=4, column=1)

    dogum_gunyazi = Label(solparca, text="Dogum Gunu(Rakamla):", bg="black", fg="red")
    dogum_gunyazi.grid(row=5, column=0)

    dogum_gunentry = Entry(solparca, bg="black", fg="red")
    dogum_gunentry.grid(row=5, column=1)

    # bosluk
    bosluk2 = Label(solparca, text="", bg="black")
    bosluk2.grid(row=6, column=0)

    anahtar1yazi = Label(solparca, text="Bir Anahtar Kelime:", bg="black", fg="red")
    anahtar1yazi.grid(row=7, column=0)

    anahtar1entry = Entry(solparca, bg="black", fg="red")
    anahtar1entry.grid(row=7, column=1)

    anahtar2yazi = Label(solparca, text="Bir Anahtar Kelime", bg="black", fg="red")
    anahtar2yazi.grid(row=8, column=0)

    anahtar2entry = Entry(solparca, bg="black", fg="red")
    anahtar2entry.grid(row=8, column=1)

    anahtar3yazi = Label(solparca, text="Bir Anahtar Kelime", bg="black", fg="red")
    anahtar3yazi.grid(row=9, column=0)

    anahtar3entry = Entry(solparca, bg="black", fg="red")
    anahtar3entry.grid(row=9, column=1)

    noktadeger = IntVar()
    buyukdeger = IntVar()
    klasikdeger = IntVar()
    silmedeger = IntVar()
    silme2deger = IntVar()

    noktabuton = Checkbutton(solparca, text="Noktalama(Onerilir!)", bg="black", fg="red", variable=noktadeger)
    noktabuton.grid(row=10, column=0)

    buyukbuton = Checkbutton(solparca, text="Buyuk Harf(Onerilir!)", bg="black", fg="red", variable=buyukdeger)
    buyukbuton.grid(row=10, column=1)

    klasikbuton = Checkbutton(solparca, text="Klasik Sifreler Kullanilsin Mi?", bg="black", fg="red",
                              variable=klasikdeger)
    klasikbuton.grid(row=11, column=0, columnspan=2)

    silmebuton = Checkbutton(solparca, text="6 Karakterden Az Sifreler Silinsin Mi?", bg="black", fg="red",
                             variable=silmedeger)
    silmebuton.grid(row=12, column=0, columnspan=2)

    silme2buton = Checkbutton(solparca,text="8 Karakterden Az Sifreler Silinsin Mi?", bg="black", fg="red", variable = silme2deger)
    silme2buton.grid(row=13,column=0,columnspan=2)

    bosluk3 = Label(solparca, text="", bg="black")
    bosluk3.grid(row=14, column=0)

    olustur = Button(solparca, text="Wordlist Olustur!", image=thtbutonlogo, compound=LEFT, bg="black", fg="red",
                     command=mod1alg)
    olustur.grid(row=15, column=0, columnspan=2)

    # sag parca

    resim = Label(sagparca, image=thtlogo, bg="black")
    resim.grid(row=0, column=0)

    sagyazi = Label(sagparca, text=mod1yazi, bg="black", fg="red")
    sagyazi.grid(row=0, column=1)


def ana_sayfa():
    for i in main.winfo_children():
        if i == menubar or i == modmenu or i == saydammenu:
            pass
        else:
            i.destroy()

    parca = Frame(bg="black")
    parca.pack()

    yazi = Label(parca,text=girisyazi, bg="black", fg="red", justify=CENTER)
    yazi.grid(row=0, column=0)


def mod2():
    for i in main.winfo_children():
        if i == menubar or i == modmenu or i == saydammenu:
            pass
        else:
            i.destroy()

    def mod2alg():
        main.dosya_yeri = filedialog.asksaveasfilename(initialdir = "Desktop",title = "Wordlist'i Kaydet",filetypes = (("txt Files","*.txt"),("All Files","*.*")))
        mod2dosya = open(main.dosya_yeri+".txt","a")



        sifreliste = []
        buyukliste = []
        fbuyukliste = []
        sifreliste.clear()
        buyukliste.clear()
        fbuyukliste.clear()

        isim = isimentry.get()
        soyisim = soyisimentry.get()
        anahtar1 = anahtar1entry.get()
        anahtar2 = anahtar2entry.get()
        anahtar3 = anahtar3entry.get()


        #degisken kontrol

        isimdegisken = False
        soyisimdegisken = False
        anahtar1degisken = False
        anahtar2degisken = False
        anahtar3degisken = False


        if len(isim) >=1:
            isimdegisken = True
        if len(soyisim) >=1:
            soyisimdegisken = True
        if len(anahtar1) >=1:
            anahtar1degisken = True
        if len(anahtar2) >=1:
            anahtar2degisken = True
        if len(anahtar3) >=1:
            anahtar3degisken = True



        nokta = False
        buyuk = False
        klasik = False
        silme = False
        silme2 = False

        if noktadeger.get() == 1:
            nokta = True
        if buyukdeger.get() == 1:
            buyuk = True
        if klasikdeger.get() == 1:
            klasik = True
        if silmedeger.get() == 1:
            silme = True
        if silme2deger.get() == 1:
            silme2 = True

        if klasik == True:
            for i in klasikler:
                if silme == True:
                    if len(i) < 6:
                        pass
                    else:
                        mod2dosya.write(i+"\n")
                if silme2 == True:
                    if len(i) < 8:
                        pass
                    else:
                        mod2dosya.write(i+"\n")
                if silme == False and silme2 == False:
                    mod2dosya.write(i+"\n")

        for i in range(1960,2024):
            if isimdegisken == True:
                sifreliste.append(isim+str(i))
                if buyuk == True:
                    buyukliste.append(isim.capitalize()+str(i))
                    fbuyukliste.append(isim.upper()+str(i))
                if nokta == True:
                    for a in noktalama:
                        sifreliste.append(isim+a+str(i))
                if nokta == True and buyuk == True:
                    for a in noktalama:
                        buyukliste.append(isim.capitalize()+ a +str(i))
                        fbuyukliste.append(isim.upper()+ a +str(i))

        for i in range(1960, 2024):
            if soyisimdegisken == True:
                sifreliste.append(soyisim+str(i))
                if buyuk == True:
                    buyukliste.append(soyisim.capitalize()+str(i))
                    fbuyukliste.append(soyisim.upper()+str(i))
                if nokta == True:
                    for a in noktalama:
                        sifreliste.append(soyisim + a + str(i))
                if nokta == True and buyuk == True:
                    for a in noktalama:
                        buyukliste.append(soyisim.capitalize()+ a +str(i))
                        fbuyukliste.append(soyisim.upper()+ a +str(i))

        for i in range(1960, 2024):
            if isimdegisken == True and soyisimdegisken == True:
                sifreliste.append(isim+soyisim+str(i))
                if buyuk == True:
                    buyukliste.append(isim.capitalize()+soyisim.capitalize()+str(i))
                    fbuyukliste.append(isim.upper()+soyisim.upper()+str(i))
                if nokta == True:
                    for a in noktalama:
                        sifreliste.append(isim + soyisim + a + str(i))
                if nokta == True and buyuk == True:
                    for a in noktalama:
                        buyukliste.append(isim.capitalize()+soyisim.capitalize()+a +str(i))
                        fbuyukliste.append(isim.upper()+soyisim.capitalize()+a +str(i))

        for i in range(1960, 2024):
            if anahtar1degisken == True:
                sifreliste.append(anahtar1+str(i))
                if buyuk == True:
                    buyukliste.append(anahtar1.capitalize()+str(i))
                    fbuyukliste.append(anahtar1.upper()+str(i))
                if nokta == True:
                    for a in noktalama:
                        sifreliste.append(anahtar1+a+str(i))
                if nokta == True and buyuk == True:
                    for a in noktalama:
                        buyukliste.append(anahtar1.capitalize()+ a +str(i))
                        fbuyukliste.append(anahtar1.upper()+ a +str(i))

        for i in range(1960, 2024):
            if anahtar2degisken == True:
                sifreliste.append(anahtar2+str(i))
                if buyuk == True:
                    buyukliste.append(anahtar2.capitalize()+str(i))
                    fbuyukliste.append(anahtar2.upper()+str(i))
                if nokta == True:
                    for a in noktalama:
                        sifreliste.append(anahtar2+a+str(i))
                if nokta == True and buyuk == True:
                    for a in noktalama:
                        buyukliste.append(anahtar2.capitalize()+ a +str(i))
                        fbuyukliste.append(anahtar2.upper()+ a +str(i))

        for i in range(1960, 2024):
            if anahtar3degisken == True:
                sifreliste.append(anahtar3+str(i))
                if buyuk == True:
                    buyukliste.append(anahtar3.capitalize()+str(i))
                    fbuyukliste.append(anahtar3.upper()+str(i))
                if nokta == True:
                    for a in noktalama:
                        sifreliste.append(anahtar3+a+str(i))
                if nokta == True and buyuk == True:
                    for a in noktalama:
                        buyukliste.append(anahtar3.capitalize()+ a +str(i))
                        fbuyukliste.append(anahtar3.upper()+ a +str(i))


        sifreliste.sort()

        for i in sifreliste:
            if silme == True and len(i) < 6 or silme2 == True and len(i) < 8:
                pass
            else:
                mod2dosya.write(i+"\n")



        for i in buyukliste:
            if silme == True and len(i) < 6 or silme2 == True and len(i) < 8:
                pass
            else:
                mod2dosya.write(i+"\n")

        for i in fbuyukliste:
            if silme == True and len(i) < 6 or silme2 == True and len(i) < 8:
                pass
            else:
                mod2dosya.write(i+"\n")


        mod2dosya.flush()
        mod2dosya.close()

        os.startfile(main.dosya_yeri+".txt")

    solparca = Frame(bg="black")
    solparca.pack(side="left")

    sagparca = Frame(bg="black")
    sagparca.pack(side="right")


    isimyazi = Label(solparca, text="Isim:", bg="black", fg="red")
    isimyazi.grid(row = 0,column = 0)

    isimentry= Entry(solparca, bg="black", fg="red")
    isimentry.grid(row = 0,column = 1)

    soyisimyazi = Label(solparca, text="Soyisim:", bg="black", fg="red")
    soyisimyazi.grid(row = 1,column = 0)

    soyisimentry= Entry(solparca, bg="black", fg="red")
    soyisimentry.grid(row = 1,column = 1)

    bosluk = Label(solparca, text="", bg="black", fg="red")
    bosluk.grid(row =2, column = 0)

    anahtar1yazi = Label(solparca, text="Bir Anahtar Kelime:", bg="black", fg="red")
    anahtar1yazi.grid(row = 3,column = 0)

    anahtar1entry= Entry(solparca, bg="black", fg="red")
    anahtar1entry.grid(row = 3,column = 1)

    anahtar2yazi = Label(solparca, text="Bir Anahtar Kelime:", bg="black", fg="red")
    anahtar2yazi.grid(row = 4,column = 0)

    anahtar2entry= Entry(solparca, bg="black", fg="red")
    anahtar2entry.grid(row = 4,column = 1)

    anahtar3yazi = Label(solparca, text="Bir Anahtar Kelime:", bg="black", fg="red")
    anahtar3yazi.grid(row = 5,column = 0)

    anahtar3entry= Entry(solparca, bg="black", fg="red")
    anahtar3entry.grid(row = 5,column = 1)

    bosluk = Label(solparca, text="", bg="black", fg="red")
    bosluk.grid(row =6, column = 0)

    noktadeger = IntVar()
    buyukdeger = IntVar()
    klasikdeger = IntVar()
    silmedeger = IntVar()
    silme2deger = IntVar()

    noktabuton = Checkbutton(solparca, text="Noktalama(Onerilir!)", bg="black", fg="red", variable=noktadeger)
    noktabuton.grid(row=7, column=0)

    buyukbuton = Checkbutton(solparca, text="Buyuk Harf(Onerilir!)", bg="black", fg="red", variable=buyukdeger)
    buyukbuton.grid(row=7, column=1)

    klasikbuton = Checkbutton(solparca, text="Klasik Sifreler Kullanilsin Mi?", bg="black", fg="red",variable=klasikdeger)
    klasikbuton.grid(row=8, column=0, columnspan=2)

    silmebuton = Checkbutton(solparca, text="6 Karakterden Az Sifreler Silinsin Mi?", bg="black", fg="red",variable=silmedeger)
    silmebuton.grid(row=9, column=0, columnspan=2)

    silme2buton = Checkbutton(solparca,text="8 Karakterden Az Sifreler Silinsin Mi?", bg="black", fg="red", variable = silme2deger)
    silme2buton.grid(row=10,column=0,columnspan=2)

    bosluk3 = Label(solparca, text="", bg="black")
    bosluk3.grid(row=11, column=0)

    olustur = Button(solparca, text="Wordlist Olustur!", image=thtbutonlogo, compound=LEFT, bg="black", fg="red",command=mod2alg)
    olustur.grid(row=12, column=0, columnspan=2)

    #sag parca

    resim = Label(sagparca,image=thtlogo,bg="black")
    resim.grid(row=0,column=0)

    sagyazi = Label(sagparca,text=mod2yazi,bg="black",fg="red")
    sagyazi.grid(row=0,column=1)


def mod3():

    def mod3alg():
        main.dosya_yeri = filedialog.asksaveasfilename(initialdir = "Desktop",title = "Wordlist'i Kaydet",filetypes = (("txt Files","*.txt"),("All Files","*.*")))
        mod3dosya = open(main.dosya_yeri+".txt","a")

        for a in wordpress_liste:
            mod3dosya.write(a + "\n")

        mod3dosya.flush()
        mod3dosya.close()

        os.startfile(main.dosya_yeri+".txt")

    for i in main.winfo_children():
        if i == saydammenu or i == menubar or i == modmenu:
            pass
        else:
            i.destroy()

    parca = Frame(bg="black")
    parca.pack()

    yazi = Label(parca,text=mod3yazi, bg = "black", fg ="red",justify=CENTER)
    yazi.grid(row=0,column=0)

    olustur = Button(parca,text="Wordlist Olustur!",bg="black",fg="red",image=thtbutonlogo,compound="left",justify=CENTER,command=mod3alg)
    olustur.grid(row=1,column=0)

    bosluk = Label(parca,text="",bg="black")
    bosluk.grid(row=2)

    resimyazi = Label(parca,image = thtlogo,bg="black",justify=CENTER)
    resimyazi.grid(row=3)


def mod4():
    for i in main.winfo_children():
        if i == menubar or i == saydammenu or i == modmenu:
            pass
        else:
            i.destroy()

    def mod4alg():



        main.dosya_yeri = filedialog.askopenfilename(initialdir="Desktop", title="Wordlist Sec", filetypes=(("TXT Dosyalari", "*.txt"), ("all files", "*.*")))
        mod4dosya_oku = open(main.dosya_yeri, "r").readlines()

        mod4dosya_oku = open(main.dosya_yeri, "r").readlines()
        main.dosya_yeri2 = filedialog.asksaveasfilename(initialdir="Desktop",title="Dork List'i Kaydet",filetypes=(("TXT Dosyalari","*.txt"),("Tum Dosyalar","*.*")))



        if len(main.dosya_yeri2) >= 1:
            mod4dosya = open(main.dosya_yeri2 + ".txt", "w")
            if dork1deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("Comment on Hello world!")'+i.strip()+"\n")

            if dork2deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("author/admin")' + i.strip()+"\n")
            if dork3deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("uncategorized/hello-world")' + i.strip()+"\n")
            if dork4deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("uncategorized")' + i.strip()+"\n")
            if dork5deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("Proudly powered by WordPress")' + i.strip()+"\n")
            if dork6deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("Welcome to WordPress.This is your first post.")' + i.strip()+"\n")
            if dork7deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("Just another WordPress site)' + i.strip()+"\n")
            if dork8deger.get() == 1:
                for i in mod4dosya_oku:
                    mod4dosya.write('("Mr WordPress on Hello World!")' + i.strip()+"\n")

        os.startfile(main.dosya_yeri2+".txt")


    solparca = Frame(bg="black")
    solparca.pack(side="left")

    sagparca = Frame(bg="black")
    sagparca.pack(side="right")

    altparca = Frame(solparca,bg="black")
    altparca.grid(row=500,stick="s")

    dork1deger = IntVar()
    dork2deger = IntVar()
    dork3deger = IntVar()
    dork4deger = IntVar()
    dork5deger = IntVar()
    dork6deger = IntVar()
    dork7deger = IntVar()
    dork8deger = IntVar()

    dork1 = Checkbutton(solparca,text='("Comment on Hello world!")',bg="black",fg="red",variable = dork1deger)
    dork2 = Checkbutton(solparca,text='("author/admin")',bg="black",fg="red",variable = dork2deger)
    dork3 = Checkbutton(solparca,text='("uncategorized/hello-world")',bg="black",fg="red",variable = dork3deger)
    dork4 = Checkbutton(solparca,text='("uncategorized")',bg="black",fg="red",variable = dork4deger)
    dork5 = Checkbutton(solparca,text='("Proudly powered by WordPress")',bg="black",fg="red",variable = dork5deger)
    dork6 = Checkbutton(solparca,text='("Welcome to WordPress.This is your first post.")',bg="black",fg="red",variable = dork6deger)
    dork7 = Checkbutton(solparca,text='("Just another WordPress site)',bg="black",fg="red",variable = dork7deger)
    dork8 = Checkbutton(solparca,text='("Mr WordPress on Hello World!")',bg="black",fg="red",variable = dork8deger)

    dork1.grid(row=0,column=0,sticky="w")
    dork2.grid(row=1 ,column=0,sticky="w")
    dork3.grid(row=2 ,column=0,sticky="w")
    dork4.grid(row=3 ,column=0,sticky="w")
    dork5.grid(row=4 ,column=0,sticky="w")
    dork6.grid(row=5 ,column=0,sticky="w")
    dork7.grid(row=6 ,column=0,sticky="w")
    dork8.grid(row=7 ,column=0,sticky="w")

    bosluk1 = Label(solparca,text="",bg="black")
    bosluk1.grid(row=8)

    wordlist_sec = Button(altparca,text = "Wordlist Sec",bg="black",fg="red",image=thtbutonlogo,compound="left",command=mod4alg)
    wordlist_sec.grid(row=0,column=0)

    bosluk2 = Label(altparca,text="",bg="black")
    bosluk2.grid(row=1)


    #sag

    resim = Label(sagparca,image=thtlogo,bg="black",justify="center")
    resim.grid(row=0,column=0)

    yazi = Label(sagparca,text=mod4yazi,bg="black",fg="red",justify="center")
    yazi.grid(row=0,column=1)






 ##giris

main = Tk()
main.title("BlackRed")
main.iconbitmap("icon.ico")
main.configure(bg="black")

thtlogo = PhotoImage(file ="logo.png")
thtbutonlogo = PhotoImage(file ="butonlogo.png")


main_en = int(main.winfo_screenwidth() / 2 - 485)
main_boy = int(main.winfo_screenheight() / 2 - 215)

main.geometry("970x430+{}+{}".format(main_en, main_boy))
main.maxsize("1020","420")
main.minsize("900","380")
ana_sayfa()

######################################### menu
menubar = Menu(main)
modmenu = Menu(menubar, tearoff=0)
saydammenu = Menu(menubar, tearoff=0)

modmenu.add_radiobutton(label="Kisisel Mod", command=mod1)
modmenu.add_radiobutton(label="Tarih Modu", command=mod2)
modmenu.add_radiobutton(label="WP Sifre Modu", command=mod3)
modmenu.add_radiobutton(label="Dork Birlestirme Modu", command=mod4)
modmenu.add_separator()
modmenu.add_radiobutton(label="Ana Menu", command=ana_sayfa)



def saydam():

    main.wm_attributes("-alpha","0.90")

saydammenu.add_radiobutton(label="Saydamlik",command=saydam)

menubar.add_cascade(label="Mod", menu=modmenu)
menubar.add_cascade(label="Gorunum", menu=saydammenu)

main.config(menu=menubar)



main = mainloop()
