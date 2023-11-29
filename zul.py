# memanggil program_1 dan membuat hasil tampil pada python 
import subprocess

subprocess.run(["python", "random_1.py"])


# Panggil program_urut_ganjil_genap.py sebagai subprocess
result = subprocess.run(["python", "random_1.py"], capture_output=True, text=True)

# Simpan output ke dalam file
with open("hasil_random.txt", "w") as file:
    file.write(result.stdout)

# Tampilkan output di terminal
print(result.stdout)
