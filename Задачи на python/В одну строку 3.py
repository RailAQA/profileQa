#Ссылка на задачу: https://stepik.org/lesson/326725/step/11

# Решение
[print(int(i) ** 2 , end=' ') for i in input().split(' ')  if int(i) % 2 == 0 and (not (int(i) ** 2) % 10 == 4)]