# ------------------------------------ PERTEMUAN PERTAMA ------------------------------------

print ('Hello World')

# STRING
nama = 'Andi'
print(nama)

# INTEGER
usia = 22
usia = 32
print(usia)

# BOOLEAN
jomblo = True
print(jomblo)

# CEK TIPE DATA
print(type(nama))
print(type(usia))
print(type(jomblo))


# LATIHAN 1
nama = 'Farhan'
umur = 22
jeniskelamin = 'Pria'
pendidikanterakhir = 'S1 Teknik Industri UNPAR'

print(nama)
print(umur)
print(jeniskelamin)
print(pendidikanterakhir)

print(type(nama))
print(type(umur))
print(type(jeniskelamin))
print(type(pendidikanterakhir))


# INPUT
nama = input('Whats your name? : ')
print(nama)
print(type(nama))

umur = input('Whats your age? : ')
print(umur)
print(int(umur))

status = input('Whats your status? : ')

print('Nama saya adalah ' + nama + ' dengan umur ' + umur + ' dan berstatus ' + status)


# LATIHAN 2
nama = input('Nama kamu? : ')
umur = input('Umur Kamu? : ')
kelamin = input('Kelamin kamu? : ')
pekerjaan = input('Pekerjaan kamu? : ')
print('Nama : ' + nama)
print('Umur : ' + umur)
print('Jenis Kelamin : ' + kelamin)
print('Pekerjaan : ' + pekerjaan)
print('Nama saya ' + nama + ', umur saya ' + umur + ', jenis kelamin saya ' + kelamin + ', pekerjaan saya adalah ' + pekerjaan)

# Nomor WA Mas Achmad 085340984234


# ------------------------------------ PERTEMUAN KEDUA ------------------------------------

usiaAndi = 40
usiaBudi = 20

print(usiaAndi * usiaBudi)
print(usiaAndi / usiaBudi)
print(usiaAndi + usiaBudi)
print(usiaAndi - usiaBudi)
print(usiaAndi % usiaBudi) # MODULUS = SISA BAGI
print(usiaBudi ** 2) # PANGKAT
print(usiaBudi // 2) # BAGI DAN DITURUNIN KEBAWAH

print(round(4.5))

import math # SELALU HARUS DITULIS
print(math.floor(4.5)) # PEMBULATAN KEBAWAH
print(math.ceil(4.5)) # PEMBULATAN KEATAS

# LATIHAN
print(8 ** 5)
print(round(9.9))
print(-9.5 * 7)
print(100 % 70)

print(12+9/3)

x = 'Halo Dunia'

print(len(x)) # PANJANG STRING
print(x.index('Dunia')) # HITUNG HURUF
print(x.split(' ')) # MISAHIN STRING
print(x.lower()) # JADI HURUF KECIL
print(x.upper()) # JADI HURUF BESAR
print(x.capitalize()) # HURUF BESAR DIDEPAN


text = "I'm Baron, nice to meet you"

print(text[1]) # X
print(text[2:]) # DARI X SAMPE AKHIR
print(text[:4]) # DARI AWAL SAMPE X
print(text[2:5]) # DARI X SAMPE Y
print(text[:]) # SEMUA


angka1 = input('angka 1 : ')
angka2 = input('angka 2 : ')

print(int(angka1) + int(angka2))


angka1 = int(input('angka 1 : '))
angka2 = int(input('angka 2 : '))

print(angka1 + angka2)


# MASIH BENTUK STRING
angka1 = input('angka 1 : ')
angka2 = input('angka 2 : ')

# DIUBAH JADI FLOAT
angka1 = float(angka1)
angka2 = float(angka2)

# OPERASI ARITMATIK BISA DIJALANKAN
print(angka1 + angka2)


usia = 22
nama = 'Andi'

print(usia + usia)
print(nama + ' ' + nama)
print(nama + ' ' + str(usia))


# LATIHAN 0
nama = input('Nama : ')
jeniskelamin = input('Jenis Kelamin : ')
umur = input('umur : ')

umur = int(umur)
umur = umur + 3
umur = str(umur)

print('Nama saya adalah ' + nama + ' berjenis kelamin ' + jeniskelamin + ' berusia ' + umur + ' di 3 tahun yang akan datang')


# LATIHAN  1
x = 4
y = 3
z = 2

w = ((x + y * z)/(x * y)) ** z
print(w)


# LATIHAN 2
angka = input('Silahkan masukkan angka berapapun : ')

pangkat = str( int(angka) * int(angka) )

print('Kuadrat dari ' + angka + ' = ' + pangkat)


# LATIHAN 3
hari = 485
tahun = (485 // 360)
sisatahun = 485 % 360
bulan = (sisatahun // 30)
sisabulan = sisatahun % 30
minggu = (sisabulan // 7)
hari = sisabulan % 7

print('485 hari = ' + str(tahun) + ' tahun ' + str(bulan) + ' bulan ' + str(minggu) + ' minggu ' + str(hari) + ' hari' )


# ------------------------------------ PR ------------------------------------

# SOAL 1
angka = input('Masukkan 4 digit angka : ')
depan = angka[0:2]
belakang = angka[2:4]

angkabaru = belakang + depan
print(angkabaru)

# SOAL 2
import math
radius = int(input('Masukkan jari-jari lingkaran : '))
area = math.pi * radius * radius

print(area)

# SOAL 3
angka1 = input('Masukkan 2 digit angka pertama : ')
angka2 = input('Masukkan 2 digit angka kedua : ')

angkabaru = angka1[0:1] + angka2[0:1] + angka1[1:2] + angka2[1:2]
print(angkabaru)

# SOAL 4
kalimat = input('Masukkan kalimat : ')
huruf = input('Masukkan huruf yang ingin dihapus : ')

kalimatbaru = kalimat.replace(huruf, '')
print(kalimatbaru)

# SOAL 5
kalimat = input('Masukkan 2 kata : ')
kata = kalimat.split(' ')
print(kata[1] + ' ' + kata[0])

# SOAL 6
# a + b = 49
# a / b = 0.4

# a = 0.4 b
# 0.4 b + b = 49
# 1.4 b = 49

rasio = 0.4
total = 49

b = total / (rasio + 1) 
a = 0.4 * b

b = str(b + 2)
a = str(a + 2)

print('Umur Andi dua tahun lagi adalah ' + a + ' dan umur Budi dua tahun lagi adalah ' + b)