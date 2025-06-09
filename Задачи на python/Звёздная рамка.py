#Ссылка на задачу: https://stepik.org/lesson/294080/step/4?unit=275759

# Решение
n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*' * 19, sep='')
    else:
        print('*', '*', sep='                 ')