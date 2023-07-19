n=1     # 곱셈의 항등원 이용
for i in range(3):
    n*=int(input())
s=str(n); d={}
for i in range(10):
    count=0
    for w in s:
        if w==chr(i+48):
            count+=1
    d[i]=count
print('\n'.join(map(str,d.values())))