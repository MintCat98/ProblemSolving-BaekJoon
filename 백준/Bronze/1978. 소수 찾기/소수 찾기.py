from sys import stdin as si

def pr(n):
    if n==1: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return 0
    return 1

n=int(si.readline())
l=list(map(int,si.readline().split()))
c=0
for e in l:
    if pr(e)==1: c+=1
    else: c+=0
print(c)