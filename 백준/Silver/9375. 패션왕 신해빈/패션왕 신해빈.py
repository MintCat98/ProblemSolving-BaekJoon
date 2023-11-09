from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    # Get clothes
    d = {}
    for _ in range(int(input())):
        item, category = input().split()
        if category not in d:
            d[category] = 2  # empty 포함
        else:
            d[category] += 1
    count = 1
    for v in d.values():
        count *= v
    print(count - 1)
