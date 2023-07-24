from sys import stdin as si
a,b=map(int,si.readline().split())
if a<b: a,b=b,a
c,d=a,b
while True:
    r=c%d
    if r==0: break
    c,d=d,r
print(d)
print(int(a*b/d))