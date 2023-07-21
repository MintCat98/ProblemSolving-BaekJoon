from sys import stdin as si
while True:
    a,b,c=map(int,si.readline().split())
    if a==0: break
    if a<b: a,b=b,a
    if a<c: a,c=c,a
    print('right') if a**2==b**2+c**2 else print('wrong')