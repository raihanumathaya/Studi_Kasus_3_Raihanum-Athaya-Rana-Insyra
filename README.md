# Studi-Kasus-DDP-3

Nama: Raihanum Athaya Rana Insyra

NIM: 2609116014 (genap) 

Code dari Program Pengelompokkan Nilai Ujian Mahasiswa :

<img width="1962" height="1500" alt="image" src="https://github.com/user-attachments/assets/36ca0d0e-681e-45a0-ad36-f7570a56203c" />

1. Tahap pertama: Membuat variable batas_nilai berbentuk Tuple untuk menjadi acuan kelulusan (minimal 65), serta list kosong untuk nilai yang masuk (nilai_masuk, lulus, remedi) untuk menampung data nilai

2. Tahap kedua: Menggunakan while True untuk terus meminta input data nilai dari user sampai user mengetik "selesai" untuk menghentikan pengulangan (break)

3. Tahap ketiga: Memasukkan input teks menjadi angka (int) dikarenakan bilangannya bulat, dan memasukkannya ke nilai_masuk, lalu memilahnya: jika nilai >= 65 maka akan masuk ke list "lulus", namun jika kurang akan masuk ke list "remedi". Kemudian, menampilkan semua nilai yang sudah dimasukkan.

4. Tahap keempat: Membuat program untuk menghapus nilai yang salah. Dengan cara menanyakan user "apakah ada nilai yang salah input?", kemudian if hapus.lower() == "ya" agar user flexibel menuliskan "ya". kemudian nilai_hapus = int(...) untuk mengubah data yang ingin dihapus ke tipe data integer. Lalu, nilai_masuk.remove(nilai hapus) untuk menghapus angka tersebut dari daftar nilai_masuk

5. Menampilkan hasil data nilai akhir yang tersimpan pada nilai_masuk, lulus, dan remedi. Dengan cara: 
print ("Nilai masuk :", nilai_masuk)
print ("Lulus       :", lulus)
print ("Remedi      :", remedi)

6. Output yang dihasilkan akan seperti ini:

<img width="2438" height="944" alt="image" src="https://github.com/user-attachments/assets/d9323fe6-f913-49c9-8724-3aa1405db4ad" />
