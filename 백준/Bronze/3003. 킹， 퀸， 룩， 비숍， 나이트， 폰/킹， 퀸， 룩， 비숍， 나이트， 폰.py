l1=[1,1,2,2,2,8]
l2=list(map(int,input().split()))
for i in range(6):
    l1[i]=l1[i]-l2[i]
print(*l1)