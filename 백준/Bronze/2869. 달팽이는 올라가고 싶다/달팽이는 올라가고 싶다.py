from sys import stdin as si
a,b,v=map(int,si.readline().split())
if a>=v: print(1)
else:
    d=int((v-b)/(a-b))
    print(d) if (v-b)%(a-b)==0 else print(d+1)