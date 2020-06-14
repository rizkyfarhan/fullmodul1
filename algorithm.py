# ------------------------------------ PERTEMUAN KEDELAPAN ------------------------------------

# FIZZBUZZ (HASIL KE BAWAH)
# jumlah = int(input('Masukkan jumlah: '))
# def bilprima(i):
#     pembagi = 0
#     for j in range(2,jumlah):
#         if i % j == 0:
#             pembagi += 1
#         else:
#             pembagi += 0
#     if pembagi == 1:
#         print('prima')
#     else:
#         print('bukan')

# for i in range(1, jumlah+1):
#     if(i % 63 == 0):
#         print('FizzBuzz')
#         bilprima(i)
#     elif(i % 7 == 0):
#         print('Fizz')
#         bilprima(i)
#     elif(i % 9 == 0):
#         print('Buzz')
#         bilprima(i)
#     else:
#         print(i)
#         bilprima(i)


# FIZZBUZZ (HASIL LANGSUNG)
# jumlah = int(input('Masukkan jumlah: '))
# for i in range(1, jumlah+1):
#     if(i % 7 == 0 and i % 9 == 0):
#         pembagi = 0
#         for j in range(2,jumlah+1):
#             if i % j == 0:
#                 pembagi += 1
#             else:
#                 pembagi += 0
#         if pembagi == 1:
#             print('FizzBuzzPrima')
#         else:
#             print('FizzBuzzBukan')
#     elif(i % 7 == 0 and i % 9 != 0):
#         pembagi = 0
#         for j in range(2,jumlah+1):
#             if i % j == 0:
#                 pembagi += 1
#             else:
#                 pembagi += 0
#         if pembagi == 1:
#             print('FizzPrima')
#         else:
#             print('FizzBukan')
#     elif(i % 9 == 0 and i % 7 != 0):
#         pembagi = 0
#         for j in range(2,jumlah+1):
#             if i % j == 0:
#                 pembagi += 1
#             else:
#                 pembagi += 0
#         if pembagi == 1:
#             print('BuzzPrima')
#         else:
#             print('BuzzBukan')
#     else:
#         pembagi = 0
#         for j in range(2,jumlah+1):
#             if i % j == 0:
#                 pembagi += 1
#             else:
#                 pembagi += 0
#         if pembagi == 1:
#             print(str(i) + ' Prima')
#         else:
            # print(str(i) + ' Bukan')


# FIBONACCI
# def fibo(urut):
#     data = [1, 1, 2]
#     for i in range(0, urut):
#         data.append(data[i] + data[i+2])
#     return data[urut-1]
# print(fibo(8))


# REVERSE LIST IN PLACE
# def fibo(urut):
#     data = [3, 7]
#     for i in range(2, urut):
#         data.append(data[i-2] + data[i-1])
#     return data
# print(fibo(10))

# def reverseList():
#     li = fibo(10)
#     for i in range(0, (len(li)//2)):
#         templi = li[i]
#         li[i] = li[len(li) - 1 - i]
#         li[len(li) - 1 - i] = templi
#     return li
# print(reverseList())


# BUBBLE SORT
def fibo(urut):
    data = [18, 5, 29, 2]
    for i in range(4, urut):
        data.append(data[i-4] + data[i-1])
    return data
print(fibo(8))

def reverseList():
    li = fibo(8)
    for i in range(0, (len(li)//2)):
        templi = li[i]
        li[i] = li[len(li) - 1 - i]
        li[len(li) - 1 - i] = templi
    return li
print(reverseList())

def bubblesort():
    li = fibo(8)
    for i in range(len(li),0,-1):
        for j in range(0,i-1):
            if(li[j] > li[j+1]):
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
    return li
print(bubblesort())