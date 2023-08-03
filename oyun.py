import random

oyuncu_skor = 0
bilgisayar_skor = 0

hamleler = ["Taş","Kağıt","Makas"]
bitis = int(input("Kaçta Bitsin: "))

while oyuncu_skor <  bitis and bilgisayar_skor < bitis:
    print()
    pc_hamle = random.choice(hamleler)
    try:
        oyuncu_hamle_text = int(input("Taş için 0, Kağıt için 1, Makas için 2 Yazın!"))
        oyuncu_hamle = hamleler[oyuncu_hamle_text]
    except:
        print("Lütfen Düzgün Hamle Yapınız!")
        continue

    if oyuncu_hamle == "Taş" and pc_hamle == "Kağıt":
        print("Bilgisayar Kağıt Yaptı!")
        print("Kağıt Taşı Yener!")
        print("Bilgisayar +1 puan aldı!")
        bilgisayar_skor += 1
        print(f"Bilgisayar: {bilgisayar_skor}")
        print(f"Oyuncu: {oyuncu_skor}")


    elif oyuncu_hamle == "Kağıt" and pc_hamle == "Taş":
        print("Bilgisayar Taş Yaptı!")
        print("Kağıt Taşı Yener!")
        print("Oyuncu +1 puan aldı!")
        oyuncu_skor += 1
        print(f"Bilgisayar: {bilgisayar_skor}")
        print(f"Oyuncu: {oyuncu_skor}")

    elif oyuncu_hamle == "Kağıt" and pc_hamle == "Makas":
        print("Bilgisayar Makas Yaptı!")
        print("Makas Kağıdı Yener!")
        print("Bilgisayar +1 puan aldı!")
        bilgisayar_skor += 1
        print(f"Bilgisayar: {bilgisayar_skor}")
        print(f"Oyuncu: {oyuncu_skor}")

    elif oyuncu_hamle == "Makas" and pc_hamle == "Kağıt":
        print("Bilgisayar Kağıt Yaptı!")
        print("Makas Kağıdı Yener!")
        print("Oyuncu +1 puan aldı!")
        oyuncu_skor += 1
        print(f"Bilgisayar: {bilgisayar_skor}")
        print(f"Oyuncu: {oyuncu_skor}")

    elif oyuncu_hamle == "Makas" and pc_hamle == "Taş":
        print("Bilgisayar Taş Yaptı!")
        print("Taş Makası Yener!")
        print("Bilgisayar +1 puan aldı!")
        bilgisayar_skor += 1
        print(f"Bilgisayar: {bilgisayar_skor}")
        print(f"Oyuncu: {oyuncu_skor}")

    elif pc_hamle == "Makas" and oyuncu_hamle == "Taş":
        print("Bilgisayar Makas Yaptı!")
        print("Taş Makası Yener!")
        print("Oyuncu +1 puan aldı!")
        oyuncu_skor += 1
        print(f"Bilgisayar: {bilgisayar_skor}")
        print(f"Oyuncu: {oyuncu_skor}")
    elif pc_hamle == oyuncu_hamle:
        print("Berabere!")
        print("Bilgisayar da ", pc_hamle, "Yaptı")
    else:
        print("Bilgisayar ----->",pc_hamle)
        print("Oyuncu ----->",oyuncu_hamle)

if oyuncu_skor > bilgisayar_skor:
    print("Tebrikler Kazandınız!!")
else:
    print("Bilgisayar Kazandı Kaybettin!!")