"""
Du trenger en dikt som er istiklal.txt på tyrkisk
Se nederst:
"""
with open("istiklal.txt", "r", encoding="utf-8") as file:
    result= file.readlines()

with open("istiklal.txt", "w", encoding="utf-8") as file:
    count = 0
    for i in result:
        count += 1
        if (count%4 != 0):
            file.writelines(i)
        else:
            file.writelines(i)
            file.write("\n")
with open("istiklal.txt", "r", encoding="utf-8") as file:
    print(file.read())

with open("istiklal.txt", "r+", encoding="utf-8") as file:
    result= file.readlines()
    file.write("\n")
    for i in result:
        if (i != "\n"):
            file.writelines(i)
        else:
            pass

with open("istiklal.txt", "r", encoding="utf-8") as file:
    print(file.read())

"""
istiklal.txt:

Korkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak.
Çatma, kurban olayım, çehreni ey nazlı hilal!
Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
Sana olmaz dökülen kanlarımız sonra helal...
Hakkıdır, hakk'a tapan, milletimin istiklal!
Ben ezelden beridir hür yaşadım, hür yaşarım.
Hangi çılgın bana zincir vuracakmış? Şaşarım!
Kükremiş sel gibiyim, bendimi çiğner, aşarım.
Yırtarım dağları, enginlere sığmam, taşarım.
Garbın afakını sarmışsa çelik zırhlı duvar,
Benim iman dolu göğsüm gibi serhaddim var.
Ulusun, korkma! Nasıl böyle bir imanı boğar,
'Medeniyet!' dediğin tek dişi kalmış canavar?
Arkadaş! Yurduma alçakları uğratma, sakın.
Siper et gövdeni, dursun bu hayasızca akın.
Doğacaktır sana va'dettigi günler hakk'ın...
Kim bilir, belki yarın, belki yarından da yakın.
Bastığın yerleri 'toprak!' diyerek geçme, tanı:
Düşün altında binlerce kefensiz yatanı.
Sen şehit oğlusun, incitme, yazıktır, atanı:
Verme, dünyaları alsan da, bu cennet vatanı.
Kim bu cennet vatanın uğruna olmaz ki feda?
Şuheda fışkıracak toprağı sıksan, şuheda!
Canı, cananı, bütün varımı alsın da hüda,
Etmesin tek vatanımdan beni dünyada cüda.
Ruhumun senden, ilahi, şudur ancak emeli:
Değmesin mabedimin göğsüne namahrem eli.
Bu ezanlar-ki şahadetleri dinin temeli,
Ebedi yurdumun üstünde benim inlemeli.
"""