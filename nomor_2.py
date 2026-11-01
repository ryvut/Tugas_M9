# Nomor 1
hitung_mundur = 10
while hitung_mundur > 0:
    print(f"Sisa waktu hitung mundur: {hitung_mundur}")
    hitung_mundur -= 1
print("Waktu Habis!")

print("-" * 40)

# Nomor 2
angka_genap = 2
while angka_genap <= 10:
    print(angka_genap, end=" ")
    angka_genap += 2
print()

print("-" * 40)

# Nomor 3
akumulasi_berat = 0

while True:
    akumulasi_berat += 5
    print(f"Total berat saat ini: {akumulasi_berat} kg")

    if akumulasi_berat >= 25:
        break

print("-" * 40)

# Nomor 4
kunci_akses = "statbis2026"

while True:
    input_sandi = input("Masukkan password: ")

    if input_sandi == kunci_akses:
        print("Login Berhasil, Selamat Datang!")
        break
    else:
        print("Password salah, silakan coba lagi!")