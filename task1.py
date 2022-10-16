#Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.


nums = list(map(float, input().split()))
print(nums)
print(f'The max number in the list : {max(nums)}')
print(f'The minim number in the list : {min(nums)}')