welcome_message = "WELCOME TO TIKUS!"
TIKUS_position = 2

print(welcome_message)

nama_user = input("Masukkan Nama Kamu : ")
print("Halo " + nama_user + "!")
print("Perhatikan guwa ini |_| |_| |_| ")

PILIHAN_user = int(input("Di Guwa nomer berapa TIKUS BERADA [ 1 / 2 / 3 ] : "))

if PILIHAN_user == TIKUS_position:
    print("KAMU MENANG")
else:
    print("KAMU SALAH")