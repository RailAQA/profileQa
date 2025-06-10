#Ссылка на задачу: https://stepik.org/lesson/327221/step/3?unit=310520

# Решение:
a = input()
my_list = [int(x) for x in a.split()]

print(f'{"+".join(str(x) for x in my_list)}={sum(my_list)}')