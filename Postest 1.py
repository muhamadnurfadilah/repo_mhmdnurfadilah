print("Nama : Muhamad Nur Fadilah")
print("NIM : 2309116001")
print ("Sistem Informasi A")
print("Tugas Postes Praktikum 1")

print("===============================================")

#Login Sederhana
username = input("Masukan Username : ") #Memasukkan input username
password = input("Masukan Password : ") #Memasukkan input password

if password == "11223344" :     #if untuk memasukkan password yang ingin di simpan
    print("Selamat Datang","Anda Berhasil Login") #Menampilkan Selamat Datang jika password sesuai
else :                          #else untuk password yang tidak sesuai atau memasukkan password lain selaing yang di simpan
    print("Maaf Anda Gagal Login!!!") #Menampilkan hasil Gagal Login karena tidak menemukan Password

print("===============================================")

# Menampilkan menu pilihan mencari sisi
print("Pilihan Rumus :")
print("1. Hitung panjang sisi miring (hipotenusa)")
print("2. Hitung panjang sisi alas")
print("3. Hitung panjang sisi tegak")

# Pilih sisi yang ingin di cari
pilihan = int(input("Masukkan nomor pilihan untuk mencari sisi (1,2,3): "))

# Meminta panjang sisi-sisi segitiga
a = float(input("Masukkan panjang sisi a: ")) #Memasukkan Sisi A
b = float(input("Masukkan panjang sisi b: ")) #Memasukkan Sisi B

# Menggunakan percabangan untuk menghitung masing masing panjang sisi
if pilihan == 1:            #if untuk memilih menu pilihan pertama (Sisi Miring)                  
    c = float(b**2 + a**2)  #Memasukkan Rumus sisi miring
    print("Panjang sisi miring (hipotenusa) adalah:", c) #Menampilkan hasil Sisi Miring
elif pilihan == 2:          #elif untuk memilih menu pilihan kedua (Sisi Alas)
    c = float(a**2 - b**2)  #Memasukkan Rumus sisi alas
    print("Panjang sisi alas adalah:", c) #Menampilkan hasil sisi alas
elif pilihan == 3:          #elif untuk memilih menu pilihan ketiga (Sisi Tegak)
    c = float(a**2 - b**2)  #Memasukkan Rumus sisi Tegak
    print("Panjang sisi tegak adalah:", c) #Menampilkan hasil sisi tegak
else:                       #else untuk untuk menu yang tidak ada maka tidak terbaca
    print("Pilihan tidak ada. Silakan masukkan nomor pilihan yang sesuai (1/2/3).") #Menampilkan hasil pencarian yang tidak ada atau tidak terdeteksi