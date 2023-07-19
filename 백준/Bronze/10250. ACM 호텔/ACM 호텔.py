from sys import stdin as si
for _ in range(int(si.readline())):
    h,w,n=map(int,si.readline().split())
    a=n%h; b=n//h+1
    print(h*100+n//h) if a==0 else print(a*100+b)