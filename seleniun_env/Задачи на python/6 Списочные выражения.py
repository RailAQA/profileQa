#Ссылка на задачу: https://stepik.org/lesson/326725/step/8?unit=310010

# Решение
b = input().split(' ')
n = [int(i) ** 3 for i in b]

for m in n:
    print(m, end=' ')
