from sys import stdin as si
n=int(si.readline())
s=[]
for i in range(n):
    cmd=si.readline()[:-1]
    dc=cmd[:3]
    if dc=='pus':
        e=int(cmd[5:])
        s.append(e)
    elif dc=='pop':
        print(s.pop()) if len(s)!=0 else print(-1)
    elif dc=='siz':
        print(len(s))
    elif dc=='emp':
        print(0) if len(s)!=0 else print(1)
    else:
        print(s[-1]) if len(s)!=0 else print(-1)