from functools import reduce

def part1(numbers):
    l = len(numbers)
    for i in range(l): 
        a = numbers[i]
        for j in range(i+1, l):
            b = numbers[j]
            if a + b == 2020:
                return a * b

def part2(numbers):
    l = len(numbers)
    for i in range(l): 
        a = numbers[i]
        for j in range(i+1, l):
            b = numbers[j]
            if a + b > 2020:
                continue
            for k in range(j+1, l):
                c = numbers[k]
                if a + b + c == 2020:
                    return a * b * c


def findAddends(numbers, n_addends, target, start = 0):
    for i in range(start, len(numbers)):
        n = numbers[i]
        if n_addends > 1:
            res = findAddends(numbers, n_addends-1, target-n, i + 1)
            if res is not None:
                return [n] + res

        elif target == n:
                return [n]


if __name__ == "__main__":
    with open('data/day1.txt') as f:
        numbers = list(map(lambda line: int(line.strip()), f))

    # These solutions are ugly
    print(part1(numbers))
    print(part2(numbers))

    # Generalized solution
    print(reduce(lambda x, y: x*y, findAddends(numbers, 3, 2020)))