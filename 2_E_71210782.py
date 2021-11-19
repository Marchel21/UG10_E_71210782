#Pendataan suhu tubuh
n = float(input("Masukkan suhu tubuh :"))

#perumusan menggunakan if dan else
if n >= 50:
    print ("anda bukan manusia :)")
elif n <=32:
    print ("Anda dianggap kedinginan! silahkan cari sesuatu yang hangat!")
elif (n>37.5) and (n<50):
    print ("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
elif (n>=32) and (n<=37.5):
    print ("Suhu anda normal!")

    
    
