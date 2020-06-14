# ------------------------------------ PERTEMUAN KELIMA ------------------------------------

# mobil = ['Alya', 'Xenia', 'Avanza']

# print(mobil)
# print(mobil[0])
# print(mobil[1])
# print(mobil[2])
# print(mobil[-1])

# buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga']

# print(buah[2:4])
# print(buah[:])

# LATIHAN LIST 1
# teman = ['Joni', 'Andi', 'Yogas', 'Chris', 'Suryo', 'Anan']

# print('Isi list teman indeks ke-3 adalah ' + teman[3] + ' dan indeks ke-5 adalah ' + teman[5])
# print('Total saya memiliki ' + str(len(teman)) + ' teman')
# print('2 orang diantara teman saya bernama ' + teman[0] + ' dan ' + teman[1])

# for i in teman:
#     print(i)

# buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga']

# buah.pop(3) # MENGAPUS ELEMEN INDEKS 3
# print(buah)
# buah.append('Mangga') # MENAMBAHKAN ELEMEN MANGGA DI AKHIR
# print(buah)

# buah.insert(2,'Pepaya') # MENAMBAHKAN PEPAYA DI INDEKS 2
# print(buah)

# buah.remove('Jeruk') # MENGHAPUS ELEMEN JERUK
# print(buah)

# LATIHAN LIST 2
# hobi = []
# stop = False
# i = 1

# while(not stop):
#     tambah = input('Inputkan hobi ke-' + str(i) + ': ')
#     hobi.append(tambah)
#     pilih = input('Mau isi lagi? (y/t) ')
#     if(pilih == 'y'):
#         stop = False
#         i += 1
#     elif(pilih == 't'):
#         stop = True
#     else:
#         stop = True
#         print('Masukkan keyword yang benar')

# print('===============================')
# print('Kamu memiliki ' + str(len(hobi)) +' hobi: ')
# for j in hobi:
#     print('- ' + j)

# LATIHAN LIST 3
# x = [40,100,1,5,25,10]

# def urut(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr

# print(urut(x))

# LATIHAN LIST 4
# x = [40,100,1,5,25,10]

# def urut(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr

# print(urut(x))

# LATIHAN LIST 5
# x = [40,100,1,5,25,10]

# def maks(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr[0]

# print(maks(x))

# def min(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr[0]

# print(min(x))

# LATIHAN 6
x = [40,100,1,5,25,10]
ganjil = []
genap = []

def hitung(x):
    for i in range(len(x)):
        if(x[i] % 2 == 0):
            genap.append(x[i])
        else:
            ganjil.append(x[i])

hitung(x)
print(ganjil)
print(genap)