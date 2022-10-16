#2. Найдите корни квадратного уравнения 
# Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения 
# корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
from math import sqrt

def radical_number(a,b,c):
    d = pow(b,2)-4*a*c
    if d > 0:
        x1 = (-b-sqrt(d))//2*a
        x2 = (-b+sqrt(d))//2*a
        return x1, x2
    else:
        return 0      
a = int(input('Enter the numbers'))
b = int(input('Enter the numbers'))  
c = int(input('Enter the numbers'))
print(radical_number(a,b,c))
