x=int(input("Finansman Gelirlerini Giriniz"))
y=int(input("Pazar Gelirlerini Giriniz"))
z=int(input("Kira Gelirlerini Giriniz"))
t=int(input("ücreti Giriniz"))
k=int(input("Finansman Giderlerini Giriniz"))
l=int(input("Pazar Gidelerini Giriniz"))
m=int(input("Kira Giderlerini Giriniz"))
n=int(input("Muhasebe Giderlerini Giriniz"))
if (x+y+z)-(t+k+l+m+n)>1000:
    print("işletme karlıdır.")
else:
    print("işletme zarardadır.")




#a=planlanmisüretim,b=plansizDurus
def kullanılabilirlikHesapla(a,b):
   kullanılabilirlik=(a-b)/a
   return kullanılabilirlik
#c=standartCevrim,d=üretimMiktari,e=planlanmisÜretim,f=plansizDurus
def performansHesapla(c,d,e,f):
   performans=(c*d)/(e-f)
   return performans
#g=saglamÜrün,h=toplamÜretim
def kalitehesapla(g,h):
   kalite=(g/h)
   return kalite
#OEE=ekipmanEtkinlikOrani
def OEEHesapla(kullanılabilirlik,performans,kalite):
   OEE=(kullanılabilirlik*performans*kalite)/100
   return OEE



#x=satisMiktari,y=birimSatisFiyati
def ciroHesapla(x,y):
    ciro=x*y
    return ciro
def ciroHesapla(x,y):
    x=int(input("Satış Miktarını Giriniz:"))
    y=int(input("Birim Satış Fiyatını Giriniz:"))
    ciro=x*y
    return ciro
