from sys import stdin as si
l=si.readlines()[1][:-1]
c=0
for i in range(len(l)):
    c+=(ord(l[i])-96)*(31**i)
print(c%1234567891)
