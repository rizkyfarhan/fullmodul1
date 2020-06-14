film = {
    1 : 'Shrek',
    2 : 'Sonic'
}
jadwal = {
    1 : 'Siang',
    2 : 'Malam'
}
histori = []

p111 = '0000000000'
p112 = '0000000000'
p121 = '0000000000'
p122 = '0000000000'
p211 = '0000000000'
p212 = '0000000000'
p221 = '0000000000'
p222 = '0000000000'

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
                if(pilihfilm == '1' and pilihjadwal == '1' and row == '1'):
                    p111 = p111[:int(seat)-1] + 'X' + p111[int(seat):]
                    print(p111)
                    print(p112)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(pilihfilm == '1' and pilihjadwal == '1' and row == '2'):
                    p112 = p112[:int(seat)-1] + 'X' + p112[int(seat):]
                    print(p111)
                    print(p112)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(pilihfilm == '1' and pilihjadwal == '2' and row == '1'):
                    p121 = p121[:int(seat)-1] + 'X' + p121[int(seat):]
                    print(p121)
                    print(p122)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(pilihfilm == '1' and pilihjadwal == '2' and row == '2'):
                    p122 = p122[:int(seat)-1] + 'X' + p122[int(seat):]
                    print(p121)
                    print(p122)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(pilihfilm == '2' and pilihjadwal == '1' and row == '1'):
                    p211 = p211[:int(seat)-1] + 'X' + p211[int(seat):]
                    print(p211)
                    print(p212)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(pilihfilm == '2' and pilihjadwal == '1' and row == '2'):
                    p212 = p212[:int(seat)-1] + 'X' + p212[int(seat):]
                    print(p211)
                    print(p212)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(pilihfilm == '2' and pilihjadwal == '2' and row == '1'):
                    p221 = p221[:int(seat)-1] + 'X' + p221[int(seat):]
                    print(p221)
                    print(p222)
                    histori.append(film[int(pilihfilm)] + ' ' + jadwal[int(pilihjadwal)])
                elif(pilihfilm == '2' and pilihjadwal == '2' and row == '2'):
                    p222 = p222[:int(seat)-1] + 'X' + p222[int(seat):]
                    print(p221)
                    print(p222)
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