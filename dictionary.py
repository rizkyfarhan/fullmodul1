# ------------------------------------ PERTEMUAN KEENAM ------------------------------------

# DICTIONARY
# SETIAP KOMPONEN MEMILIKI KEY YANG BERBEDA
# PEMANGGILAN DILAKUKAN DENGAN KEY BUKAN INDEKS

# CONTOH
# d = {'key1' : 'item1', 'key2' : 'item2', 'kucing' : [3, 'jerapah']}
# print(d['key1'])

# COBA DICTIONARY
# biodata = {'Nama' : 'Farhan', 'Tempat Lahir' : 'Bekasi', 'Tanggal Lahir' : '15/08/97', 'Hobi' : 'Main', 'Alamat' : 'Bekasi'}

# DICTIONARY DIDALAM DICTIONARY
# biodata = {
#     'Nama' : 'Farhan',
#     'Tempat Lahir' : 'Bekasi',
#     'Tanggal Lahir' : '15/08/97',
#     'Hobi' : 'Main',
#     'Alamat' : 'Bekasi',
#     'Pendidikan' : {'SD' : 'Victory plus', 'SMP' : 'Al-Azhar 8', 'SMA' : 'Labschool', 'S1' : 'TI UNPAR'},
#     'Medsos' : {'Facebook' : 'Muhammad Rizky Farhan', 'LinkedIn' : 'Muhammad Rizky Farhan'}
# }
# for i in biodata:
#     print(biodata[i])

# CARA LAIN MEMANGGIL KOMPONEN
# print(biodata.get('Nama'))

# LATIHAN DICTIONARY
identitas = {
    'Nama' : 'Farhan',
    'TTL' : 'Bekasi, 15 Agustus 1997',
    'Alamat' : 'Kemang Pratama',
    'Pekerjaan' : 'Freelance'
}
pendidikan = {
    'SD' : 'Victory',
    'SMP' : 'Al-Azhar',
    'SMA' : 'Labschool',
    'S1' : 'TI UNPAR'
}
portofolio = {
    'Himpunan' : 'Majalah',
    'Jurusan' : 'Bantu UMKM'
}

def tampilid():
    for i in identitas:
        print(identitas[i])
def tampilpd():
    for j in pendidikan:
        print(pendidikan.get(j))
def tampilpt():
    for k in portofolio:
        print(portofolio.get(k))

# print('1. Identitas')
# print('2. Pendidikan')
# print('3. Portofolio')
# pilih = input('Pilih yang mana? ')
# if(pilih == '1'):
#     tampilid()
# elif(pilih == '2'):
#     tampilpd()
# elif(pilih == '3'):
#     tampilpt()
# else:
#     print('Masukkan pilihan yang benar')

# MENGGANTI KOMPONEN DALAM DICTIONARY
# identitas['Nama'] = 'Rizky'
# identitas['TTL'] = 'Jakarta, 14 Juli 1996'
# tampilid()

# LATIHAN BESAR
film = {
    1 : 'Shrek',
    2 : 'Sonic'
}
jadwal = {
    1 : 'Siang',
    2 : 'Malam'
}
histori = [

]

row1 = '0000000000'
row2 = '0000000000'

stop = False
while(not stop):
    print('1. Pesan Tiket')
    print('2. Lihat History')
    print('3. Keluar')
    pilihan = input('Tentukan pilihan : ')
    if(pilihan == '1'):
        stop = False
        print('List Film:')
        for i in film:
            print(str(i) + '. ' + film[i])
        pilihfilm = input('Silahkan pilih film: ')
        print('Pilih jadwal film ' + film[int(pilihfilm)] + ': ')
        for j in jadwal:
            print(str(j) + '. ' + jadwal[j])
        pilihjadwal = input('Pilihan: ')
        jumlahpesan = input('Untuk berapa tiket: ')
        for z in range(int(jumlahpesan)):
            if(int(jumlahpesan)>0 and int(jumlahpesan)<=10):
                row = input('Row: ')
                seat = input('Seat: ')
                print('Tempat Duduk')
                if(row == '1'):
                    row1 = row1[:int(seat)-1] + 'X' + row1[int(seat):]
                    print(row1)
                    print(row2)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(row == '2'):
                    row2 = row2[:int(seat)-1] + 'X' + row2[int(seat):]
                    print(row1)
                    print(row2)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                else:
                    print('Pilih antara row 1 atau row 2')
            else:
                print('Maks tiket dibeli hanya 10')
    elif(pilihan == '2'):
        stop = False
        for y in histori:
            print(y)
    elif(pilihan == '3'):
        stop = True
        
