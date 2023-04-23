# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X . 
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# 

# from random import randint
# print('Введите кол-во элементов в массиве!')
# element_n = int(input()) # количество элементов в массиве
# a,b = 1,15 # диапазон, можно задавать через input()
# number = 0 
# num_x = int(input('Введите число X которое хотите сравнить: ')) 
# array = [randint(a,b) for i in range(num_x)] # генерация массива
# print(array)

# min = num_x - array[0]
# index = 0
# for i in (array):
#     count = num_x - array[0]
#     if count < min:
#         min = count
#         index = i
# print(f'Число {array[i]} в списке A наиболее близко по величине к числу {num_x}')

N = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[i]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')

        

N = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')




