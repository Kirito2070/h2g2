print("NOT HESAPLAMA PROGRAMI\n")

ad = input("Adınızı girin: ")
n1 = int(input(f"Sayın {ad}, 1. yazılı notun nedir? "))
n2 = int(input(f"Sayın {ad}, 2. yazılı notun nedir? "))

ortalama = (n1 + n2) / 2

if n1 > 100 or n1 < 0 or n2 > 100 or n2 < 0:
    print("Geçersiz not girişi.")
    print("Lütfen tekrar deneyiniz.")
else:
    if ortalama >= 90:
        print(f"Süper: ortalama {ortalama}")
    elif ortalama >= 80:
        print(f"Güzel not: ortalama {ortalama}")
    elif ortalama >= 50:
        print(f"{ortalama} ortalama ile geçtin.")
    else:
        print(f"Maalesef {ortalama} ortalama ile kaldın.")