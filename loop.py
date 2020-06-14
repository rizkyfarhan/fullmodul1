# ------------------------------------ PERTEMUAN KETIGA ------------------------------------

# angka = 1 

# while(angka <= 10) :
#     print(angka)
#     angka += 1


# listItem = list(range(1,11,2)) 
# print(listItem)

# range -> 
# angka pertama mulainya
# angka kedua selesainya (ga termasuk)
# angka ketiga stepnya (interval)

# for item in range(1,11,2) :
#     print(item)


# LATIHAN 1
# for i in range(1,11) :
#     print('Nomor urut ' + str(i))


# LATIHAN 2
# for i in range(0,51,5) :
#     print('Nomor urut ' + str(i))


# z = ''

# for item in range(0,5):
#     z += ' * '

# print(z)


# z = ''

# for item in range(0,5):
#     z += ' * \n'

# print(z)


# LATIHAN 3
# z = ''
# for i in range(0,5):
#     for i1 in range(0,5):
#         z += ' * '
#     z += '\n'
# print(z)


# LATIHAN 4 
# z = ''
# for i in range(0,10,2):
#     for i1 in range(0,i+1):
#         z += ' * '
#     z += '\n'
# print(z)


# ------------------------------------ PR ------------------------------------

# SOAL 1
z = ''
for i in range(0,5):
    for j in range(0,5-i):
        z += ' * '
    z += '\n'
print(z)

# SOAL 2
z = ''
for i in range(0,5):
    for j in range(0,5-i):
        z += ' * '
    z += '\n'
for i in range(0,5):
    for j in range(0,i+1):
        z += ' * '
    z += '\n'
print(z)

# SOAL 3
z = ''
for i in range(0,19,2):
    for j in range(0,19-i):
        z += ' '
    for k in range(0,i+1):
        z += ' *'
    z += '\n'
print(z)

# SOAL 4
z = ''
for i in range(0,19,2):
    for j in range(0,i+1):
        z += ' '
    for k in range(0,19-i):
        z += ' *'
    z += '\n'
print(z)

# SOAL 5
z = ''
for i in range(0,9,2):
    for j in range(0,9-i):
        z += ' '
    for k in range(0,i+1):
        z += ' *'
    z += '\n'
for i in range(0,9,2):
    for j in range(0,i+1):
        z += ' '
    for k in range(0,9-i):
        z += ' *'
    z += '\n'
print(z)