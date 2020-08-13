class calisan(object):

    zam_oranı = 1.3

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@clarusway.com"
    def fullname(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)
    
    def arttir(self):
        self.maas = (self.maas * self.zam_oranı)

    def __str__(self):
        return "{}, eposta: {}".format(self.fullname(), self.eposta) 
    def __repr__(self):
        return f"ad: {self.ad} soyad:{self.soyad} maaş:{self.maas}"
    def __add__(self, other):
        return self.maas + other.maas


class gelistirici(calisan):
    def __init__(self,ad,soyad,maas, pdili):
        super().__init__(ad,soyad,maas)
        self.pdili = pdili
        self.zam_oranı = 3
class yonetici(calisan):
    def __init__(self,ad,soyad,maas, calisanlar = None):
        super().__init__(ad,soyad,maas)
        if calisanlar is None:
            self.calisanlar = []
        else: 
            self.calisanlar = calisanlar
    def elemanekle(self, eleman):
        self.calisanlar.append(eleman)
    def elemancikar(self, eleman):
        self.calisanlar.remove(eleman)
    def calisan_listele(self):
        for i in self.calisanlar:
            print(i.tamad())
    
    
personel1 = calisan("serdar","durmus",2500)
personel2 = calisan("demir","durmus",2000)
gel1 = yonetici("geliştirici", "can", 6500, "Python")
yön1 = yonetici("yönetici", "mehmet", 6500,[gel1, personel1])

print(personel1 + personel2)