for _ in range(int(input())):
    h,w,n=map(int,input().split())
    a=n%h; b=n//h+1
    if a==0:
        a=h; b=n//h
    a=str(a); b=str(b)
    print(a+b) if len(b)==2 else print(a+'0'+b)