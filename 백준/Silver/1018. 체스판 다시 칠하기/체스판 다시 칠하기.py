from sys import stdin as si
m,n=map(int,si.readline().split())
l=si.readlines()
aw=['WBWBWBWB','BWBWBWBW']
cal=[]  # 연산결과
for i0 in range(m-7):
    rows=l[i0:i0+8]
    for i1 in range(n-7):
        # Case 1
        row=[]; c=0
        for i2 in range(8):
            row.append(rows[i2][i1:i1+8])
        for x in range(4):
            for y in range(8):
                if row[2*x][y]==aw[0][y]:
                    continue
                else: c+=1
        for x in range(4):
            for y in range(8):
                if row[2*x+1][y]==aw[1][y]:
                    continue
                else: c+=1
        cal.append(c)
        # Case 2
        c=0
        for x in range(4):
            for y in range(8):
                if row[2*x][y]==aw[1][y]:
                    continue
                else: c+=1
        for x in range(4):
            for y in range(8):
                if row[2*x+1][y]==aw[0][y]:
                    continue
                else: c+=1
        cal.append(c)
print(min(cal))