n=int(input())
x=n//5; y=n//3
cal=[]
for i in range(x,-1,-1):
    for j in range(0,y+1):
        if 5*i+3*j==n:
            cal.append(i+j)
print(min(cal)) if len(cal)!=0 else print(-1)