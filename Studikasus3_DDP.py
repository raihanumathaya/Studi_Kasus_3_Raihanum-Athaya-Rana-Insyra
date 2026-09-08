batas_nilai = (65, 100) 
nilai_masuk = []
lulus = [] 
remedi = [] 

while True:
    nilai = input("masukkan nilai: ")
    if nilai.lower() == "selesai":
        break

    nilai = int(nilai)
    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedi.append(nilai)
    
print("Nilai yang sudah dimasukkan:", nilai_masuk)

hapus = input ("Apakah ada nilai yang salah input? (ya/tidak):")

if hapus.lower() == "ya" : 
    nilai_hapus = int(input("Masukkan nilai yang ingin dihapus: "))

    if nilai_hapus in nilai_masuk:
        nilai_masuk.remove(nilai_hapus)

        if nilai_hapus in lulus:
            lulus.remove(nilai_hapus)
        elif nilai_hapus in remedi:
            remedi.remove(nilai_hapus)

        print("Nilai berhasil dihapus")
    else:
        print("Nilai tidak ditemukan")
    
print ("Nilai masuk :", nilai_masuk)
print ("Lulus       :", lulus)
print ("Remedi      :", remedi)
