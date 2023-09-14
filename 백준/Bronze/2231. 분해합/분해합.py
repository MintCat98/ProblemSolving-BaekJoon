n = int(input())
m = n
c = 0     # 자릿수
while m != 0:
    m = m//10
    c += 1
l = []
for i in range(n-9*c, n+1):
    if i <= 0:
        continue
    sum = i
    char = str(i)
    for j in range(len(char)):
        sum += int(char[j])
    if sum == n:
        l.append(i)
print(min(l)) if len(l) != 0 else print(0)