import random

# Membuat list bilangan acak
bilangan_acak = [random.randint(0, 399) for _ in range(100)]

# Menampilkan bilangan acak sebelum diurutkan
print("Bilangan Acak Sebelum Diurutkan:", bilangan_acak)

# Mengurutkan bilangan acak
bilangan_acak.sort()

# Menampilkan bilangan acak setelah diurutkan
print("Bilangan Acak Setelah Diurutkan:", bilangan_acak)

# Mencari bilangan ganjil dan genap
bilangan_ganjil = [bilangan for bilangan in bilangan_acak if bilangan % 2 != 0]
bilangan_genap = [bilangan for bilangan in bilangan_acak if bilangan % 2 == 0]

# Menampilkan hasil
print("Bilangan Ganjil:", bilangan_ganjil)
print("Bilangan Genap:", bilangan_genap)

