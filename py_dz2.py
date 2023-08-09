'''Задача 1'''

print(a.
      count(1)
        if (a := [int(input()) 
                  for i in range(int(input()))]).
                  count(1) < a.
                  count(0)
                    else a.
                    count(0))

'''Задача 2'''
# Вариант 2. Решить эту задачу можно "перебором значений" в цикле
# X + Y = 5, X * Y = 6, X = 6/Y, 6/Y + Y = 5, 6/Y = 5 - Y, 6 = 5Y - Y**2, 0 = 5Y - Y**2 - 6, Y**2 - 5Y + 6 = 0
# ax^2 + bx + c = 0, Y = (-b ± √(b^2 - 4ac)) / 2a
# Y = (S + (S**2 - 4*P)) / 2, X = (S - (S**2 - 4*P)) / 2

S = 5
P = 6

Y = int((S + (S**2 - 4*P)) / 2)
X = int((S - (S**2 - 4*P)) / 2)

print(X, Y)

#Задача 3

N = 1000
k = 0
result = 0

for i in range(N):
    result = 2 ** k
    if result < N:
        print(result, end=' ')
        k += 1
    else:
        break