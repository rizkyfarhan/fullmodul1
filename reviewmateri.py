# MAP
# MENJALANKAN SETIAP KOMPONEN PARAMETER 2
# KE DALAM PARAMETER 1
# def times2(num):
#     return num * 2
# listNum = [1, 2, 3, 4 ,5]
# listRes = list(map(times2, listNum))
# print(listRes)

# ZIP
# MENGGABUNGKAN PER KOMPONEN 
# DARI MASING-MASING PARAMETER
# x = ['A', 'B', 'C']
# y = [1, 2, 3]
# z = list(zip(x, y))
# print(z)

# REVERSE KATA
# makanan = 'BAKSO'
# print(makanan[-1::-1])

# SORTING
# HANYA MASUKKAN ANGKA GENAP
# seq = [5, 4, 1, 6, 4, 3, 0]
# for i in range(len(seq)):
#     for j in range(i+1):
#         if seq[i] < seq [j] :
#             seq[i], seq[j] = seq[j], seq[i]
# for i in range(len(seq)):
#     if seq[i] % 2 != 0 or seq[i] == 0:
#         seq[i] = ' '
#     else:
#         seq[i] = seq[i]
# print(seq)

# SEGITIGA PASCAL
# baris = int(input('Masukkan berapa banyak baris: '))
# z = ''
# for i in range(0, baris):
#     for j in range(baris-i):
#         z += ' '
#     for k in range(1+i):
#         if k == 0:
#             z += ' 1'
#         elif k == max(range(1+i)):
#             z += ' 1'
#         else:
#             z += ' X'
#     z += '\n'
# print(z)

# SOAL KEMBALIAN
# def tickets(li):
#     result = list()
#     fifty = li.count(50)
#     twfive = li.count(25)
#     # print(fifty)
#     # print(twfive)
#     for i in range(len(li)):
#         if li[i] == 100:
#             if fifty >= 1 and twfive >= 1:
#                 fifty -= 1
#                 twfive -= 1
#                 result.append('YES')
#             else:
#                 result.append('NO')
#         if li[i] == 50:
#             if twfive >= 1:
#                 twfive -= 1
#                 result.append('YES')
#             else:
#                 result.append('NO')
#         if li[i] == 25:
#             result.append('YES')
#     # print(result)
#     nos = result.count('NO')
#     if nos == 0:
#         return 'YES'
#     else:
#         return 'NO'

# print(tickets([25, 100, 25, 100, 50]))
# print(tickets([25, 25, 50]))
