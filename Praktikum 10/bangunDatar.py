import math

def jajarGanjar(alas, tinggi):
    return alas * tinggi
print (jajarGanjar(4,7))

def persegi(sisi):
    hasil = sisi * sisi
    return hasil
print (persegi(5))

def persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil
print (persegi_panjang(7,5))

def segitiga (alas, tinggi):
    hasil = 0.5 * alas * tinggi
    return hasil
print (segitiga(20,4))

def lingkaran(jari_jari):
    hasil = math.pi * jari_jari * jari_jari
    return hasil
print (lingkaran(7))
