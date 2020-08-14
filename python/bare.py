class sporcu():
    def __init__(self, ad, brans, altin, gumus,bronz):
        self.ad = ad 
        self.brans = brans
        self.mbronz = bronz  # public
        self._mgumus = gumus  # protected
        self.__maltin = altin  # privat

    def atlet_bilgisi(self):
        return ("Sporcu adı: {} Branşı: {}".format(atlet1.ad, atlet1.brans))
    @property
    def altin_madalya(self):
        amadalya = self.__maltin
        return amadalya

atlet1 = sporcu("ali", "100 metre",2,3,9)

print(atlet1.atlet_bilgisi())
print("Bronz madalya sayısı: ",atlet1.mbronz)
print("Bronz madalya sayısı: ",atlet1._mgumus)
print("Bronz madalya sayısı: ",atlet1.altin_madalya)