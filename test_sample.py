def simple(x):
    return x + 1


def medium(x, y):
    if x > 0:
        if y > 0:
            return x + y
        else:
            return x
    elif x == 0:
        return y
    else:
        return 0


def complex_func(data):
    result = []

    for item in data:
        if item > 0:
            for i in range(item):
                if i % 2 == 0:
                    result.append(i)
                else:
                    result.append(-i)

        elif item == 0:
            result.append(0)

        else:
            try:
                result.append(abs(item))
            except Exception:
                result.append(0)

    return result