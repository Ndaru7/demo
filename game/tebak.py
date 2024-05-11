#program tebak angka
import random

while True:
    print("1.Tebak")
    print("2.Keluar\n")
    
    pilih = int(input("Pilih\t:"))

    if pilih==1:
        angka = int(input("\nTebak 1-10: "))
        acak = random.randint(1,10)

        if angka==acak:
            print("\nTebakan Benar\n")
            break

        elif angka!=acak:
            print("Tebakan Salah\n")
            break

    elif pilih==2:
        print("\nKeluar...\n")
        break

    else:
        print("\npilihan tidak valid\n")
