import sqlite3
import uuid
import random

def universitepanel():
    class university():
            def __init__(self):
                self.calismadurum = True




            def randomnumber(self,string_length=10):

                random = str(uuid.uuid4()) 
                random = random.upper()  
                random = random.replace("-","") 
                return random[0:string_length] 

            def ogrencikayit(self):



                with sqlite3.connect("ogrenciler.db") as ogrenciler:
                    cursor = ogrenciler.cursor()

                    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT,soyad TEXT,fakulte TEXT,bolum TEXT,numara TEXT,ogrenim TEXT,durum TEXT)")

                    print("****** BAHCESEHIR OGRENCI KAYIT SISTEMI ******")
                    ad = str(input("Ogrenci adini Giriniz: "))
                    soyad = str(input("Ogrenci soyadini Giriniz: "))
                    fakulte = str(input("Ogrencinin Fakultesini Giriniz: "))
                    bolum = str(input("Ogrencinin bolumunu giriniz: "))
                    numara = universite.randomnumber()
                    ogrenimturu = str(input("Ogrencinin Ogrenim Turunu Giriniz: "))
                    durum = str(input("Ogrencinin Durumunu giriniz: "))

                    cursor.execute("INSERT INTO ogrenciler VALUES('{}','{}','{}','{}','{}','{}','{}')".format(ad,soyad,fakulte,bolum,numara,ogrenimturu,durum))

            def ogrencigoster(self):
                with sqlite3.connect("ogrenciler.db") as ogrenciler:
                    cursor = ogrenciler.cursor()
                    cursor.execute("SELECT * from ogrenciler")
                    for silmek in cursor.fetchall():
                        print("**BILGILERI**\n AD : '{}' \n SOYAD: '{}' \n FAKULTE: '{}' \n BOLUM: '{}' \n OGRENIMTURU: '{}' \n DURUM: '{}' \n ".format(silmek[0],silmek[1],silmek[2],silmek[3],silmek[5],silmek[6]))
            
            def ogrencisil(self):

                with sqlite3.connect("ogrenciler.db") as ogrenciler:
                    cursor = ogrenciler.cursor()
                    cursor.execute("SELECT * from ogrenciler")
                    for silmek in cursor.fetchall():
                        print("Ogrenci adi: {} Ogrenci Soyadi: {} Ogrenci Numarasi: {}".format(silmek[0],silmek[1],silmek[4]))
                    sil = str(input("Kaldirmak istediginiz ogrencinin numarasini yaziniz: "))
                    cursor.execute("DELETE FROM ogrenciler WHERE numara = '{}'".format(sil))

            def ogrenciduzenle(self):

                with sqlite3.connect("ogrenciler.db") as ogrenciler:
                    cursor = ogrenciler.cursor()
                    cursor.execute("SELECT * from ogrenciler")
                    for silmek in cursor.fetchall():
                        print("Ogrenci adi: {} Ogrenci Soyadi: {} Ogrenci Numarasi: {}".format(silmek[0],silmek[1],silmek[4])) 
                    degis = str(input("Bilgisini Degistirmek istediginiz ogrencinin numarasini yaziniz: "))

                    while degis != silmek[4]:
                        degis = str(input("Bilgisini Degistirmek istediginiz ogrencinin numarasini yaziniz: "))

                    print("**BILGILERI**\n AD : '{}' \n SOYAD: '{}' \n FAKULTE: '{}' \n BOLUM: '{}' \n OGRENIMTURU: '{}' \n DURUM: '{}' \n ".format(silmek[0],silmek[1],silmek[2],silmek[3],silmek[5],silmek[6]))
                    bilgi = str(input("Secili kisinin hangi bilgilerini degistirmek istiyorsunuz? : "))

                    if bilgi == "ad" or bilgi == "AD":
                        degisecekad = str(input("Ogrencinin yeni adi: "))

                        cursor.execute("UPDATE ogrenciler SET ad = '{}' WHERE numara = '{}'".format(degisecekad,degis))
                    if bilgi == "soyad" or bilgi == "SOYAD":
                        degisecesoyad = str(input("Ogrencinin yeni soyadi: "))

                        cursor.execute("UPDATE ogrenciler SET soyad = '{}' WHERE numara = '{}'".format(degisecekad,degis))
                    if bilgi == "fakulte" or bilgi == "FAKULTE":
                        degisecefakulte = str(input("Ogrencinin yeni fakultesi: "))

                        cursor.execute("UPDATE ogrenciler SET fakulte = '{}' WHERE numara = '{}'".format(degisecekad,degis))
                    if bilgi == "bolum" or bilgi == "BOLUM":
                        degisecekbolum = str(input("Ogrencinin yeni bolumu: "))

                        cursor.execute("UPDATE ogrenciler SET bolum = '{}' WHERE numara = '{}'".format(degisecekad,degis))
                    if bilgi == "ogrenimturu" or bilgi == "OGRENIMTURU":
                        degisecektur = str(input("Ogrencinin yeni Ogrenim Turu: "))

                        cursor.execute("UPDATE ogrenciler SET ogrenimturu = '{}' WHERE numara = '{}'".format(degisecekad,degis))
                    if bilgi == "durum" or bilgi == "DURUM":
                        degisecekdurum = str(input("Ogrencinin yeni durumu: "))

                        cursor.execute("UPDATE ogrenciler SET durum = '{}' WHERE numara = '{}'".format(degisecekad,degis))

            def universitemenu(self):
                print("****** BAHCESEHIR UNIVERSITE OGRENCI DUZENLEME PROGRAMI ******")
                print("1 - Ogrenci Kaydi Yap \n 2 - Ogrencileri goster \n 3 -   Ogrencileri sil \n 4 - Ogrencileri duzenle")
            
            def universitesecim(self):
                secim = int(input("Seciminiz giriniz: "))

                while secim < 1 or secim > 4:
                    secim = int(input("Seciminiz giriniz: "))
                return secim
            def universitecalistir(self):
                self.universitemenu()
                secim = self.universitesecim()

                if secim == 1:
                    self.ogrencikayit()
                if secim == 2:
                    self.ogrencigoster()
                if secim == 3:
                    self.ogrencisil()
                if secim == 4:
                    self.ogrenciduzenle()


    universite = university()

    while universite.calismadurum:
        universite.universitecalistir()