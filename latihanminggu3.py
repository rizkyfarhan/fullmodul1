# SOAL 1
# BELAH KETUPAT
# class belahketupat():
#     def __init__(self, sisi, diagonal):
#         self.sisi = sisi
#         self.diagonal = diagonal
#     def luas(self):
#         hasilluas = (self.diagonal * self.diagonal) / 2
#         return hasilluas
#     def keliling(self):
#         hasilkel = self.sisi * 4
#         return hasilkel

# sisi = int(input('Masukkan panjang sisi belah ketupat: '))
# diagonal = int(input('Masukkan panjang diagonal belah ketupat: '))
# sisi1 = belahketupat(sisi, diagonal)

# print('Luas belah ketupat dengan panjang sisi ' + str(sisi) + ' adalah ' + str(sisi1.luas()))
# print('Keliling belah ketupat dengan panjang diagonal ' + str(diagonal) + ' adalah ' + str(sisi1.keliling()))


# SOAL 2
# setengah lingkaran, layang layang, jajar genjang, belah ketupat, trapesium
# class setlingkaran():
#     def __init__(self, jarijari):
#         self.jarijari = jarijari
#     def lsetling(self):
#         lsl = (3.14 * self.jarijari * self.jarijari) / 2
#         return lsl
#     def ksetling(self):
#         ksl = (3.14 * (self.jarijari * 2)) / 2
#         return ksl

# jarijari = int(input('Masukkan jari-jari lingkaran: '))
# jarijari1 = setlingkaran(jarijari)

# print('Luas setengah lingkaran dengan jari-jari ' + str(jarijari) + ' adalah ' + str(jarijari1.lsetling()))
# print('Keliling setengah lingkaran dengan jari-jari ' + str(jarijari) + ' adalah ' + str(jarijari1.ksetling()))


# class layanglayang():
#     def __init__(self, d1, d2, s1, s2):
#         self.d1 = d1
#         self.d2 = d2
#         self.s1 = s1
#         self.s2 = s2
#     def llayang(self):
#         ll = (self.d1 * self.d2) / 2
#         return ll
#     def klayang(self):
#         kl = 2 * (self.s1 + self.s2)
#         return kl

# d1 = int(input('Masukkan panjang diagonal 1 layang-layang: '))
# d2 = int(input('Masukkan panjang diagonal 2 layang-layang: '))
# s1 = int(input('Masukkan sisi pendek layang-layang: '))
# s2 = int(input('Masukkan sisi panjang layang-layang: '))
# layang1 = layanglayang(d1, d2, s1, s2)

# print('Luas layang-layang dengan panjang diagonal satu ' + str(d1) + ' dan diagonal dua '+ str(d2) + ' adalah ' + str(layang1.llayang()))
# print('Keliling layang-layang dengan sisi pendek ' + str(s1) + ' dan sisi panjang '+ str(s2) + ' adalah ' + str(layang1.klayang()))


# class jajargenjang():
#     def __init__(self, a, b, t):
#         self.a = a
#         self.b = b
#         self.t = t
#     def ljgenjang(self):
#         ljg = self.a * self.t
#         return ljg
#     def kjgenjang(self):
#         kjg = 2 * (self.a + self.b)
#         return kjg

# a = int(input('Masukkan alas dari jajar genjang: '))
# b = int(input('Masukkan sisi miring dari jajar genjang: '))
# t = int(input('Masukkan tinggi dari jajar genjang: '))
# genjang1 = jajargenjang(a, b, t)

# print('Luas jajar genjang dengan alas ' + str(a) + ' dan tinggi '+ str(t) + ' adalah ' + str(genjang1.ljgenjang()))
# print('Keliling jajar genjang dengan alas ' + str(a) + ' dan sisi miring '+ str(b) + ' adalah ' + str(genjang1.kjgenjang()))


# class belahketupat():
#     def __init__(self, sisi, diagonal):
#         self.sisi = sisi
#         self.diagonal = diagonal
#     def lbketupat(self):
#         hasilluas = (self.diagonal * self.diagonal) / 2
#         return hasilluas
#     def kbketupat(self):
#         hasilkel = self.sisi * 4
#         return hasilkel

# sisi = int(input('Masukkan panjang sisi belah ketupat: '))
# diagonal = int(input('Masukkan panjang diagonal belah ketupat: '))
# sisi1 = belahketupat(sisi, diagonal)

# print('Luas belah ketupat dengan panjang sisi ' + str(sisi) + ' adalah ' + str(sisi1.lbketupat()))
# print('Keliling belah ketupat dengan panjang diagonal ' + str(diagonal) + ' adalah ' + str(sisi1.kbketupat()))


# class trapesium():
#     def __init__(self, sa, sb, mki, mka, t):
#         self.sa = sa
#         self.sb = sb
#         self.mki = mki
#         self.mka = mka
#         self.t = t
#     def ltrap(self):
#         lt = (self.sa + self.sb) * self.t / 2
#         return lt
#     def ktrap(self):
#         kt = self.sa + self.sb + self.mki + self.mka
#         return kt

# sa = int(input('Masukkan panjang sisi atas trapesium: '))
# sb = int(input('Masukkan panjang sisi bawah trapesium: '))
# mki = int(input('Masukkan panjang sisi miring kiri trapesium: '))
# mka = int(input('Masukkan panjang sisi miring kanan trapesium: '))
# t = int(input('Masukkan tinggi dari trapesium: '))
# trap1 = trapesium(sa, sb, mki, mka, t)

# print('Luas trapesium adalah ' + str(trap1.ltrap()))
# print('Keliling trapesium adalah ' + str(trap1.ktrap()))


# SOAL 3
# listumur = list()
# class student():
#     def __init__(self, nama, nomor, umur):
#         self.nama = nama
#         self.nomor = nomor
#         self.umur = umur
#     def display(self):
#         data = self.umur
#         listumur.append(data)
#         print('Nama siswa ini adalah ' + self.nama + ' dengan nomor induk ' + str(self.nomor) + ' dan berumur ' + str(self.umur) + ' tahun')
        
# student1 = student('Arief', 10001, 21)
# student2 = student('Ariyanda', 10002, 23)
# student3 = student('Raihan', 10003, 20)
# student4 = student('Prissil', 10004, 22)
# student5 = student('Farhan', 10005, 21)

# student1.display()
# student2.display()
# student3.display()
# student4.display()
# student5.display()

# hasilrata = sum(listumur) / len(listumur)
# print('Rata-rata umur siswa di kelas adalah ' + str(hasilrata))


# SOAL 4
# def timeconverter(inputdetik):
#     if inputdetik >= 3600:
#         jam = inputdetik // 3600
#         sisadarijam = inputdetik % 3600
#         menit = sisadarijam // 60
#         detik = sisadarijam % 60
#         if jam < 10:
#             jam = '0' + str(jam)
#         if menit < 10:
#              menit = '0' + str(menit) 
#         if detik < 10:
#             detik = '0' + str(detik)
#         print(str(jam) + ':' + str(menit) + ':' + str(detik))
#     else:
#         menit = inputdetik // 60
#         detik = inputdetik % 60
#         if menit < 10:
#             menit = '0' + str(menit) 
#         if detik < 10:
#             detik = '0' + str(detik)
#         print('00:' + str(menit) + ':' + str(detik))

# inputdetik = int(input('Detik yang akan dikonversikan: '))
# timeconverter(inputdetik)

# SOAL 5
# def segitiga(n):
#     z = ''
#     a = 1
#     temp = list()
#     kumpulan = list()
#     for i in range(0, n):
#         for j in range(n-i):
#             z += '  '
#         for k in range(i+1):
#             z += str(a).ljust(4, ' ')
#             temp.append(a)
#             a += 2
#         kumpulan.append(temp)
#         temp = list()
#         z += '\n'
#     print(kumpulan)
#     print(z)
#     print('Hasil penjumlahan baris terakhir: ' + str(sum(kumpulan[-1])))

# segitiga(7)

# SOAL 6
# def putarkata():
#     kalimat = input('Tulis kalimat: ')
#     kata = kalimat.split()
#     hasil = list()
#     for i in range(len(kata)):
#         if len(kata[i]) < 5:
#             hasil.append(kata[i])
#         else:
#             putar = (kata[i])[-1::-1]
#             hasil.append(putar)
#     print(' '.join(map(str,hasil)))

# putarkata()

# SOAL 7
# def pindahnol(list):
#     for i in range(len(list)):
#         if list[i] != 0:
#             continue
#         elif list[i] == 0:
#             list.append(list[i])
#             list.remove(list[i])
#     print(list)

# pindahnol([False, 1, 0, 1, 0, 2, 0, 1, 3, 'a'])

# SOAL 8
pnol = 1000
gro = 2
mig = 50
maks = 1200
year = 0

def tahunakhir(pnol, gro, mig, maks, year):
    while pnol < maks:
        pnol += (pnol * gro / 100) + mig
        year += 1
    print(year)

tahunakhir(pnol, gro, mig, maks, year)