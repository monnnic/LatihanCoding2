import random
import os
class ceritaKu:
    def __init__(self):
        orang = [ "irene", "fahri", "dave", "farhan", "kiel"]
        randomOrang = random.choice(orang)
        tujuanAwal = [ "sekolah", "taman", "cafe" ]
        randomtujuanAwal = random.choice(tujuanAwal)
        orangLain = [ "monic", "razan", "maliq"]
        randomorangLain = random.choice(orangLain)
        tujuanAkhir = [ "restoran", "mall", "waterpark" ]
        randomtujuanAkhir = random.choice(tujuanAkhir)
        os.system("cls")
        print(f"{randomOrang} pergi ke {randomtujuanAwal} untuk berjumpa dengan {randomorangLain} lalu mereka berdua pergi bersama ke {randomtujuanAkhir}")
def main():
    run = ceritaKu()
if __name__ == "__main__":
    main()