def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x


def RandomGenerator(min, max, seed):
    random_array = [0, 0, 0]
    a, c, m = 1103515245, 12345, 2**31 - 1
    random_value = lcg(seed, a, c, m)

    for i in range(3):
        normalized_value = int(min + (max - min) * (next(random_value) / m))
        random_array[i] = normalized_value

    return random_array
