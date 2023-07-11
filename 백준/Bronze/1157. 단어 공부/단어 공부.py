w=input().strip().upper()
s=set(w); d={}
for i in s:
    count=0
    for j in w:
        if j==i:
            count+=1
    d[i]=count
l=[k for k,v in d.items() if max(d.values())==v]
print(l[0]) if len(l)==1 else print('?')