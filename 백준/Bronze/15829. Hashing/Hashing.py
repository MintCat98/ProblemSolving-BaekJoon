from sys import stdin as si
l=int(si.readline())
s=si.readline()[:-1]
r=31; m=1234567891
c=0
for i in range(l):
    c+=(ord(s[i])-96)*(r**i)
print(c%m)
