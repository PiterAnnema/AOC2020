with open('data/day3.txt') as f:
    trees = [line for line in f]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


w = len(trees[0]) - 1
prod = 1
for right, down in slopes:
    count = 0
    x = 0
    for y in range(0, len(trees), down):
        count += trees[y][x%w] == '#'
        x += right

    prod *= count

print(prod)