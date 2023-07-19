from sys import stdin as si
n=int(si.readline())
r=1
if n!=0:
    for i in range(1,n+1):
        r*=i
    r=str(r)[::-1]
    c=0
    for i in range(500):
        if r[i]=='0': c+=1
        else: break
    print(c)
else: print(0)