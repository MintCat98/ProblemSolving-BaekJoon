from sys import stdin
input = stdin.readline
n, m, b = map(int, input().split())
land = []
for _ in range(n):
    land += list(map(int, input().split()))
at, ah = 1e9, -1    # answers
maxH, minH = max(land), min(land)

for h in range(minH, maxH+1):
    t = 0     # Init time
    dig = 0
    place = 0
    # Calculate nums of dig and place
    for y in land:
        if y == h:
            continue
        elif y > h:
            dig += (y-h)
        else:
            place += (h-y)
    # Check Availability
    if place > (b+dig):
        continue
    else:
        t = 2*dig+place
        # min time & max height
        if t <= at:
            at = t
            if h > ah:
                ah = h
print(at, ah)