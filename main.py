import random

def kelime_sec(kelimeler):
    return random.choice(kelimeler).upper()

def oyunu_baslat():
    kelimeler = ["elma", "kitap", "masa", "python", "oyun", "araba", "bilgisayar"]
    gizli_kelime = kelime_sec(kelimeler)
    tahmin_edilen = ["_" for _ in gizli_kelime]
    tahmin_edilen_harfler = set()
    can_hakki = 6

    print("🎮 Kelime Tahmin Oyununa Hoş Geldin!")
    print("Kelimeyi tahmin etmeye çalış. Harf harf ilerle.\n")

    while can_hakki > 0 and "_" in tahmin_edilen:
        print(f"\nKelime: {' '.join(tahmin_edilen)}")
        print(f"Kalan can: {can_hakki}")
        print(f"Tahmin edilen harfler: {', '.join(sorted(tahmin_edilen_harfler))}")

        tahmin = input("Bir harf tahmin et: ").strip().upper()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("⚠️ Lütfen sadece bir harf gir.")
            continue

        if tahmin in tahmin_edilen_harfler:
            print("🔁 Bu harfi zaten denedin.")
            continue

        tahmin_edilen_harfler.add(tahmin)

        if tahmin in gizli_kelime:
            print("✅ Doğru tahmin!")
            for i, harf in enumerate(gizli_kelime):
                if harf == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("❌ Yanlış tahmin.")
            can_hakki -= 1

    if "_" not in tahmin_edilen:
        print(f"\n🎉 Tebrikler! Kelimeyi bildin: {gizli_kelime}")
    else:
        print(f"\n😢 Oyun bitti. Doğru kelime: {gizli_kelime}")

if __name__ == "__main__":
    oyunu_baslat()
