stop = False
arr = []

# FUNSGI ISI ARRAY
def isiArray():
    jumlah = input('Berapa data yang ingin dimasukkan? ')
    for i in range(int(jumlah)):
        data = int(input('Masukkan data ke-' + str(i+1) + ': '))
        arr.append(data) 
# FUNSGI LIHAT ARRAY
def lihatArray():
    print('Isi array: ')
    print(arr)
# FUNGSI URUT KECIL KE BESAR
def asc(arr):
    for j in range(len(arr)):
        for k in range(j+1, len(arr)):
            if(arr[j] > arr[k]):
                arr[j], arr[k] = arr[k], arr[j]
    return arr
# FUNGSI URUT BESAR KE KECIL
def desc(arr):
    for j in range(len(arr)):
        for k in range(j+1, len(arr)):
            if(arr[j] < arr[k]):
                arr[j], arr[k] = arr[k], arr[j]
    return arr
# FUNGSI HITUNG GANJIL
ganjil = []
def hitungGanjil(arr):
    ganjil = []
    for i in range(len(arr)):
        if(arr[i] % 2 != 0):
            ganjil.append(arr[i])
    return ganjil
# FUNGSI HITUNG GENAP
genap = []
def hitungGenap(arr):
    genap = []
    for i in range(len(arr)):
        if(arr[i] % 2 == 0):
            genap.append(arr[i])
    return genap

while(not stop):
    print('Main Menu')
    print('1. Isi Array')
    print('2. Lihat Array')
    print('3. Sort Array')
    print('4. Nilai Tertinggi dan Terrendah')
    print('5. Jumlah Ganjil dan Genap')
    print('6. Keluar')
    pilih = input('Pilih yang mana? ')
    if(pilih == '1'):
        stop = False   
        isiArray()
    elif(pilih == '2'):
        stop = False
        lihatArray()
    elif(pilih == '3'):
        stop = False
        print('1. Ascending')
        print('2. Descending')
        jenissort = input('Pilih yang mana? ')
        if(jenissort == '1'):
            print(asc(arr))
        elif(jenissort == '2'):
            print(desc(arr))
        else:
            print('Masukkan pilihan yang benar')
    elif(pilih == '4'):
        stop = False
        print('1. Nilai Tertinggi')
        print('2. Nilai Terrendah')
        jenisnilai = input('Pilih yang mana? ')
        if(jenisnilai == '1'):
            maks = desc(arr)
            print('Nilai Tertinggi: ' + str(maks[0]))
        elif(jenisnilai == '2'):
            mins = asc(arr)
            print('Nilai Tertinggi: ' + str(mins[0]))
        else:
            print('Masukkan pilihan yang benar')
    elif(pilih == '5'):
        stop = False
        print('1. Nilai Ganjil')
        print('2. Nilai Genap')
        jenisangka = input('Pilih yang mana? ')
        if(jenisangka == '1'):
            hasilGanjil = hitungGanjil(arr)
            print('Terdapat ' + str(len(hasilGanjil)) + ' angka ganjil')
            print('Angka-angka ganjil:')
            print(hasilGanjil)
        elif(jenisangka == '2'):
            hasilGenap = hitungGenap(arr)
            print('Terdapat ' + str(len(hasilGenap)) + ' angka genap')
            print('Angka-angka genap:')
            print(hasilGenap)
    elif(pilih == '6'):
        stop = True
    else:
        print('Masukkan pilihan yang benar')

    

