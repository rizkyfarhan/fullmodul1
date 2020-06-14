# ------------------------------------ PERTEMUAN KESEMBILAN ------------------------------------

# CLASS - OBJECT ORIENTED PROGRAMMING

# CONTOH 1
# class classKeren:
#     halo = 5
# obj1 = classKeren()
# print(obj1.halo)

# INIT - DIGUNAKAN UNTUK INISIASI PARAMETER
# CONTOH 2
# class manusia:
#     def __init__(self, name, age):
#         self.nama = name
#         self.umur = age
# manusia1 = manusia('Baron', 22)
# print(manusia1)
# print(manusia1.nama)
# print(manusia1.umur)

# LATIHAN 1
# class farhan:
#     def __init__(self, name, age, job, birthplace):
#         self.nama = name
#         self.umur = age
#         self.pekerjaan = job
#         self.tempatlahir = birthplace
# biodata = farhan('Farhan', 22, 'Freelance', 'Bekasi')
# print(biodata.nama)
# print(biodata.umur)
# print(biodata.pekerjaan)
# print(biodata.tempatlahir)
# print(biodata.__dict__)

# CONTOH 3
# class manusia:
#     def __init__(self, name, age):
#         self.nama = name
#         self.umur = age
#     def salamkenal(self, kalimatlanjut):
#         print('Halo nama saya ' + self.nama + kalimatlanjut)

# manusia1 = manusia('Baron', 22)
# manusia1.salamkenal(', nama kamu siapa?')

# EDIT
# manusia1.nama = 'Andi'
# manusia1.pekerjaan = 'Guru'
# print(manusia1.__dict__)

# DELETE
# del manusia1.pekerjaan
# print(manusia1.__dict__)

# LATIHAN 2
# class perkenalan:
#     def __init__(self, name, gender, age):
#         self.nama = name
#         self.jeniskelamin = gender
#         self.umur = age
#     def kalimat(self):
#         print('Nama saya adalah ' + self.nama + ' yang berjenis kelamin ' + self.jeniskelamin + ' dan berusia ' + str(self.umur))

# farhan = perkenalan('Farhan', 'Pria', 22)
# farhan.kalimat()

# farhan.nama = 'Ari'
# farhan.kalimat()

# INHERITANCE
# PARENT CLASS - DITULIS SEPERTI KELAS PADA UMUMNYA
# CHILD CLASS - TURUNAN DARI PARENT CLASS, PARAMETER ADALAH PARENT CLASS

# LATIHAN 3
# class biodata:
#     def __init__(self, name, gender, birthplace):
#         self.nama = name
#         self.jeniskelamin = gender
#         self.kotalahir = birthplace
#     def perkenalan(self):
#         print('Nama saya adalah ' + self.nama + ' yang berjenis kelamin ' + self.jeniskelamin + ' dan lahir di ' + self.kotalahir)

# class tambahan(biodata):
#     def __init__(self, name, gender, birthplace, age, job):
#         super().__init__(name, gender, birthplace)
#         self.umur = age
#         self.pekerjaan = job
#     def perkenalanbaru(self):
#         print('Nama saya adalah ' + self.nama + ' yang berjenis kelamin ' + self.jeniskelamin + ' lahir di ' + self.kotalahir + ' berumur ' + str(self.umur + 2) + ' tahun dan bekerja sebagai ' + self.pekerjaan)
        

# farhan = tambahan('Farhan', 'Pria', 'Bekasi', 22, 'Freelance')
# print(farhan.__dict__)
# farhan.perkenalan()
# farhan.perkenalanbaru()

# LATIHAN 4
class pencariHuruf():
    def __init__(self, teks):
        self.kata = teks
        self.a = 0
    def A(self):
        for i in range(len(self.kata)):
            if self.kata[i] == 'a' or self.kata[i] == 'A':
                self.a = self.a + 1
        return self.a

teks = input('Masukkan kalimat yang diinginkan: ')
penampung = pencariHuruf(teks)

jumlahA = penampung.A()

print('Jumlah huruf A pada kalimat "' + teks + '" adalah: ' + str(jumlahA))
