import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
b2=b//100
b1=(b//10)-(b2*10)
b0=b-((b1*10)+(b2*100))
r=[a*b0,a*b1,a*b2]
for i in range(3):
    print(r[i])
print(a*b)