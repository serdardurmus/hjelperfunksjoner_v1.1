class calisan(object):

    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property    
    def eposta(self):
        self.email = (self.ad+self.soyad+"@clarusway.com").lower()
        return self.email
    @property
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)
    @tamad.setter
    def tamad(self, gelenisim):
        ad, soyad = gelenisim.split(" ")
        self.ad =ad
        self.soyad = soyad
    
    @tamad.deleter
    def tamad(self):
        self.ad = None
        self.soyad = None
        print("Kullanıcı bilgileri silindi")

personel1 = calisan("serdar","durmus")

personel1.tamad = "can demir"
print(personel1.ad)
print(personel1.eposta)
print(personel1.tamad)

del personel1.tamad
print(personel1.ad)
print(personel1.eposta)
print(personel1.tamad)