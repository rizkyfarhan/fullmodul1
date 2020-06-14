# SOAL 1
# def hitungkata():
#     kalimat = input('Masukkan kalimat: ')
#     kalimat = kalimat.lower()
#     kata = kalimat.split()

#     hitung = dict()

#     for i in kata:
#         if i in hitung:
#             hitung[i] += 1
#         else:
#             hitung[i] = 1

#     for j in hitung:
#         print('Jumlah kata ' + j + ' ada sebanyak ' + str(hitung.get(j)))
# hitungkata()

# SOAL 2
# def sevensegment():
#     list = input('Masukkan angka: ').split()
#     listangka = []

#     for angka in list:
#         listangka.append(int(angka))

#     z = ''
#     for i in listangka:
#         if(i == 1 or i == 4):
#             z += '      '
#         else:
#             z += '  __  '
#     z += '\n'
#     for j in listangka:
#         if(j == 5 or i == 6):
#             z += ' |__  '
#         elif(j == 2 or j == 3):
#             z += '  __| '
#         elif(j == 1 or j == 7):
#             z += '    | '
#         elif(j == 0):
#             z += ' |  | '
#         else:
#             z += ' |__| '
#     z += '\n'
#     for k in listangka:
#         if(k == 1 or k == 4 or k == 7):
#             z += '    | '
#         elif(k == 3 or k == 5 or k == 9):
#             z += '  __| '
#         elif(k == 2):
#             z += ' |__  '
#         else:
#             z += ' |__| '
#     print(z)
# sevensegment()

# SOAL 3
# def angkaurut():
#     angka = 1
#     z = ''
#     for i in range(0,ukuran):
#         for j in range(0,ukuran):
#             z += str(angka) + ' '
#             angka += 1
#         z += '\n'
#     print(z)

# def angkarandom():
#     z = ''
#     for i in range(0,ukuran):
#         for j in range(0,ukuran):
#             import random
#             rand = random.randint(1,100)
#             z += str(rand) + ' '
#         z += '\n'
#     print(z)

# stop = False
# while(not stop):
#     ukuran = int(input('Masukkan ukuran: '))
#     print('Pilih')
#     print('1. Angka Urut')
#     print('2. Angka Random')
#     pilihan = input('Masukkan pilihan: ')
#     if pilihan == '1':
#         stop = False
#         angkaurut()
#     elif pilihan == '2':
#         angkarandom()
#         stop = False
#     coba = input('Coba lagi [y/n]: ')
#     if coba == 'y':
#         stop = False
#     elif coba == 'n':
#         stop = True
#     else:
#         print('Masukkan pilihan yang benar')

# SOAL 4
# import math
# angka = []
# for i in range(5):
#     import random
#     rand = random.randint(1,100)
#     angka.append(rand)

# print('Data: ' + str(angka))

# ratarata = sum(angka) / len(angka)

# jumlahan = 0
# for i in angka:
#     kuadrat = (i - ratarata) ** 2
#     jumlahan += kuadrat

# variansi = jumlahan / 5
# print('Variansi data: ' + str(variansi))
# stdev = math.sqrt(variansi)
# print('Standar deviasi data: ' + str(stdev))

# SOAL 5
# jumlahdata = int(input('Jumlah data: '))
# angka = []
# for i in range(jumlahdata):
#     import random
#     rand = random.randint(1,100)
#     angka.append(rand)

# print('Hasil pembangkitan data: ' + str(angka))
# angka.sort()
# print('Data yang telah diurutkan: ' + str(angka))

# if(len(angka) % 2 == 0):
#     angkabawah = angka[int((len(angka)/2)-1)]
#     angkaatas = angka[int((len(angka)/2))]
#     median = (angkaatas + angkabawah) / 2
#     print('Median dari data: ' + str(median))
# else:
#     median = angka[int((len(angka)//2))]
#     print('Median dari data: ' + str(median))

# SOAL 6
# jumlahdata = int(input('Jumlah data: '))
# angka = []
# for i in range(jumlahdata):
#     import random
#     rand = random.randint(1,10)
#     angka.append(rand)

# print('Hasil pembangkitan data: ' + str(angka))
# angka.sort()
# print('Data yang telah diurutkan: ' + str(angka))

# n = len(angka)

# from collections import Counter
# data = Counter(angka)
# get_mode = dict(data)

# print(data)
# print(get_mode)

# modus = max(get_mode.values())
# print(modus)

# SOAL 6 YANG BENAR
from collections import Counter

# DATA INPUT
n_angka = [5,4,3,2,3,2,2,3,4,2,3,2,4,2,1,2,3,4,1,2]
print(n_angka)

# JUMLAH DATA
n = len(n_angka)
print(n)

# COUNTER MENGHITUNG JUMLAH ANGKA
data = Counter(n_angka)
print(data)

# MERUBAH DATA MENJADI DICTIONARY
datamodus = dict(data)
print(datamodus)

# MERUBAH DICTIONARY MENJADI LIST LAGI
print(datamodus.items())

# MENGAMBIL VALUES DICTIONARY DAN MEMASUKKANNYA KE LIST
print(datamodus.values())

# MENCARI NILAI MODUS
modus = [k for (k, v) in datamodus.items() if v == max(datamodus.values())]

if len(modus) == n:
    datamodus = 'No mode found'
else:
    datamodus = 'Mode is / are: ' + str(modus)

print(datamodus)
