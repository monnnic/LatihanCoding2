awal=int(input("Masukkan Angka Awal : "))
akhir=int(input("Masukkan Angka Akhir : "))
print("=============================================")
print("= 1. Penjumlahan (+) =")
print("= 2. Pengurangan (-) =")
print("= 3. Perkalian   (*) =")
print("= 4. Pembagiann  (/) =")
print("= 5. Sisa bagi   (%) =")
print("=============================================")
operator=int(input("Masukkan operator = "))
if operator == 1:
  print("Hasil dari",awal," + ",akhir, " = " ,awal+akhir)
elif operator == 2:
  print("Hasil dari",awal," - ",akhir, " = " ,awal-akhir)
elif operator == 3:
  print("Hasil dari",awal," * ",akhir, " = " ,awal*akhir)
elif operator == 4:
  print("Hasil dari",awal," / ",akhir, " = " ,awal/akhir)
elif operator == 5:
  print("Hasil dari",awal," % ",akhir, " = " ,awal%akhir)
else:
  print("operator tidak tersedia")