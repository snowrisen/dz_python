# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

print('Введите номер вашего билета!')
num = input()

def happyticket(num):
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    res1 = a+b+c
    a2 = int(num[3])
    b2 = int(num[4])
    c2 = int(num[5])
    res2 =a2+b2+c2
    if res1 == res2:
        print('Поздравляю у вас счастливый билет!')
    else:
        print('Очень жаль, у вас несчастливый билет!')
print()
happyticket(num)