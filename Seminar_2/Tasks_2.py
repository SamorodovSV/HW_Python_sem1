# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11



# N = input()
# sum = 0

# for result in N:
#     if result.isdigit():
#         sum += int(result)

# print('Сумма', sum)


# ------------------------------------------------------------------


# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# a = []
# res = 1
# for i in range(1, n+1):
#     res *= i
#     print(res, end =' ')


# ------------------------------------------------------------------

# Задача 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

N = int(input('Введите число = количеству элементов:'))
a = list()

res = 0
for i in range(1, N+1):
    res += (1 + 1/i)**i
print(round(res, 2)) 