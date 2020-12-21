def bisect2dIt(tree, left = 0, right = 8, front = 0, back = 128):
    for node in tree:
        if node == 'R':
            left  += (right - left)//2
        elif node == 'L':
            right -= (right - left)//2
        elif node == 'B':
            front += (back - front)//2
        elif node == 'F':
            back  -= (back - front)//2

    return front, left


def bisect2d(tree, left = 0, right = 8, front = 0, back = 128):
    if not tree:
        return front, left

    node = tree[0]

    return bisect2d(
        tree[1:],
        left  + (right - left)//2  if node == 'R' else left,
        right - (right - left)//2  if node == 'L' else right,
        front + (back - front)//2 if node == 'B' else front,
        back  - (back - front)//2 if node == 'F' else back
    )


if __name__ == "__main__":
    seat_id = lambda row, col: row*8 + col

    with open('data/day5.txt') as f:
        trees = [line.strip() for line in f]

    # Two solutions, iterative is faster
    seat_ids = set(seat_id(*bisect2dIt(tree)) for tree in trees)

    ma = max(seat_ids)

    # Part 1
    print(max(seat_ids))

    # Part 2
    mi = min(seat_ids)
    all_seats = set(range(mi, ma+1))
    print(all_seats.difference(seat_ids).pop())