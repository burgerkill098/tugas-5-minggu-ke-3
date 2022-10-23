print("menghitung luas persegi panjang ,segitiga dan lingkaran ")
print("=================================================================")

panjang=float(input("masukkan panjang = "))

lebar =float(input("masukkan lebar = "))

alas=float(input("masukkan alas ="))

tinggi=float(input("masukkan tinggi "))

r=float(input("masukkan jari jari ="))

phi=22/7

luas_persegi_panjang= panjang *lebar

luas_segitiga=1/2*alas *tinggi

luas_lingkaran= phi*r*r
print("______________________________________________________________")
print("luas persegi panjang adalah =",luas_persegi_panjang)
print("luas segitiga adalah =",luas_segitiga )
print("luas lingkaran adalah =",luas_lingkaran)