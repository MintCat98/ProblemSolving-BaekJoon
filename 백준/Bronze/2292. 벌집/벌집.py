from sys import stdin as si
n=int(si.readline())
r=1; i=1
while True:
    if r>=n: break
    r+=6*i
    i+=1
print(i)