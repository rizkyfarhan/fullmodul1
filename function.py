# ------------------------------------ PERTEMUAN KEEMPAT ------------------------------------

# FUNGSI 
# kode-kode yang dinamakan dan dapat digunakan kembali

# # CONTOH
# def contoh():
#     print('Halo Dunia!')

# contoh()

# # COBA-COBA FUNGSI
# def farhan():
#     print('Nama saya Farhan')
#     print('Umur saya 22 tahun')

# farhan()

# for i in range(1,6):
#     print('saya anak rajin ' + str(i))

# farhan()

# # PARAMETER
# def namaku(nama):
#     print(nama + ' Susilo')

# namaku('Adi')

# # COBA-COBA PARAMETER
# def farhan(x):
#     print(5 ** x)

# pangkat = int(input('Masukkan pangkat : '))
# farhan(pangkat)

# # DUA PARAMETER
# def data(x,y):
#     print(x + ' lahir tahun ' + y)

# data('Adi', '1990')

# # COBA-COBA MULTIPLE PARAMETER
# def rumus(p,l,t):
#     print('Volume balok : ' + str(p * l * t))

# ip = int(input('Masukkan panjang balok : '))
# il = int(input('Masukkan lebar balok : '))
# it = int(input('Masukkan tinggi balok : '))

# rumus(ip,il,it)

# # RETURN -> HASILNYA KESIMPEN
# def total(x,y):
#     z = x + y
#     return z

# print(total(4,5))

# def total2(x,y):
#     z = x + y
#     print(z)

# total2(4,5)

# # COBA-COBA RETURN
# def persegi(pp,lp):
#     luas = pp * lp
#     return luas

# ipp = int(input('Masukkan panjang persegi : '))
# ilp = int(input('Masukkan lebar persegi : '))

# hluas = persegi(ipp,ilp)
# print('Luas persegi : ' + str(hluas))

# def kubus(pk,lk,tk):
#     volume = pk * lk * tk
#     return volume

# ipk = int(input('Masukkan panjang kubus : '))
# ilk = int(input('Masukkan lebar kubus : '))
# itk = int(input('Masukkan tinggi kubus : '))

# hvolume = kubus(ipk,ilk,itk)
# print('Volume persegi : ' + str(hvolume))

# hkali = persegi(ipp,ilp) * kubus(ipk,ilk,itk)
# print('Hasil kali luas dan volume : ' + str(hkali))

# # FUNCTION INSIDE A FUNCTION
# def kali(x):
#     if(x<2):
#         lpersegi = x * x
#         return lpersegi
#     else:
#         lpersegi = x * x
#         return (lpersegi * sisi(5,3))

# def sisi(a,b):
#     return (a % b)

# ix = int(input('Masukkan angka : '))
# print(kali(ix))

# # DEFAULT PARAMETER
# def kali(angka1 = 5,angka2 = 2):
#     return angka1 * angka2

# print(kali(angka2 = 4))