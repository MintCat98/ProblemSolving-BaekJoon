from sys import stdin as si
n=int(si.readline())
an=list(map(int,si.readlines()))
s_temp=[]   # 임시 스택
s_res=[]    # 결과 스택
oper=[]     # 연산 과정
c=0
for i in range(n):
    s_temp.append(i+1)
    oper.append('+')
    lg=len(s_temp)
    for j in range(lg):
        if s_temp[lg-j-1]==an[c]:
            s_res.append(s_temp.pop())
            c+=1
            oper.append('-')
        else: break
print('NO') if len(s_res)!=n else print('\n'.join(oper))