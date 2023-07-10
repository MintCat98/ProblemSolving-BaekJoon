h,m=map(int,input().split())
d=int(input())
if d//60>0:
    a,b=d//60,d%60
else:
    a,b=0,d
h+=a
m+=b
if m<60:
    print(h,m) if h<24 else print(h-24,m)
else:
    print(h+1,m%60) if h+1<24 else print(h+1-24,m%60)