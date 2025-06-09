#Ссылка на задачу: https://stepik.org/lesson/294080/step/6?unit=275759

# Решение
def q3(value: str):
    return value.count('3')


def last_qty(value: str):
    return value.count(value[-1])


def evens(value: str):
    ints = list(map(int, value))
    return len([d for d in ints if d % 2 == 0])


def sum_more_5(value: str):
    ints = list(map(int, value))
    return sum([d for d in ints if d > 5])


def multi_7(value: str):
    ints = list(map(int, value))
    i = 1
    for d in ints:
        i *= d if d > 7 else 1
    return i


def qty05(value: str):
    ints = list(map(int, value))
    return len([d for d in ints if d == 0 or d == 5])


if __name__ == '__main__':
    inp = input()
    print(q3(inp))
    print(last_qty(inp))
    print(evens(inp))
    print(sum_more_5(inp))
    print(multi_7(inp))
    print(qty05(inp))