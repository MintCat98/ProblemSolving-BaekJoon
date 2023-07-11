import sys
a,b,c=0,0,[]
while True:
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    c.append([a,b])
for i in range(len(c)):
    print(c[i][0]+c[i][1])