import subprocess
import json
import random
import sqlite3

class gethwid():

    def __init__(self):
        self.current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        self.durum = True

    def getserialid(self):
        print(self.current_machine_id)
        hwid.durum = False  

    def basariliPanel(self):
        print("Basarili Giris")

    def giris(self):

            kAdigiris = input("Kullanici adinizi Giriniz: ")
            kPassgiris = str(input("Sifrenizi Giriniz: "))

            while kAdigiris.__len__() < 8 or  kAdigiris.__len__() > 16:
                kAdigiris = str(input("Kullanici adinizi Giriniz: "))

            while kPassgiris.__len__() < 8 or  kPassgiris.__len__() > 16:
                kPassgiris = str(input("Sifrenizi Giriniz: "))

            
            with sqlite3.connect("users.db") as database:
                cursor = database.cursor()

                cursor.execute("SELECT * from users")

                for giris in cursor.fetchall():
                    if giris[0] == kAdigiris and giris[1] == kPassgiris and giris[3] == self.current_machine_id:
                        self.panel()
                    else:
                        print("Giris Basarisiz")

    def kayitpanel(self):


        currrenthwid = self.current_machine_id
        kAdi = str(input("Kullanici adinizi Giriniz: "))
        while kAdi.__len__() < 8 or  kAdi.__len__() > 16:
            kAdi = str(input("Kullanici adinizi Giriniz (8-16 Karakter arasinda olmalidir): "))


        kPass = str(input("Sifrenizi Giriniz: "))
        while kPass.__len__() < 8 or  kPass.__len__() > 16:
            kPass = str(input("Sifrenizi Giriniz (8-16 arasinda olmalidir): "))
        
        kPass2 = str(input("Sifrenizi  Tekrar Giriniz: "))
        while kPass2 != kPass:
            print("Sifreler uyusmalidir!")
            kPass = str(input("Sifrenizi Giriniz: "))
            kPass2 = str(input("Sifrenizi  Tekrar Giriniz: "))
        kMail = str(input("Mailinizi giriniz: "))
        while kMail == "":
            print("Dogru Mail turunde yaziniz")
            kMail = str(input("Mailinizi giriniz: "))
        krealPass = kPass2

        with sqlite3.connect("users.db") as database:
            cursor = database.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT,mail TEXT,hwid TEXT)")


            cursor.execute("INSERT INTO users VALUES('{}','{}','{}','{}')".format(kAdi,krealPass,kMail,currrenthwid))
        

    def panel(self):
        print("Basarili giris")

    def sifreunuttum(self):
        randomcodes = ["ACT-123213","ACT-099249","ACT-128312321","ACT-12321312345","ACT12312476"]
        selectrandomcode = random.choice(randomcodes)
        with sqlite3.connect("users.db") as database:
            cursor = database.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS codes(code TEXT)")
            cursor.execute("INSERT INTO codes VALUES('{}')".format(selectrandomcode))

        emailr = str(input("Hesabiniza bagli olan mailinizi giriniz: "))

        with sqlite3.connect("users.db") as database:
            cursor = database.cursor()
            cursor2 = database.cursor()

            cursor.execute("SELECT * from users")
            cursor2.execute("SELECT * from codes")

            for mail in cursor.fetchall():
                geneldurum = False
                if mail[2] == emailr:
                    geneldurum = True
                    print("Mailinize Gelen Kod: {}".format(selectrandomcode))
                        
            if geneldurum == True:
                    
                            gelenkod = str(input("Gelen kodu giriniz: "))
                            if gelenkod == selectrandomcode:
                                yenisifre = str(input("Girmek istediginiz yeni sifreyi giriniz : "))
                                cursor.execute("UPDATE users SET password = '{}' WHERE mail = '{}'".format(yenisifre,emailr))
                            else:
                                print("Yanlis Gelen kod")

            else:
                print("Yanlis mail adresi")


    def cikis(self):
        hwid.durum = False

    def secim(self):
        sec = int(input("Seciminizi yapiniz: "))

        while sec < 1 or sec > 4:
            sec = int(input("Seciminizi yapiniz: "))
        return sec

    def calistir(self):
        self.menu()
        secim = self.secim()


        if secim == 1:
            self.giris()
        if secim == 2:
            self.kayitpanel()
        if secim == 3:
            self.sifreunuttum()
        if secim == 4:
            self.cikis()


    def menu(self):
        print("1 - Giris \n 2 - Kayit \n 3 - Sifremi unuttum \n 4 - Cikis \n")

hwid = gethwid()

while hwid.durum:
    hwid.calistir()
    
