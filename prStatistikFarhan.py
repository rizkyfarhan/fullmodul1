import random
from collections import Counter
import math
li = []

def menu():
    stop = False
    while(not stop):
        print('1. Urut Data')
        print('2. Rata-Rata')
        print('3. Median')
        print('4. Modus')
        print('5. Variansi')
        print('6. Standar Deviasi')
        print('7. Skewness')
        print('8. Kurtosis')
        print('9. Keluar')
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            print('1. Urutkan Ascending')
            print('2. Urutakn Descending')
            jenisurut = input('Pilih jenis urut: ')
            if jenisurut == '1':
                print('Hasil pengurutan secara ascending: ' + str(urutasc(li)))
            elif jenisurut == '2':
                print('Hasil pengurutan secara descending: ' + str(urutdesc(li)))
            else:
                print('Masukkan pilihan yang benar')
        elif pilihan == '2':
            print('Rata-rata dari data adalah: ' + str(ratarata(li)))
        elif pilihan == '3':
            print('Nilai median dari data adalah: ' + str(nilaitengah(li)))
        elif pilihan == '4':
            print(modus(li))
        elif pilihan == '5':
            print('Variansi dari data adalah: ' + str(variansi(li)))
        elif pilihan == '6':
            print('Standar deviasi dari data adalah: ' + str(stdeviasi(li)))
        elif pilihan == '7':
            print('Nilai skewness dari data adalah: ' + str(skewness(li)))
        elif pilihan == '8':
            print('Nilai kurtosis dari data adalah: ' + str(kurtosis(li)))
        elif pilihan == '9':
            stop = True
        else:
            print('Masukkan pilihan yang benar')

def genrandom():
    jumlahdata = int(input('Masukkan jumlah data: '))
    for _ in range(jumlahdata):
        rand = random.randint(1,10)
        li.append(rand)
    return li 

def urutasc(li):
    for i in range(len(li)):
        for j in range(i+1):
            if(li[i] < li[j]):
                li[i], li[j] = li[j], li[i]
    return li

def urutdesc(li):
    for i in range(len(li)):
        for j in range(i+1):
            if(li[i] > li[j]):
                li[i], li[j] = li[j], li[i]
    return li

def ratarata(li):
    total = 0
    for i in range(len(li)):
        total = total + li[i]
    rata = total / len(li)
    return rata

def nilaitengah(li):
    li = urutasc(li)
    if len(li) % 2 == 0:
        angkabawah = li[(len(li)//2)-1]
        print(angkabawah)
        angkaatas = li[len(li)//2]
        print(angkaatas)
        med = (angkaatas + angkabawah) / 2
        return med
    else:
        med = angkaatas = li[len(li)//2]
        return med

def modus(li):
    n = len(li)
    data = Counter(li)
    datadict = dict(data)
    maxvalue = max(datadict.values())
    hasilmodus = [k for (k, v) in datadict.items() if v == maxvalue]
    if(len(hasilmodus) == n):
        datadict = 'Tidak ada modus'
    else:
        datadict = 'Modus adalah ' + str(hasilmodus)
    return(datadict)
    
def variansi(li):
    rata = ratarata(li)
    jumlahan = 0
    for i in range(len(li)):
        kuadrat = (li[i] - rata) ** 2
        jumlahan = jumlahan + kuadrat
    hasilvariansi = jumlahan / len(li)
    return hasilvariansi

def stdeviasi(li):
    hasilvariansi = variansi(li)
    hasilstdev = math.sqrt(hasilvariansi)
    return hasilstdev

def skewness(li):
    rata = ratarata(li)
    hasilstdev = stdeviasi(li)
    jumlahan = 0
    for i in range(len(li)):
        ptiga = (li[i] - rata) ** 3
        jumlahan = jumlahan + ptiga
    hasilskew = jumlahan / ((len(li)) * (hasilstdev ** 3))
    return hasilskew

def kurtosis(li):
    rata = ratarata(li)
    jatas = 0
    for i in range(len(li)):
        pempat = (li[i] - rata) ** 4
        jatas = jatas + pempat
    jbawah = 0
    for j in range(len(li)):
        kkuadrat = (li[j] - (rata ** 2)) ** 2
        jbawah = jbawah + kkuadrat
    hasilkurtosis = len(li) * (jatas / jbawah)
    return hasilkurtosis

genrandom()
print('Hasil pembangkitan data: ' + str(li))

pilfilt = input('Hilangkan duplikasi pada data? (y/n) ')
if pilfilt == 'y':
    li = set(li)
    li = list(li)
elif pilfilt == 'n':
    li = li
else:
    print('Masukkan pilihan yang benar')

print('Data yang digunakan: ' + str(li))
menu()


