from sys import stdin as si
cs=[0]*10001    # 0~10000
for _ in range(int(si.readline())):
    cs[int(si.readline())]+=1
for i in range(10001):
    for _ in range(cs[i]): print(i)