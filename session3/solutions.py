from functools import reduce
from operator import add, mul
import re
import heapq


def sum(xs):
    return reduce(add, xs, 0)


def product(xs):
    return reduce(mul, xs, 1)


def mean(xs):
    return sum(xs) / len(xs)


def flatten(xs):
    return [x for sublist in xs for x in sublist]


def sum2(xs, ys):
    return [(x + y) for (x, y) in zip(xs + [0] * (len(ys) - len(xs)), ys + [0] * (len(xs) - len(ys)))]


def threes_or_fives(n):
    return [x for x in range(0, n) if x % 3 == 0 or x % 5 == 0]


def filtered_even(xs):
    return [x for x in xs if x % 2 == 0]


def filtered_text(xs):
    return [x for x in xs if re.match('^[a-z]', x)]


def rot(xs, n):
    return xs[n:] + xs[:n]


def uniques(xs):
    return sorted(set(xs))


def bin_search(xs, x):
    l, r = 0, len(xs)

    while l + 1 < r:
        m = (l + r) // 2

        if xs[m] <= x:
            l = m
        else:
            r = m

    return l


def merge(xs, ys):
    i, j, zs = 0, 0, []

    while i < len(xs) and j < len(ys):
        if xs[i] <= ys[j]:
            zs.append(xs[i])
            i += 1
        else:
            zs.append(ys[j])
            j += 1

    zs.extend(xs[i:])
    zs.extend(ys[j:])
    return zs


def merge2(xs, ys):
    return [x for x in heapq.merge(xs, ys)]


def merge_sort(xs):
    return xs if len(xs) <= 1 else merge(merge_sort(xs[:len(xs) // 2]), merge_sort(xs[len(xs) // 2:]))


def poly_sum(xs, ys):
    return sum2(xs, ys)


def poly_prod(xs, ys):
    zs = [0] * (len(xs) + len(ys))

    for (i, x) in enumerate(xs):
        for (j, y) in enumerate(ys):
            zs[i + j] += x * y

    while len(zs) > 0 and zs[-1] == 0:
        zs.pop()

    return zs
