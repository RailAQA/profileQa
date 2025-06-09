#Ссылка на задачу: https://stepik.org/lesson/326725/step/7?unit=310010

# Решение
n = int(input())
squares = [el ** 2 for el in range(1, n + 1)]

for el in squares:
    print(el)