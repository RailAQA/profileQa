#Ссылка на задачу: https://stepik.org/lesson/294080/step/1?unit=275759

# Решение
n = int(input())
s = 0
while n > 0:
    a = n % 10
    if a % 2 == 0:
        s = s + a
    n //= 10
print(s)