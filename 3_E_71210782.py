#pendataan daftar siswa
a = ((input("Masukkan daftar siswa : ")))
print ("Daftar Siswa : ", a.title().split(",")) 

#menginput siswa yang ditambahkan
b = ((input("Masukkan siswa yang ingin ditambahkan : ")))

#menemukan hasil 
if b not in a :
    print ("Hasil penambahan pada daftar siswa : ", [a.title(), b.upper()])
else:
    print("Siswa atas nama", (b.upper()) ,"sudah berada dalam daftar siswa.")
    
