# 1. Задача. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input('Введите порядковый номер дня недели: '))
# if 0 < day < 6:
#     print( day, '-> Нет. Это будний день')
# else: 
#     print( day, '-> Да. Это выходной день')



# 2. Задача. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))


# 3. Задача. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координату по оси X: '))
# y = int(input('Введите координату по оси Y: '))
# if x>0 and y>0: 
#     print('1 четверть')
# elif x<0 and y>0:
#      print('2 четверть')
# elif x<0 and y<0:
#      print('3 четверть')
# else: 
#     print('4 четверть')