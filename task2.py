# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


def simple(n):
   i = 2
   lst = []
   while i * i <= n:
       while n % i == 0:
           lst.append(i)
           n /= i
       i = i + 1
   if n > 1:
       lst.append(n)
   return lst


n = int(input('Введите число: '))
print(simple(n))