import subprocess

class gethwid():

    def __init__(self):
        self.current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        self.durum = True
        self.kayit = {}


    def getserialid(self):
        print(self.current_machine_id)
        hwid.durum = False  

    def basariliPanel(self):
        print("Basarili Giris")

    def giris(self):

            kAdigiris = input("Kullanici adinizi Giriniz: ")
            kPassgiris = str(input("Sifrenizi Giriniz: "))

            if kAdigiris == self.kayit["username"] and kPassgiris == self.kayit["password"] and self.current_machine_id == self.kayit["serial"]:
                self.durum = False
                self.basariliPanel()
            else:
                print("Kullanici adi veya sifre yanlis!")
                kAdigiris = input("Kullanici adinizi Giriniz: ")
                kPassgiris = str(input("Sifrenizi Giriniz: "))

    def kayitpanel(self):
        kAdi = str(input("Kullanici adinizi Giriniz: "))
        kPass = str(input("Sifrenizi Giriniz: "))

        while kAdi.__len__() < 8 or  kAdi.__len__() > 16:
            kAdi = str(input("Kullanici adinizi Giriniz (8-16 Karakter arasinda olmalidir): "))
        while kPass.__len__() < 8 or  kPass.__len__() > 16:
            kPass = str(input("Sifrenizi Giriniz (8-16 arasinda olmalidir): "))
        self.kayit["username"] = kAdi
        self.kayit["password"] = kPass
        self.kayit["serial"] = self.current_machine_id
        print(self.kayit)

    def adminPanel(self):
        print("Daha Sonra")


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
            self.adminPanel()
        if secim == 4:
            self.cikis()


    def menu(self):
        print("1 - Giris \n 2 - Kayit \n 3 - Admin panel \n 4 - Cikis \n")

hwid = gethwid()

while hwid.durum:
    hwid.calistir()
    
