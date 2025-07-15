a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x * 2 - x, a)))


a_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(x):
    return x % 2 == 0

    
new_a_2 = filter(is_even, a_2)
print(list(new_a_2))