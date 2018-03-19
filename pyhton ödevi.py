#Soru1
def katmaDegerCiro(toplams,hmmad,bonarim,sevgi,sahg):
    katmaDeger=toplams-(hmmad+bonarim+sevgi+sahg)
    return katmaDeger
toplams=int(input("toplam satış miktarını giriniz:"))
hmmad=int(input("Hammadde maliyetini giriniz:"))
bonarim=int(input("Bakım onarım giderini giriniz:"))
sevgi=int(input("Sevkiyat giderlerini giriniz:"))
sahg=int(input("Satın alınan hizmet giderlerini giriniz:"))
katmaD=katmaDegerCiro(toplams,hmmad,bonarim,sevgi,sahg)
if (katmaD>1000):
    print("Yüksek")
elif (500<katmaD<999):
    print("Orta")
else:
    print("Düşük")
    
#soru2
x=170
y=50
def musterilerleCalisma(x,y):
    global musteriCalisma
    musteriCalisma=x/y
    return musteriCalisma
def musterilerleCalisma2(x,y):
    global musteriCalisma2
    musteriCalisma2=(x+50)/(y+20)
    return musteriCalisma2
def calismaSureleriFarki(musteriCalisma,musteriCalisma2):
    calismaSureF=musteriCalisma-musteriCalisma2
    print(calismaSureF)
sure1=musterilerleCalisma(x,y)
sure2=musterilerleCalisma2(x,y)
calismaSureleriFarki(sure1,sure2)
#Soru3
yazilimg=int(input("Yazılım Gelirini giriniz."))
finansmang=int(input("Finansman Gelirinizi giriniz."))
urunsatisg=int(input("Ürün satış gelirini giriniz."))
calisanma=int(input("Çalışan maaş giderlerini giriniz."))
kirag=int(input("Kira giderlerini giriniz."))
donanim=int(input("Donanım giderlerini giriniz."))
yazilimge=int(input("Yazılım gelirini giriniz."))
sponsorge=int(input("Sponsor gelirini giriniz."))
eticge=int(input("E ticaret gelirini giriniz."))
urunsatisgelir=int(input("Ürün satış gelirini giriniz."))
calisanmag=int(input("Calışan maaş giderlerini giiniz."))
kiragi=int(input("Kira giderini giriniz."))
bakim=int(input("Bakim giderini giriniz."))

def ilkAylikGelir(yazilimg,finansmang,urunsatisg):
    global ilkGelir
    ilkGelir=yazilimg+finansmang+urunsatisg
    return ilkGelir
def ilkAylikGider(calisanma,kirag,donanim):
    global ilkGider
    ilkGider=calisanma+kirag+donanim
    return ilkGider
def sonAylikGelir(yazilimge,sponsorge,eticge,urunsatisgelir):
    global sonGelir
    sonGelir=yazilimge+sponsorge+eticge+urunsatisgelir
    return sonGelir
def sonAylikGider(calisanmag,kiragi,bakim):
    global sonGider
    sonGider=calisanmag+kiragi+bakim
    return sonGider
def isletmeKari(ilkGelir,ilkGider,sonGelir,sonGider):
    kar=(ilkGelir+sonGelir)-(ilkGider+sonGider)
    if (kar>5000):
        print("İşletme çok karlı.")
    elif (1000<kar<5000):
        print("İşletme karı normal.")
    else:
        print("İşletme yeterince karda değil.")
iGelir=ilkAylikGelir(yazilimg,finansmang,urunsatisg)
iGider=ilkAylikGider(calisanma,kirag,donanim)
sGelir=sonAylikGelir(yazilimge,sponsorge,eticge,urunsatisgelir)
sGider=sonAylikGider(calisanmag,kiragi,bakim)
isletmeKari(ilkGelir,ilkGider,sonGelir,sonGider)


#Soru4
donemBKol=int(input("Dönem başı koltuk sayısı:"))
donemBYat=int(input("Dönem başı yatak sayısı:"))
donemBDol=int(input("Dönem başı dolap sayısı:"))
birYılSonuKoltuk=(25-10)
birYılSonuYatak=(15-10)
birYılSonuDolap=(10-5)
def donemBasiStok(donemBKol,donemBYat,donemBDol):
    global donemBasi
    donemBasi=donemBKol+donemBYat+donemBDol
    return donemBasi
def donemSonuStok(donemBKol,donemBYat,donemBDol,birYılSonuKoltuk,birYılSonuYatak,birYılSonuDolap):
    global donemSonu
    donemSonu=(donemBKol-birYılSonuKoltuk)+(donemBYat-birYılSonuYatak)+(donemBDol-birYılSonuDolap)
    return donemSonu
def ortalamaStok(donemBasi,donemSonu):
    ortStok=(donemBasi+donemSonu)/2
    print(ortStok)
dBasi=donemBasiStok(donemBKol,donemBYat,donemBDol)
dSonu=donemSonuStok(donemBKol,donemBYat,donemBDol,birYılSonuKoltuk,birYılSonuYatak,birYılSonuDolap)
oStok=ortalamaStok(donemBasi,donemSonu)
