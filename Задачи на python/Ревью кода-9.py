#Ссылка на задачу: https://stepik.org/lesson/294080/step/3?unit=275759

# Решение:
count = 0
minimum = -10 ** 9
for i in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > minimum:
            minimum = x
            
if count > 0:
    print(count)
    print(minimum)
else:
    print('NO')