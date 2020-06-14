# ------------------------------------ PERTEMUAN KETIGA ------------------------------------

nilai = 40

if(nilai>80) :
    print("Excellent!")
elif(nilai>=60 and nilai<=80) :
    print("Good Job!")
else :
    print("Don't Give Up!")


# LATIHAN 1
angka = int(input('Masukkan angka : '))

if(angka%2 == 0) :
    print('Angka ' + str(angka) + ' tergolong bilangan GENAP!')
else :
    print('Angka ' + str(angka) + ' tergolong bilangan GANJIL!')


# LATIHAN 2
massa = int(input('Masukkan Massa(kg) : '))
tinggi = int(input('Masukkan Tinggi(cm) : '))

tinggi = float(tinggi/100)

print('Massa ' + str(massa) + ' kg & tinggi ' + str(tinggi))

imt = massa / (tinggi*tinggi)

if(imt>39.9) :
    print('IMT = ' + str(imt) + ', obesitas')
elif(imt>30 and imt<=39.9) :
    print('IMT = ' + str(imt) + ', BB sangat berlebih')
elif(imt>25 and imt<29.9) :
    print('IMT = ' + str(imt) + ', BB berlebih')
elif(imt>18.5 and imt<24.9) :
    print('IMT = ' + str(imt) + ', berat badan ideal')
else :
    print('IMT = ' + str(imt) + ', berat badan kurang')