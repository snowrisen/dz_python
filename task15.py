# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.
import random 

melons = int(input('Введите количество арбузов'))
mass_melons = random.randint(1,30000)
print(f'Масса 1-го арбуза : {mass_melons} ')
if mass_melons > 30000:
    print('Вы ввели не верную массу')
else:

    min_melons = mass_melons
    max_melons = mass_melons
    for i in range(1,melons,1):
        mass_melons = random.randint(1,30000)
        print(f'Масса {i+1} {mass_melons}')
        # if mass_melons > 30000:
            # print('Вы ввели неверную массу арбуза')
        # else:
        if(min > mass_melons):
                    min = mass_melons
        if(max < mass_melons):
                    max = mass_melons
                
    print(f"Масса лёгкого арбуза = {min}")
    print(f"Масса тяжёлого арбуза = {max}")


# # period = int(input('Period: '))
# # if period > 100 or period < 1:
# #     raise 'период должен быть от 1 до 100'
# Flag =False
# while not flag:
#     period = int(input('Period: '))
#     if not (period > 100 or period < 1):
#         flag = True


# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

A = int(input("Ведите число фибоначчи "))     

if A == 0:
    print("Номер заданного числа Фиббоначи: 0")

elif A == 1:
    print(f"Номер заданного числа Фиббоначи: 1 или 2")

elif (A < 0):
    print("-1")
else:
    fib1 = 0 
    fib2 = 1
    fib3 = 1
    FibIndx = 2  # начинаем порядковый отсчет с номера 2, так как первые два числа нам уже известны 

    while (fib2 < A):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        FibIndx += 1

    print (f'Номер заданного числа Фиббоначи:  {FibIndx}')
