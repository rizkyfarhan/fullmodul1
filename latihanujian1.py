# SOAL 1
# def timeconverter(input):
#     jam = input // 60
#     menit = input % 60
#     if jam < 10:
#         jam = '0' + str(jam)
#     if menit < 10:
#         menit = '0' + str(menit)
#     print(str(jam) + ':' + str(menit))

# detik = int(input('Masukkan berapa detik: '))
# timeconverter(detik)


# SOAL 2
# diataslima = list()
# hasilpindah = list()
# def moveOverFive(listinput):
#     for i in range(len(listinput)):
#         if type(listinput[i]) != int:
#             hasilpindah.append(listinput[i])
#         elif listinput[i] <= 5:
#             hasilpindah.append(listinput[i])
#         elif listinput[i] > 5:
#             diataslima.append(listinput[i])
#     return hasilpindah

# moveOverFive([5, 2, 19, 'Halo', 6, 1, 4, 24, 3, False, 7])
# print(hasilpindah + diataslima)
# diataslima.sort()
# print(diataslima)


# SOAL 3
# baris = int(input('Masukkan berapa baris: '))

# ct = 0
# temp = list()
# a = 1
# z = ''
# for i in range(0, baris*2, 2):
#     for j in range(baris*2+1-i):
#         z += '  '
#     for k in range(i+1):
#         if a == 1:
#             z += str(a).ljust(4, ' ')
#             a += 1
#         elif ct != 2:
#             z += str(a).ljust(4, ' ')
#             temp.append(a)
#             a += 1
#             ct += 1
#         elif ct == 2:
#             z += str(sum(temp)).ljust(4, ' ')
#             ct = 0
#             temp = list()
#     z += '\n'
# print(z)


# SOAL 3
baris = int(input('Masukkan berapa banyak baris: '))
a = 1
temp = list()
z = ''
for i in range(0, baris):
    for j in range(0, baris-i):
        z += '  '
    for k in range(0, 1+i):
        temp.append(a)
        z += str(a).ljust(4, ' ')
        a += 1
    z += str(sum(temp))
    temp = list()
    z += '\n'
print(z)

