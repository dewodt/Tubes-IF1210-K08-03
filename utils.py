import datetime


# Mengembalikan waktu sekarang dalam detik
def TimeNow():
    return int(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))


# Menerima range min, max, dan seed dan mengembalikan 3 bilangan random
def RandomLCG(min, max, seed):
    random_array = [0, 0, 0]
    a, c, m = 1103515245, 12345, 2**31 - 1
    xn = (a * seed + c) % m

    for i in range(3):
        normalized_value = int(min + (max - min) * (xn / m))
        random_array[i] = normalized_value
        xn = (a * xn + c) % m

    return random_array
