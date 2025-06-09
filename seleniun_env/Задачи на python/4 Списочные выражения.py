#Ссылка на задачу: https://stepik.org/lesson/326725/step/6?thread=solutions&unit=310010

# Решение
s = [i for i in range(100, 1000) if list(str(i))[0] == list(str(i))[-1]]
print (s)