list = [1, 2, 3, 4, 5, 6]
list_odds = [item for item in list if item % 2 == 0]

print(list_odds)

zeros = [0 for _ in list]

print(zeros)

pairs = [
    (x, y)
    for x in range(2)
    for y in range(2)
]

print(pairs)