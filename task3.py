#Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# a = 84
# b = 648
#num_1 = int(input('Enter the number:'))
#num_2 = int(input('Enter the number:'))
# i = min(num_1, num_2)
# while True:
#     if i % num_1 == 0 and i % num_2 == 0:
#         break
#     i += 1
# print(i)
import math

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
res = math.lcm(a, b)
print(f'НОК =', res)

# nodd = num_1 % num_2
# nodd2 = num_2 % nodd  #if 0 return nodd
# result = num_1 * num_2 // nodd2
# print(result)