l=list(map(int,input().split()))
s=set()
for i in range(7):
    s.add(0) if l[i]<l[i+1] else s.add(1)
if s=={0}: print('ascending')
elif s=={1}: print('descending')
else: print('mixed')