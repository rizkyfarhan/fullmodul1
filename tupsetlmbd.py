# ------------------------------------ PERTEMUAN KETUJUH ------------------------------------

# TUPLES
# ISI DARI TUPLES TIDAK BISA DIUBAH SEPERTI DICTIONARY
# BISA PAKAI KURUNG BIASA ATAUPUN TIDAK

#CONTOH
# a = (1,2,3,4,'lima')
# print(a)

# INISIASI TUPLES KOSONG
# angka = ()

# HARUS TETAP PAKAI KOMA AGAR TIDAK TERBACA STRING
# huruf = 'a',
# print(type(huruf))

# DIAKSES DENGAN INDEKS SEPERTI LIST
# print(a[0])

# LATIHAN
# tipedata = ('string', 0, True, 1.0, ['a', 'b', 'c', 1, 2, 3], {'satu': 1, 'dua': 2}, [1, 2, [3, 4]])
# single = ('tunggal',)

# print(tipedata)
# print(type(tipedata))
# print(single)
# print(type(single))


# SETS
# SETS SEPERTI DICTIONARY TAPI TIDAK MENGGUNAKAN KEYS
# TIDAK MEMILIKI INDEKS

# CONTOH
# s = {1, 2, 3}
# print(s)
# print(type(s))

# MERUBAH MENJADI SET
# s1 = set([1, 2, 3])
# print(s1)
# print(type(s1))

# TIDAK MENDUKUNG DUPLIKASI
# s2 = {1, 2, 2, 2, 3, 4, 5, 5}
# print(s2)

# INISIASI SET KOSONG AGAR TIDAK TERBACA DICTIONARY
# s3 = set()
# print(type(s3))

# LATIHAN
# jumlahdata = int(input('Jumlah data: '))
# angka = []
# for i in range(jumlahdata):
#     import random
#     rand = random.randint(1,10)
#     angka.append(rand)
    
# print('Data awal: ')
# print(angka)

# filtered = set(angka)
# print('Hasil filter: ')
# print(filtered)


# LIST COMPREHENSION
# li = [1, 2, 3, 4, 5]
# pangkat = [x ** 2 for x in li]
# print(pangkat)

# LATIHAN
# ganjil = [x for x in range(1,51) if x % 2 != 0]
# genap = [x for x in range(1,51) if x % 2 == 0]

# print(ganjil)
# print(genap)


# LAMBDA
# print((lambda x,y: x**2 + y**2)(5,4))

# bilangan = [1, 2, 3, 4, 5]
# filtered = map(lambda x: x*x, bilangan)

# LATIHAN
# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))
# w = int(input('w: '))
# m = int(input('m: '))

# hitung = (lambda x,y,z,w,m: (((x**y//z)**w)/m))
# print(hitung(x,y,z,w,m))


# SEARCH
# num = [1, 2, 3]
# input = 1
# check = input in num
# print(check)

# LATIHAN
# kata = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
# katalower = [x.lower() for x in kata]

# hasil = []

# keyword = (input('Search: ')).lower()
# for i in range(len(kata)):
#     if keyword in katalower[i]:
#         hasil.append(kata[i])
# print(hasil)

# LATIHAN (LIST INPUT SENDIRI)
# kata = []
# jumlahkata = int(input('Jumlah kata: '))
# for i in range(0,jumlahkata):
#     inpkata = input('Kata ke-' + str(i+1) + ': ')
#     kata.append(inpkata)
# print(kata)
# katalower = [x.lower() for x in kata]

# hasil = []

# keyword = (input('Search: ')).lower()
# for i in range(len(kata)):
#     if keyword in katalower[i]:
#         hasil.append(kata[i])
# print(hasil)