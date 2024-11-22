print("===================================")
print("   Selamat datang di tebak angka   ")
print("===================================")

jawab="YA"
while(jawab=="YA"):
  a=int(input("Masukkan Angka Awal :"))
  b=int(input("Masukkan Angka Akhir :"))
  print()
  print("=========================================")
  print("Silahkan menebak angka yang anda masukkan")
  print("=========================================")
  import random
  angka_acak=random.randint(a,b)

  for i in range(1,4):
    print("Kesempatan ke",i)
    tebakan=int(input("Masukkan tebakan anda :"))
    if(tebakan==angka_acak):
      print("Selamat, Tebakan anda benar!")
      print()
      break
    elif(tebakan>=angka_acak):
      print("Tebakan anda terlalu besar")
      print()
    else:
      print("Tebakan anda terlalu kecil")
  else:
    print("Maaf, Kesempatan anda telah habis!")
  jawab=(input("Apakah anda ingin mengulang permainan(YA/TIDAK) :"))

print("Terimakasih telah menggunakan program saya!")