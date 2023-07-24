from sys import stdin as si
for _ in range(int(si.readline())):
    s=[]    # array-based stack
    p=si.readline()[:-1]
    # close로 시작하면 바로 종료
    if p[0]==')': print('NO')
    else:
        for i in p:
            # open이면 push
            if i=='(': s.append(i)
            # close면 pop
            else:
                try: s.pop()
                # close가 더 많으면 pop 불가능하므로 예외처리
                except: print('NO'); break
        else: print('YES') if len(s)==0 else print('NO')