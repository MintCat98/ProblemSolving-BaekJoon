# 정렬리스트 테스트
n,m=map(int,input().split())
l=list(map(int,input().split())); l.sort(reverse=True)
save=0
for i in range(n-2):
    for j in range(i+1,n-1):    # 중복 방지
        for k in range(j+1,n):
            s=l[i]+l[j]+l[k]
            if s<=m:
                if s>save: save=s; break
print(save)