# # SOAL 1
# inputhari = int(input('Masukkan jumlah hari : '))

# if(inputhari>=0):
#     tahun = inputhari // 360
#     sisatahun = inputhari % 360
#     bulan = sisatahun // 30
#     sisabulan = sisatahun % 30
#     minggu = sisabulan // 7
#     hari = sisabulan % 7
#     print(str(inputhari) + ' hari = ' + str(tahun) + ' tahun ' + str(bulan) + ' bulan ' + str(minggu)+ ' minggu ' + str(hari) + ' hari')
# else:
#     print('Masukkan jumlah hari yang benar')


# SOAL 2 ALT 1
# a = int(input('Masukkan range : '))
# abaru = a+1
# b = 0
# listitem = list(range(0,abaru))
# print(str(listitem))
# for i in range(0,abaru):
#     b+=i
# print('rata-rata dari 0 sampai ' + str(a) + ' adalah ' + str(b/(a))) 


# SOAL 2 ALT 2
# listitem = list(range(1,10))
# print(listitem)

# jumlah = 0
# for i in range(0,10):
#     jumlah += int(i)

# rata = jumlah / len(listitem)
# print(rata)


# SOAL 3 ALT 1
# kata = (input('Masukkan kata apa saja : ')).lower()
# huruf = (input('Huruf atau kata yang akan dihitung jumlahnya : ')).lower()

# jumlahkarakter = len(kata)
# hitung = 0
# awal = 0
# akhir = awal + 1

# for i in range(awal,jumlahkarakter):
#     if(kata[awal:akhir] == huruf):
#         hitung+=1
#     awal+=1
#     akhir= awal + 1

# print(kata + ' memiliki huruf ' + huruf + ' sebanyak ' + str(hitung))

# SOAL 3 ALT 2
# kata = input('Masukkan kata apa saja : ')
# huruf = input('Huruf atau kata yang akan dihitung jumlahnya : ')

# katalower = kata.lower()
# huruflower = huruf.lower()

# hitung = kata.count(huruf)
# print(hitung)

# SOAL 4
# jarak = 120
# a = 60
# b = 40
# mulai = 9

# jam = 120//(a+b)
# sisajarak = 120%(a+b)
# sisajam = sisajarak/(a+b)
# menit = sisajam * 60

# print(str(mulai+jam) + ' jam dan ' + str(menit) + ' menit')

# SOAL 5
# baris = int(input('Masukkan jumlah baris bintang yang diinginkan : '))

# z = ''
# for i in range(0,baris):
#     for j in range(0,i+1):
#         z += '* '
#     z += '\n \n'
# print(z)

# SOAL 6
# jumlah = int(input('Masukkan banyaknya data : '))
# total = 0

# for i in range (1, jumlah+1):
#     data = input('Data ke-' + str(i) + ' : ')
#     total = total + int(data)
# # print(total)
# ratarata = total / jumlah
# print('rata-rata ' + str(jumlah) + ' data tersebut adalah ' + str(ratarata))

# SOAL 7
print('Pilihan 1 adalah menghitung luas segitiga')
print('Pilihan 2 adalah menghitung setengah luas lingkaran')
print('Pilihan 3 adalah menghitung rata-rata')
print('Pilihan 4 adalah menghitung variansi dan standar deviasi')
pilihan = input('Perhatikan pilihan diatas, masukkan pilihan anda : ')

if(pilihan == '1'):
    alas = float(input('Masukkan alas dari segitiga : '))
    tinggi = float(input('Masukkan tinggi dari segitiga : '))
    luassegitiga = 0.5 * alas * tinggi
    print('Luas segitiga dengan alas ' + str(alas) + ' dan tinggi ' + str(tinggi) + ' adalah ' + str(luassegitiga))

elif(pilihan == '2'):
    jarijari = float(input('Masukkan jari-jari lingkaran : '))
    import math
    luassetling = 0.5 * math.pi * jarijari * jarijari
    print('Luas setengah lingkaran dengan jari-jari ' + str(jarijari) + ' adalah ' + str(luassetling))

elif(pilihan == '3'):
    jumlah = int(input('Masukkan banyaknya data : '))
    total = 0

    for i in range (1, jumlah+1):
        data = input('Data ke-' + str(i) + ' : ')
        total = total + int(data)

    ratarata = total / jumlah
    print('rata-rata ' + str(jumlah) + ' data tersebut adalah ' + str(ratarata))

elif(pilihan == '4'):
    jumlah = int(input('Masukkan banyaknya data : '))
    total = 0
    listdata = []

    for i in range(1, jumlah+1):
        data = input('Data ke-' + str(i) + ' : ')
        listdata.append(str(data))
        total = total + int(data)
        
    ratarata = total / jumlah
    # print(listdata)

    jumlahan = 0
    for j in range(0,jumlah):
        kuadrat = (float(listdata[j]) - ratarata) ** 2
        jumlahan = jumlahan + kuadrat
    variansi = jumlahan / (jumlah-1)
    print('Variansi dari data-data tersebut adalah ' + str(variansi))
    import math
    stdev = math.sqrt(variansi)
    print('Standar deviasi dari data-data tersebut adalah ' + str(stdev))

else:
    print('Masukkan pilihan yang benar')
