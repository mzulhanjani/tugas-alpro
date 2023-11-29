# Input bilangan dari pengguna
input_bilangan = input("Masukkan bilangan yang akan disusun (pisahkan dengan spasi): ")

# Mengonversi input string menjadi list bilangan
bilangan_list = [int(bil) for bil in input_bilangan.split()]

# Mengurutkan bilangan secara ascending
bilangan_list.sort()

# Menampilkan hasil
print("Bilangan setelah diurutkan secara ascending:", bilangan_list)
