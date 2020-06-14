# # ------------------------------------ PR ------------------------------------

# # SOAL 1
# angka = input('Masukkan 4 digit angka : ')
# depan = angka[0:2]
# belakang = angka[2:4]

# angkabaru = belakang + depan
# print(angkabaru)

# # PAKE NUMERICAL METHOD
# angka = int(input('Masukkan angka : '))
# print(angka % 100 * 100 + angka // 100)

# # SOAL 2
# import math
# radius = float(input('Masukkan jari-jari lingkaran : '))
# area = math.pi * radius * radius
# print(area)

# # SOAL 3
# angka1 = input('Masukkan 2 digit angka pertama : ')
# angka2 = input('Masukkan 2 digit angka kedua : ')

# angkabaru = angka1[0:1] + angka2[0:1] + angka1[1:2] + angka2[1:2]
# print(angkabaru)

# # PAKE NUMERICAL METHOD
# angka1 = int(input('Masukkan 2 digit angka pertama : '))
# angka2 = int(input('Masukkan 2 digit angka kedua : '))

# # MOD DAPET BELAKANG, BAGI DAPET DEPAN
# d1 = angka1 // 10
# b1 = angka1 % 10
# d2 = angka2 // 10
# b2 = angka2 % 10

# print(d1 * 1000 + d2 * 100 + b1 * 10 + b2)

# # SOAL 4
# kalimat = (input('Masukkan kalimat : ')).lower()
# huruf = (input('Masukkan huruf yang ingin dihapus : ')).lower()

# kalimatbaru = kalimat.replace(huruf, '')
# print(kalimatbaru)

# # SOAL 5
# kalimat = input('Masukkan 2 kata : ')
# kata = kalimat.split(' ')
# print(kata[1] + ' ' + kata[0])

# # SOAL 6
# # a + b = 49
# # a / b = 0.4

# # a = 0.4 b
# # 0.4 b + b = 49
# # 1.4 b = 49

# rasio = float(input('Masukkan rasio umur : '))
# total = float(input('Masukkan total umur : '))

# b = total / (rasio + 1) 
# a = rasio * b

# b = str(b + 2)
# a = str(a + 2)

# print('Umur Andi dua tahun lagi adalah ' + a + ' dan umur Budi dua tahun lagi adalah ' + b)


# # ALTERNATIF SOAL 4
# kalimat = input('Masukkan kalimat : ')
# huruf = input('Masukkan huruf yang ingin dihapus : ')

# hurufkecil = huruf.lower()
# hurufbesar = huruf.upper()

# kalimatbaru = kalimat.replace(hurufkecil, '')
# kalimatbaru = kalimatbaru.replace(hurufbesar, '')
# print(kalimatbaru)