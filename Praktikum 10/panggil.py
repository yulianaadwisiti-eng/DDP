import bangunRuang as br
import bangunDatar as bd

print("==== BANGUN RUANG ====")
print(f"volum kubus dengan sisi 3 adalah {br . kubus(3)}")
print(f"volum balok adalah {br . balok(4, 5, 2)}")
print(f"volum prisma segitiga adalah {br . prisma(5, 4, 5)}")
print(f"volum tabung adalah {br . tabung(6, 15)}")
print(f"volum kerucut adalah {br . kerucut(4, 14)}")

print("==== BANGUN DATAR ====")
print(f"Luas Persegi adalah {bd.persegi(5)}")
print(f"Luas Persegi Panjang adalah {bd.persegi_panjang(8,5)}")
print(f"Luas Segitiga adalah {bd.segitiga(20,4)}")
print(f"Luas Lingkaran adalah {bd.lingkaran(7)}")
print(f"Luas jajarGanjar adalah {bd.jajarGanjar(4, 7)} ")
